import logging
from datetime import datetime
from typing import Literal

import requests
import snappy
import xmltodict
from cachetools.func import ttl_cache
from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND, HTTP_503_SERVICE_UNAVAILABLE
from valveprotos_py.citadel_gcmessages_client_pb2 import (
    CMsgCitadelProfileCard,
    CMsgClientToGCGetActiveMatches,
    CMsgClientToGCGetLeaderboard,
    CMsgClientToGCGetLeaderboardResponse,
    CMsgClientToGCGetMatchHistory,
    CMsgClientToGCGetMatchHistoryResponse,
    CMsgClientToGCGetMatchMetaData,
    CMsgClientToGCGetMatchMetaDataResponse,
    CMsgClientToGCGetProfileCard,
    k_EMsgClientToGCGetActiveMatches,
    k_EMsgClientToGCGetLeaderboard,
    k_EMsgClientToGCGetMatchHistory,
    k_EMsgClientToGCGetMatchMetaData,
    k_EMsgClientToGCGetProfileCard,
)
from valveprotos_py.citadel_gcmessages_common_pb2 import (
    k_ECitadelLeaderboardRegion_Asia,
    k_ECitadelLeaderboardRegion_Europe,
    k_ECitadelLeaderboardRegion_NAmerica,
    k_ECitadelLeaderboardRegion_Oceania,
    k_ECitadelLeaderboardRegion_SAmerica,
)

from deadlock_data_api.conf import CONFIG
from deadlock_data_api.globs import CH_POOL, postgres_conn
from deadlock_data_api.models.build import Build
from deadlock_data_api.models.leaderboard import Leaderboard
from deadlock_data_api.models.patch_note import PatchNote
from deadlock_data_api.models.player_card import PlayerCard
from deadlock_data_api.models.player_match_history import (
    PlayerMatchHistory,
    PlayerMatchHistoryEntry,
)
from deadlock_data_api.utils import (
    call_steam_proxy,
    call_steam_proxy_raw,
    send_webhook_message,
)

CACHE_AGE_ACTIVE_MATCHES = 20
CACHE_AGE_BUILDS = 5 * 60
LOAD_FILE_RETRIES = 5

LOGGER = logging.getLogger(__name__)


@ttl_cache(ttl=900)
def get_player_match_history(
    account_id: int, continue_cursor: int | None = None, account_groups: str | None = None
) -> PlayerMatchHistory:
    if CONFIG.deactivate_match_history and account_groups is None:
        raise HTTPException(
            status_code=HTTP_503_SERVICE_UNAVAILABLE,
            detail="Calls to Steam API are currently unavailable, try analytics match history instead",
        )
    msg = CMsgClientToGCGetMatchHistory()
    msg.account_id = account_id
    if continue_cursor is not None:
        msg.continue_cursor = continue_cursor
    msg = call_steam_proxy(
        k_EMsgClientToGCGetMatchHistory,
        msg,
        CMsgClientToGCGetMatchHistoryResponse,
        15_000,  # 4 per minute
        account_groups.split(",") if account_groups else ["GetMatchHistory"],
    )
    match_history = [PlayerMatchHistoryEntry.from_msg(m) for m in msg.matches]
    match_history = sorted(match_history, key=lambda x: x.start_time, reverse=True)
    with CH_POOL.get_client() as client:
        PlayerMatchHistoryEntry.store_clickhouse(client, account_id, match_history)
    return PlayerMatchHistory(cursor=msg.continue_cursor, matches=match_history)


@ttl_cache(ttl=60 * 60)
def get_match_salts_from_db(
    match_id: int, need_demo: bool = False
) -> CMsgClientToGCGetMatchMetaDataResponse | None:
    with CH_POOL.get_client() as client:
        result = client.execute(
            "SELECT metadata_salt, replay_salt, cluster_id FROM match_salts WHERE match_id = %(match_id)s",
            {"match_id": match_id},
        )
    if result:
        result = result[0]
        if not need_demo or result[1] != 0:
            return CMsgClientToGCGetMatchMetaDataResponse(
                metadata_salt=result[0], replay_salt=result[1], cluster_id=result[2]
            )
    return None


@ttl_cache(ttl=60 * 60)
def get_match_start_time(match_id: int) -> datetime | None:
    with CH_POOL.get_client() as client:
        result = client.execute(
            "SELECT start_time FROM match_info WHERE match_id <= %(match_id)s ORDER BY match_id DESC LIMIT 1",
            {"match_id": match_id},
        )
    return result[0][0] if result else None


@ttl_cache(ttl=60 * 60)
def get_match_salts_from_steam(
    match_id: int, need_demo: bool = False, account_groups: str | None = None
) -> CMsgClientToGCGetMatchMetaDataResponse:
    if CONFIG.deactivate_match_metadata and account_groups is None:
        raise HTTPException(
            status_code=HTTP_503_SERVICE_UNAVAILABLE,
            detail="Calls to Steam API are currently unavailable",
        )
    msg = CMsgClientToGCGetMatchMetaData()
    msg.match_id = match_id
    msg = call_steam_proxy(
        k_EMsgClientToGCGetMatchMetaData,
        msg,
        CMsgClientToGCGetMatchMetaDataResponse,
        576_000 if not account_groups else 1,  # 25 per 4 hours
        account_groups.split(",") if account_groups else ["GetMatchMetaData"],
    )
    if msg.metadata_salt == 0 or (need_demo and msg.replay_salt == 0):
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Match not found")
    with CH_POOL.get_client() as client:
        client.execute(
            "INSERT INTO match_salts (match_id, metadata_salt, replay_salt, cluster_id) VALUES (%(match_id)s, %(metadata_salt)s, %(replay_salt)s, %(cluster_id)s)",
            {
                "match_id": match_id,
                "metadata_salt": msg.metadata_salt,
                "replay_salt": msg.replay_salt,
                "cluster_id": msg.cluster_id,
            },
        )
    return msg


def fetch_metadata(match_id: int, salts: CMsgClientToGCGetMatchMetaDataResponse) -> bytes:
    meta_url = f"http://replay{salts.cluster_id}.valve.net/1422450/{match_id}_{salts.metadata_salt}.meta.bz2"
    metafile = requests.get(meta_url)
    metafile.raise_for_status()
    metafile = metafile.content
    return metafile


@ttl_cache(ttl=CACHE_AGE_BUILDS - 1)
def load_builds(
    start: int | None = None,
    limit: int | None = 100,
    sort_by: Literal["favorites", "ignores", "reports", "updated_at"] = "favorites",
    sort_direction: Literal["asc", "desc"] = "desc",
    search_name: str | None = None,
    search_description: str | None = None,
    only_latest: bool = False,
    language: int | None = None,
) -> list[Build]:
    query = """
    WITH latest_build_versions as (SELECT DISTINCT ON (build_id) build_id, version
                          FROM hero_builds
                          ORDER BY build_id, version DESC)
    SELECT data as builds
    FROM hero_builds
    WHERE TRUE
    """
    if only_latest:
        query += " AND (build_id, version) IN (SELECT build_id, version FROM latest_build_versions)"
    if search_name is not None:
        search_name = search_name.lower()
        query += f" AND lower(data->'hero_build'->>'name') LIKE '%%{search_name}%%'"
    if search_description is not None:
        search_description = search_description.lower()
        query += f" AND lower(data->'hero_build'->>'description') LIKE '%%{search_description}%%'"
    if language is not None:
        query += f" AND language = {language}"
    args = []
    if sort_by is not None:
        if sort_by == "favorites":
            query += " ORDER BY favorites"
        elif sort_by == "ignores":
            query += " ORDER BY ignores"
        elif sort_by == "reports":
            query += " ORDER BY reports"
        elif sort_by == "updated_at":
            query += " ORDER BY updated_at"
        if sort_direction is not None:
            query += f" {sort_direction}"

    if limit is not None or start is not None:
        if start is None:
            start = 0
        if limit is None:
            raise HTTPException(status_code=400, detail="Start cannot be provided without limit")
        if limit != -1:
            query += " LIMIT %s OFFSET %s"
            args += [limit, start]

    conn = postgres_conn()
    with conn.cursor() as cursor:
        cursor.execute(query, tuple(args))
        results = cursor.fetchall()
    return [b for b in [Build.model_validate(result[0]) for result in results] if b]


@ttl_cache(ttl=CACHE_AGE_BUILDS - 1)
def load_builds_by_hero(
    hero_id: int,
    start: int | None = None,
    limit: int | None = 100,
    sort_by: (Literal["favorites", "ignores", "reports", "updated_at"] | None) = "favorites",
    sort_direction: Literal["asc", "desc"] = "desc",
    search_name: str | None = None,
    search_description: str | None = None,
    only_latest: bool = False,
    language: int | None = None,
) -> list[Build]:
    query = """
    WITH latest_build_versions as (SELECT DISTINCT ON (build_id) build_id, version
                          FROM hero_builds
                          ORDER BY build_id, version DESC)
    SELECT data as builds
    FROM hero_builds
    WHERE hero = %s
    """
    if only_latest:
        query += " AND (build_id, version) IN (SELECT build_id, version FROM latest_build_versions)"
    if search_name is not None:
        search_name = search_name.lower()
        query += f" AND lower(data->'hero_build'->>'name') LIKE '%%{search_name}%%'"
    if search_description is not None:
        search_description = search_description.lower()
        query += f" AND lower(data->'hero_build'->>'description') LIKE '%%{search_description}%%'"
    if language is not None:
        query += f" AND language = {language}"
    args = [hero_id]
    if sort_by is not None:
        if sort_by == "favorites":
            query += " ORDER BY favorites"
        elif sort_by == "ignores":
            query += " ORDER BY ignores"
        elif sort_by == "reports":
            query += " ORDER BY reports"
        elif sort_by == "updated_at":
            query += " ORDER BY updated_at"
        if sort_direction is not None:
            query += f" {sort_direction}"

    if limit is not None or start is not None:
        if start is None:
            start = 0
        if limit is None:
            raise HTTPException(status_code=400, detail="Start cannot be provided without limit")
        if limit != -1:
            query += " LIMIT %s OFFSET %s"
            args += [limit, start]

    conn = postgres_conn()
    with conn.cursor() as cursor:
        cursor.execute(query, tuple(args))
        results = cursor.fetchall()
    return [b for b in [Build.model_validate(result[0]) for result in results] if b]


@ttl_cache(ttl=CACHE_AGE_BUILDS - 1)
def load_builds_by_author(
    author_id: int,
    start: int | None = None,
    limit: int | None = 100,
    sort_by: Literal["favorites", "ignores", "reports", "updated_at"] = "favorites",
    sort_direction: Literal["asc", "desc"] = "desc",
    only_latest: bool = False,
) -> list[Build]:
    query = """
    WITH latest_build_versions as (SELECT DISTINCT ON (build_id) build_id, version
                          FROM hero_builds
                          ORDER BY build_id, version DESC)
    SELECT data as builds
    FROM hero_builds
    WHERE author_id = %s
    """
    if only_latest:
        query += " AND (build_id, version) IN (SELECT build_id, version FROM latest_build_versions)"
    args = [author_id]
    if sort_by is not None:
        if sort_by == "favorites":
            query += " ORDER BY favorites"
        elif sort_by == "ignores":
            query += " ORDER BY ignores"
        elif sort_by == "reports":
            query += " ORDER BY reports"
        elif sort_by == "updated_at":
            query += " ORDER BY updated_at"
        if sort_direction is not None:
            query += f" {sort_direction}"

    if limit is not None or start is not None:
        if start is None:
            start = 0
        if limit is None:
            raise HTTPException(status_code=400, detail="Start cannot be provided without limit")
        if limit != -1:
            query += " LIMIT %s OFFSET %s"
            args += [limit, start]

    conn = postgres_conn()
    with conn.cursor() as cursor:
        cursor.execute(query, tuple(args))
        results = cursor.fetchall()
    return [b for b in [Build.model_validate(result[0]) for result in results] if b]


@ttl_cache(ttl=CACHE_AGE_BUILDS - 1)
def load_build(build_id: int) -> Build:
    query = "SELECT data FROM hero_builds WHERE build_id = %s ORDER BY version DESC LIMIT 1"
    conn = postgres_conn()
    with conn.cursor() as cursor:
        cursor.execute(query, (build_id,))
        result = cursor.fetchone()
        if result is None:
            raise HTTPException(status_code=404, detail="Build not found")
        return Build.model_validate(result[0])


@ttl_cache(ttl=CACHE_AGE_BUILDS - 1)
def load_build_version(build_id: int, version: int) -> Build:
    query = "SELECT data FROM hero_builds WHERE build_id = %s AND version = %s"
    conn = postgres_conn()
    with conn.cursor() as cursor:
        cursor.execute(query, (build_id, version))
        result = cursor.fetchone()
        if result is None:
            raise HTTPException(status_code=404, detail="Build not found")
        return Build.model_validate(result[0])


@ttl_cache(ttl=CACHE_AGE_ACTIVE_MATCHES)
def fetch_active_matches_raw(account_groups: str | None = None) -> bytes:
    try:
        msg = call_steam_proxy_raw(
            k_EMsgClientToGCGetActiveMatches,
            CMsgClientToGCGetActiveMatches(),
            10,
            account_groups.split(",") if account_groups else ["LowRateLimitApis"],
        )
        return snappy.decompress(msg[7:])
    except Exception as e:
        if isinstance(e, requests.exceptions.HTTPError):
            send_webhook_message(
                f"Failed to fetch active matches: HTTPError: {e.response.status_code}",
            )
            LOGGER.exception(f"Failed to fetch active matches: HTTPError: {e.response.status_code}")
        else:
            send_webhook_message(f"Failed to fetch active matches: {type(e).__name__}")
            LOGGER.exception(f"Failed to fetch active matches: {type(e).__name__}")
        raise HTTPException(status_code=500, detail="Failed to fetch active matches")


@ttl_cache(ttl=30 * 60)
def fetch_patch_notes() -> list[PatchNote]:
    rss_url = "https://forums.playdeadlock.com/forums/changelog.10/index.rss"
    response = requests.get(rss_url)
    items = xmltodict.parse(response.text)["rss"]["channel"]["item"]
    return [PatchNote.model_validate(item) for item in items]


@ttl_cache(ttl=900)
def get_player_rank(account_id: int, account_groups: str | None = None) -> PlayerCard:
    msg = CMsgClientToGCGetProfileCard()
    msg.account_id = account_id
    msg = call_steam_proxy(
        k_EMsgClientToGCGetProfileCard,
        msg,
        CMsgCitadelProfileCard,
        10,
        account_groups.split(",") if account_groups else ["LowRateLimitApis"],
    )
    player_card = PlayerCard.from_msg(msg)
    with CH_POOL.get_client() as client:
        player_card.store_clickhouse(client, account_id)
    return player_card


@ttl_cache(ttl=900)
def get_leaderboard(
    region: Literal["Europe", "Asia", "NAmerica", "SAmerica", "Oceania"],
    hero_id: int | None = None,
    account_groups: str | None = None,
) -> Leaderboard:
    msg = CMsgClientToGCGetLeaderboard()
    msg.hero_id = hero_id
    match region:
        case "Europe":
            msg.leaderboard_region = k_ECitadelLeaderboardRegion_Europe
        case "Asia":
            msg.leaderboard_region = k_ECitadelLeaderboardRegion_Asia
        case "NAmerica":
            msg.leaderboard_region = k_ECitadelLeaderboardRegion_NAmerica
        case "SAmerica":
            msg.leaderboard_region = k_ECitadelLeaderboardRegion_SAmerica
        case "Oceania":
            msg.leaderboard_region = k_ECitadelLeaderboardRegion_Oceania
    msg = call_steam_proxy(
        k_EMsgClientToGCGetLeaderboard,
        msg,
        CMsgClientToGCGetLeaderboardResponse,
        10,
        account_groups.split(",") if account_groups else ["LowRateLimitApis"],
    )
    return Leaderboard.from_msg(msg)
