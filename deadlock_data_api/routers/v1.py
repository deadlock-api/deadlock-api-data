import logging
import os
from typing import Literal

import requests
from cachetools.func import ttl_cache
from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import Response, StreamingResponse
from valveprotos_py.citadel_gcmessages_client_pb2 import (
    CMsgCitadelProfileCard,
    CMsgClientToGCGetProfileCard,
    k_EMsgClientToGCGetProfileCard,
)

from deadlock_data_api import utils
from deadlock_data_api.globs import CH_POOL, s3_conn
from deadlock_data_api.models.active_match import ActiveMatch
from deadlock_data_api.models.build import Build
from deadlock_data_api.models.player_card import PlayerCard
from deadlock_data_api.models.player_match_history import PlayerMatchHistoryEntry
from deadlock_data_api.rate_limiter import limiter
from deadlock_data_api.rate_limiter.models import RateLimit
from deadlock_data_api.routers.v1_utils import (
    fetch_active_matches,
    fetch_patch_notes,
    get_match_salts,
    get_player_match_history,
    load_build,
    load_build_version,
    load_builds,
    load_builds_by_author,
    load_builds_by_hero,
)
from deadlock_data_api.utils import call_steam_proxy

CACHE_AGE_ACTIVE_MATCHES = 20
CACHE_AGE_BUILDS = 5 * 60

LOGGER = logging.getLogger(__name__)

router = APIRouter(prefix="/v1")


@router.get("/patch-notes")
def get_patch_notes(res: Response):
    LOGGER.info("get_patch_notes")
    res.headers["Cache-Control"] = f"public, max-age={30 * 60}"
    return fetch_patch_notes()


@router.get("/builds", response_model_exclude_none=True)
def get_builds(
    req: Request,
    res: Response,
    start: int | None = None,
    limit: int | None = 100,
    sort_by: Literal["favorites", "ignores", "reports", "updated_at"] = "favorites",
    sort_direction: Literal["asc", "desc"] = "desc",
    search_name: str | None = None,
    search_description: str | None = None,
    only_latest: bool | None = None,
) -> list[Build]:
    only_latest = only_latest or False
    LOGGER.info("get_builds")
    limiter.apply_limits(req, res, "/v1/builds", [RateLimit(limit=10, period=1)])
    res.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_BUILDS}"
    return load_builds(
        start,
        limit,
        sort_by,
        sort_direction,
        search_name,
        search_description,
        only_latest,
    )


@router.get("/builds/{build_id}", response_model_exclude_none=True)
def get_build(
    req: Request, res: Response, build_id: int, version: int | None = None
) -> Build:
    LOGGER.info("get_build")
    limiter.apply_limits(req, res, "/v1/builds/{id}", [RateLimit(limit=100, period=1)])
    res.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_BUILDS}"
    return (
        load_build(build_id)
        if version is None
        else load_build_version(build_id, version)
    )


@router.get("/builds/by-hero-id/{hero_id}", response_model_exclude_none=True)
def get_builds_by_hero_id(
    req: Request,
    res: Response,
    hero_id: int,
    start: int | None = None,
    limit: int | None = 100,
    sort_by: Literal["favorites", "ignores", "reports", "updated_at"] = "favorites",
    sort_direction: Literal["asc", "desc"] = "desc",
    search_name: str | None = None,
    search_description: str | None = None,
    only_latest: bool | None = None,
) -> list[Build]:
    only_latest = only_latest or False
    LOGGER.info("get_builds_by_hero_id")
    limiter.apply_limits(
        req, res, "/v1/builds/by-hero-id/{hero_id}", [RateLimit(limit=100, period=1)]
    )
    res.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_BUILDS}"
    return load_builds_by_hero(
        hero_id,
        start,
        limit,
        sort_by,
        sort_direction,
        search_name,
        search_description,
        only_latest,
    )


@router.get("/builds/by-author-id/{author_id}", response_model_exclude_none=True)
def get_builds_by_author_id(
    req: Request,
    res: Response,
    author_id: int,
    start: int | None = None,
    limit: int | None = 100,
    sort_by: Literal["favorites", "ignores", "reports", "updated_at"] = "favorites",
    sort_direction: Literal["asc", "desc"] = "desc",
    only_latest: bool | None = None,
) -> list[Build]:
    only_latest = only_latest or False
    LOGGER.info("get_builds_by_author_id")
    limiter.apply_limits(
        req,
        res,
        "/v1/builds/by-author-id/{author_id}",
        [RateLimit(limit=100, period=1)],
    )
    res.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_BUILDS}"
    return load_builds_by_author(
        author_id, start, limit, sort_by, sort_direction, only_latest
    )


@router.get(
    "/active-matches",
    response_model_exclude_none=True,
    summary="Updates every 20s | Rate Limit 15req/20s",
)
def get_active_matches(
    req: Request, res: Response, account_id: int | None = None
) -> list[ActiveMatch]:
    LOGGER.info("get_active_matches")
    limiter.apply_limits(
        req, res, "/v1/active-matches", [RateLimit(limit=15, period=20)]
    )
    last_modified = os.path.getmtime("active_matches.json")
    res.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_ACTIVE_MATCHES}"
    res.headers["Last-Updated"] = str(int(last_modified))
    account_id = utils.validate_steam_id(account_id)

    def has_player(am: ActiveMatch, account_id: int) -> bool:
        for p in am.players:
            if p.account_id == account_id:
                return True
        return False

    return [
        a
        for a in fetch_active_matches()
        if account_id is None or has_player(a, account_id)
    ]


@router.get(
    "/players/{account_id}/rank",
    response_model_exclude_none=True,
    summary="Rate Limit 10req/min, API-Key RateLimit: 100req/min & 5000req/h, Ask for an increase if needed",
)
def player_rank(
    req: Request,
    res: Response,
    account_id: int,
) -> PlayerCard:
    LOGGER.info("player_rank")
    limiter.apply_limits(
        req,
        res,
        "/v1/players/{account_id}/rank",
        [RateLimit(limit=10, period=60)],
        [RateLimit(limit=100, period=60), RateLimit(limit=5000, period=3600)],
        [RateLimit(limit=1200, period=60)],
    )
    res.headers["Cache-Control"] = "public, max-age=900"
    account_id = utils.validate_steam_id(account_id)
    return get_player_rank(account_id)


@ttl_cache(ttl=900)
def get_player_rank(account_id: int) -> PlayerCard:
    msg = CMsgClientToGCGetProfileCard()
    msg.account_id = account_id
    msg = call_steam_proxy(k_EMsgClientToGCGetProfileCard, msg, CMsgCitadelProfileCard)
    player_card = PlayerCard.from_msg(msg)
    with CH_POOL.get_client() as client:
        player_card.store_clickhouse(client, account_id)
    return player_card


@router.get(
    "/players/{account_id}/match-history",
    response_model_exclude_none=True,
    summary="Rate Limit 10req/min, API-Key RateLimit: 100req/min & 5000req/h",
)
def player_match_history(
    req: Request,
    res: Response,
    account_id: int,
) -> list[PlayerMatchHistoryEntry]:
    LOGGER.info("player_match_history")
    limiter.apply_limits(
        req,
        res,
        "/v1/players/{account_id}/match-history",
        [RateLimit(limit=10, period=60)],
        [RateLimit(limit=100, period=60), RateLimit(limit=5000, period=3600)],
        [RateLimit(limit=1200, period=60)],
    )
    res.headers["Cache-Control"] = "public, max-age=900"
    account_id = utils.validate_steam_id(account_id)
    return get_player_match_history(account_id)


@router.get(
    "/matches/{match_id}/raw_metadata",
    description="""
# Raw Metadata

This endpoints streams the raw .meta.bz2 file for the given `match_id`.

You have to decompress it and decode the protobuf message.

Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

At the moment the rate limits are quite strict, as we are serving it from an s3 with egress costs, but that may change.
    """,
    summary="RateLimit: 1req/min & 100req/h, API-Key RateLimit: 10req/min",
)
def get_raw_metadata_file(
    req: Request, res: Response, match_id: int
) -> StreamingResponse:
    limiter.apply_limits(
        req,
        res,
        "/v1/matches/{match_id}/raw_metadata",
        [RateLimit(limit=1, period=60), RateLimit(limit=100, period=3600)],
        [RateLimit(limit=10, period=60)],
        [RateLimit(limit=3, period=1)],
    )
    bucket = os.environ.get("S3_BUCKET_NAME", "hexe")
    key = f"processed/metadata/{match_id}.meta.bz2"
    s3 = s3_conn()
    object_exists = True
    try:
        s3.head_object(Bucket=bucket, Key=key)
    except s3.exceptions.ClientError:
        object_exists = False
    if object_exists:
        obj = s3.get_object(Bucket=bucket, Key=key)
    else:
        salts, _ = get_match_salts(match_id)
        meta_url = f"http://replay{salts.cluster_id}.valve.net/1422450/{match_id}_{salts.metadata_salt}.meta.bz2"
        metafile = requests.get(meta_url)
        metafile.raise_for_status()
        metafile = metafile.content
        s3.put_object(
            Bucket=bucket, Key=f"ingest/metadata/{match_id}.meta.bz2", Body=metafile
        )
        obj = s3.get_object(Bucket=bucket, Key=key)
    return StreamingResponse(
        obj["Body"],
        media_type="application/octet-stream",
        headers={
            "Content-Disposition": f"attachment; filename={match_id}.meta.bz2",
            "Cache-Control": "public, max-age=1200",
        },
    )


@router.get(
    "/matches/{match_id}/demo-url",
    summary="RateLimit: 1req/min & 100req/h, API-Key RateLimit: 10req/min",
)
def get_demo_url(req: Request, res: Response, match_id: int) -> dict[str, str]:
    salts, from_db = get_match_salts(match_id, True)
    if from_db:
        limiter.apply_limits(
            req,
            res,
            "/v1/matches/{match_id}/demo-url#db",
            [RateLimit(limit=60, period=60), RateLimit(limit=1000, period=3600)],
            [RateLimit(limit=60, period=60)],
            [RateLimit(limit=3, period=1)],
        )
    else:
        limiter.apply_limits(
            req,
            res,
            "/v1/matches/{match_id}/demo-url#gc",
            [RateLimit(limit=1, period=60), RateLimit(limit=100, period=3600)],
            [RateLimit(limit=5, period=60)],
            [RateLimit(limit=3, period=1)],
        )
    demo_url = f"http://replay{salts.cluster_id}.valve.net/1422450/{match_id}_{salts.replay_salt}.dem.bz2"
    return {"demo_url": demo_url}
