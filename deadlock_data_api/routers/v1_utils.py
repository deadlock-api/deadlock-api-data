import logging
import os
from time import sleep
from typing import Literal

import requests
import snappy
import xmltodict
from cachetools.func import ttl_cache
from fastapi import HTTPException
from valveprotos_py.citadel_gcmessages_client_pb2 import (
    CMsgClientToGCGetActiveMatches,
    CMsgClientToGCGetActiveMatchesResponse,
    CMsgClientToGCGetMatchHistory,
    CMsgClientToGCGetMatchHistoryResponse,
    CMsgClientToGCGetMatchMetaData,
    CMsgClientToGCGetMatchMetaDataResponse,
    k_EMsgClientToGCGetActiveMatches,
    k_EMsgClientToGCGetMatchHistory,
    k_EMsgClientToGCGetMatchMetaData,
)

from deadlock_data_api.globs import CH_POOL, postgres_conn
from deadlock_data_api.models.active_match import ActiveMatch, APIActiveMatch
from deadlock_data_api.models.build import Build
from deadlock_data_api.models.patch_note import PatchNote
from deadlock_data_api.models.player_match_history import PlayerMatchHistoryEntry
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
def get_player_match_history(account_id: int) -> list[PlayerMatchHistoryEntry]:
    msg = CMsgClientToGCGetMatchHistory()
    msg.account_id = account_id
    msg = call_steam_proxy(
        k_EMsgClientToGCGetMatchHistory, msg, CMsgClientToGCGetMatchHistoryResponse
    )
    match_history = [PlayerMatchHistoryEntry.from_msg(m) for m in msg.matches]
    match_history = sorted(match_history, key=lambda x: x.start_time, reverse=True)
    with CH_POOL.get_client() as client:
        PlayerMatchHistoryEntry.store_clickhouse(client, account_id, match_history)
    return match_history


@ttl_cache(ttl=60)
def get_match_salts(match_id: int) -> CMsgClientToGCGetMatchMetaDataResponse:
    msg = CMsgClientToGCGetMatchMetaData()
    msg.match_id = match_id
    msg = call_steam_proxy(
        k_EMsgClientToGCGetMatchMetaData, msg, CMsgClientToGCGetMatchMetaDataResponse
    )
    requests.post(
        f"https://analytics.deadlock-api.com/v1/match-salts?api_key={os.environ['INTERNAL_DEADLOCK_API_KEY']}",
        json=[
            {
                "cluster_id": msg.cluster_id,
                "match_id": match_id,
                "metadata_salt": msg.metadata_salt,
                "replay_salt": msg.replay_salt,
            }
        ],
    ).raise_for_status()
    return msg


@ttl_cache(ttl=CACHE_AGE_BUILDS - 1)
def load_builds(
    start: int | None = None,
    limit: int | None = 100,
    sort_by: Literal["favorites", "ignores", "reports", "updated_at"] = "favorites",
    sort_direction: Literal["asc", "desc"] = "desc",
    only_latest: bool = False,
) -> list[Build]:
    LOGGER.debug("load_builds")
    query = """
    WITH latest_build_ids as (SELECT DISTINCT ON (build_id, version) (build_id)
                          FROM hero_builds
                          ORDER BY version DESC)
    SELECT data as builds
    FROM hero_builds
    WHERE build_id IN (SELECT * FROM latest_build_ids) OR %s = 1
    """
    args = [int(only_latest)]
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
            raise HTTPException(
                status_code=400, detail="Start cannot be provided without limit"
            )
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
    sort_by: (
        Literal["favorites", "ignores", "reports", "updated_at"] | None
    ) = "favorites",
    sort_direction: Literal["asc", "desc"] = "desc",
    only_latest: bool = False,
) -> list[Build]:
    LOGGER.debug("load_builds_by_hero")
    query = """
    WITH latest_build_ids as (SELECT DISTINCT ON (build_id, version) (build_id)
                          FROM hero_builds
                          ORDER BY version DESC)
    SELECT data as builds
    FROM hero_builds
    WHERE (build_id IN (SELECT * FROM latest_build_ids) OR %s = 1) AND hero = %s
    """
    args = [int(only_latest), hero_id]
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
            raise HTTPException(
                status_code=400, detail="Start cannot be provided without limit"
            )
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
    LOGGER.debug("load_builds_by_author")
    query = """
    WITH latest_build_ids as (SELECT DISTINCT ON (build_id, version) (build_id)
                          FROM hero_builds
                          ORDER BY version DESC)
    SELECT data as builds
    FROM hero_builds
    WHERE (build_id IN (SELECT * FROM latest_build_ids) OR %s = 1) AND author_id = %s
    """
    args = [int(only_latest), author_id]
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
            raise HTTPException(
                status_code=400, detail="Start cannot be provided without limit"
            )
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
    LOGGER.debug("load_build")
    query = (
        "SELECT data FROM hero_builds WHERE build_id = %s ORDER BY version DESC LIMIT 1"
    )
    conn = postgres_conn()
    with conn.cursor() as cursor:
        cursor.execute(query, (build_id,))
        result = cursor.fetchone()
        if result is None:
            raise HTTPException(status_code=404, detail="Build not found")
        return Build.model_validate(result[0])


@ttl_cache(ttl=CACHE_AGE_BUILDS - 1)
def load_build_version(build_id: int, version: int) -> Build:
    LOGGER.debug("load_build_version")
    query = "SELECT data FROM hero_builds WHERE build_id = %s AND version = %s"
    conn = postgres_conn()
    with conn.cursor() as cursor:
        cursor.execute(query, (build_id, version))
        result = cursor.fetchone()
        if result is None:
            raise HTTPException(status_code=404, detail="Build not found")
        return Build.model_validate(result[0])


@ttl_cache(ttl=CACHE_AGE_ACTIVE_MATCHES)
def fetch_active_matches() -> list[ActiveMatch]:
    try:
        LOGGER.debug("fetch_active_matches")
        msg = call_steam_proxy_raw(
            k_EMsgClientToGCGetActiveMatches, CMsgClientToGCGetActiveMatches()
        )
        return [
            ActiveMatch.from_msg(m)
            for m in CMsgClientToGCGetActiveMatchesResponse.FromString(
                snappy.decompress(msg[7:])
            ).active_matches
        ]
    except Exception:
        return load_active_matches()


@ttl_cache(ttl=CACHE_AGE_ACTIVE_MATCHES)
def load_active_matches() -> list[ActiveMatch]:
    LOGGER.debug("load_active_matches")
    last_exc = None
    for i in range(LOAD_FILE_RETRIES):
        try:
            with open("active_matches.json") as f:
                return APIActiveMatch.model_validate_json(f.read()).active_matches
        except Exception as e:
            last_exc = e
            LOGGER.warning(
                f"Error loading active matches: {str(e)}, retry ({i + 1}/{LOAD_FILE_RETRIES})"
            )
        sleep(50)
    send_webhook_message(f"Error loading active matches: {str(last_exc)}")
    raise HTTPException(status_code=500, detail="Failed to load active matches")


@ttl_cache(ttl=30 * 60)
def fetch_patch_notes() -> list[PatchNote]:
    LOGGER.debug("fetch_patch_notes")
    rss_url = "https://forums.playdeadlock.com/forums/changelog.10/index.rss"
    response = requests.get(rss_url)
    items = xmltodict.parse(response.text)["rss"]["channel"]["item"]
    return [PatchNote.model_validate(item) for item in items]