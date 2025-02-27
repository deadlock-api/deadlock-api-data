import logging
from typing import Literal

from fastapi import APIRouter, Depends
from fastapi.openapi.models import APIKey
from starlette.datastructures import URL
from starlette.requests import Request
from starlette.responses import RedirectResponse, Response
from starlette.status import HTTP_301_MOVED_PERMANENTLY

from deadlock_data_api import utils
from deadlock_data_api.models.player_card import PlayerCard
from deadlock_data_api.models.player_match_history import (
    PlayerMatchHistoryEntry,
)
from deadlock_data_api.models.webhook import MatchCreatedWebhookPayload
from deadlock_data_api.rate_limiter import limiter
from deadlock_data_api.rate_limiter.models import RateLimit
from deadlock_data_api.routers.v1_utils import (
    get_player_match_history,
    get_player_rank,
)
from deadlock_data_api.utils import send_webhook_event

# CACHE_AGE_ACTIVE_MATCHES = 20
# CACHE_AGE_BUILDS = 5 * 60

LOGGER = logging.getLogger(__name__)

router = APIRouter(prefix="/v1", tags=["V1"])


@router.get(
    "/patch-notes",
    summary="Moved to new API: http://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: http://api.deadlock-api.com/docs
- New API Endpoint: http://api.deadlock-api.com/v1/patches/big-days
    """,
    deprecated=True,
)
def get_patch_notes():
    return RedirectResponse(
        "https://api.deadlock-api.com/v1/patches", status_code=HTTP_301_MOVED_PERMANENTLY
    )


@router.get(
    "/big-patch-days",
    summary="Moved to new API: http://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: http://api.deadlock-api.com/docs
- New API Endpoint: http://api.deadlock-api.com/v1/patches/big-days
    """,
    deprecated=True,
)
def get_big_patch_days() -> RedirectResponse:
    return RedirectResponse(
        "https://api.deadlock-api.com/v1/patches/big-days", status_code=HTTP_301_MOVED_PERMANENTLY
    )


@router.get(
    "/builds",
    summary="Moved to new API: http://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: http://api.deadlock-api.com/docs
- New API Endpoint: http://api.deadlock-api.com/v1/builds
    """,
    deprecated=True,
)
def get_builds(
    req: Request,
    start: int | None = None,
    limit: int | None = 100,
    sort_by: Literal["favorites", "ignores", "reports", "updated_at"] = "favorites",
    sort_direction: Literal["asc", "desc"] = "desc",
    search_name: str | None = None,
    search_description: str | None = None,
    only_latest: bool | None = None,
    language: int | None = None,
) -> RedirectResponse:
    url = URL("https://api.deadlock-api.com/v1/builds").include_query_params(
        **{k: v for k, v in req.query_params.items() if v is not None}
    )
    return RedirectResponse(url, status_code=HTTP_301_MOVED_PERMANENTLY)


@router.get(
    "/builds/{build_id}",
    summary="Moved to new API: http://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: http://api.deadlock-api.com/docs
- New API Endpoint: http://api.deadlock-api.com/v1/builds
    """,
    deprecated=True,
)
def get_build(build_id: int, version: int | None = None) -> RedirectResponse:
    url = URL("https://api.deadlock-api.com/v1/builds").include_query_params(
        **{k: v for k, v in {"build_id": build_id, "version": version}.items() if v is not None}
    )
    return RedirectResponse(url, status_code=HTTP_301_MOVED_PERMANENTLY)


@router.get(
    "/builds/{build_id}/all-versions",
    summary="Moved to new API: http://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: http://api.deadlock-api.com/docs
- New API Endpoint: http://api.deadlock-api.com/v1/builds
    """,
    deprecated=True,
)
def get_builds_by_build_id(build_id: int) -> RedirectResponse:
    url = URL("https://api.deadlock-api.com/v1/builds").include_query_params(build_id=build_id)
    return RedirectResponse(url, status_code=HTTP_301_MOVED_PERMANENTLY)


@router.get(
    "/builds/by-hero-id/{hero_id}",
    summary="Moved to new API: http://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: http://api.deadlock-api.com/docs
- New API Endpoint: http://api.deadlock-api.com/v1/builds
    """,
    deprecated=True,
)
def get_builds_by_hero_id(
    req: Request,
    hero_id: int,
    start: int | None = None,
    limit: int | None = 100,
    sort_by: Literal["favorites", "ignores", "reports", "updated_at"] = "favorites",
    sort_direction: Literal["asc", "desc"] = "desc",
    search_name: str | None = None,
    search_description: str | None = None,
    only_latest: bool | None = None,
    language: int | None = None,
) -> RedirectResponse:
    url = URL("https://api.deadlock-api.com/v1/builds").include_query_params(
        hero_id=hero_id, **{k: v for k, v in req.query_params.items() if v is not None}
    )
    return RedirectResponse(url, status_code=HTTP_301_MOVED_PERMANENTLY)


@router.get(
    "/builds/by-author-id/{author_id}",
    summary="Moved to new API: http://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: http://api.deadlock-api.com/docs
- New API Endpoint: http://api.deadlock-api.com/v1/builds
    """,
    deprecated=True,
)
def get_builds_by_author_id(
    req: Request,
    author_id: int,
    start: int | None = None,
    limit: int | None = 100,
    sort_by: Literal["favorites", "ignores", "reports", "updated_at"] = "favorites",
    sort_direction: Literal["asc", "desc"] = "desc",
    only_latest: bool | None = None,
) -> RedirectResponse:
    url = URL("https://api.deadlock-api.com/v1/builds").include_query_params(
        author_id=author_id, **{k: v for k, v in req.query_params.items() if v is not None}
    )
    return RedirectResponse(url, status_code=HTTP_301_MOVED_PERMANENTLY)


@router.get(
    "/raw-active-matches",
    summary="Moved to new API: http://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: http://api.deadlock-api.com/docs
- New API Endpoint: http://api.deadlock-api.com/v1/matches/active/raw
    """,
    deprecated=True,
)
def get_active_matches_raw() -> RedirectResponse:
    return RedirectResponse(
        "https://api.deadlock-api.com/v1/matches/active/raw", HTTP_301_MOVED_PERMANENTLY
    )


@router.get(
    "/active-matches",
    summary="Moved to new API: http://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: http://api.deadlock-api.com/docs
- New API Endpoint: http://api.deadlock-api.com/v1/matches/active
    """,
    deprecated=True,
)
def get_active_matches(account_id: int | None = None) -> RedirectResponse:
    url = URL("https://api.deadlock-api.com/v1/matches/active")
    if account_id:
        url.include_query_params(account_id=account_id)
    return RedirectResponse(url, HTTP_301_MOVED_PERMANENTLY)


@router.get(
    "/players/{account_id}/rank",
    response_model_exclude_none=True,
    summary="Rate Limit 10req/min, API-Key RateLimit: 20req/s",
)
def player_rank(
    req: Request,
    res: Response,
    account_id: int,
    account_groups: str = None,
) -> PlayerCard:
    limiter.apply_limits(
        req,
        res,
        "/v1/players/{account_id}/rank",
        [RateLimit(limit=10, period=60)],
        [RateLimit(limit=20, period=1)],
    )
    res.headers["Cache-Control"] = "public, max-age=60"
    account_id = utils.validate_steam_id(account_id)
    account_groups = utils.validate_account_groups(
        account_groups, req.headers.get("X-API-Key", req.query_params.get("api_key"))
    )
    return get_player_rank(account_id, account_groups)


@router.get(
    "/leaderboard/{region}",
    summary="Moved to new API: http://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: http://api.deadlock-api.com/docs
- New API Endpoint: http://api.deadlock-api.com/v1/leaderboard/{region},
    """,
    deprecated=True,
)
def leaderboard(
    region: Literal["Europe", "Asia", "NAmerica", "SAmerica", "Oceania"],
) -> RedirectResponse:
    return RedirectResponse(
        f"https://api.deadlock-api.com/v1/leaderboard/{region}", HTTP_301_MOVED_PERMANENTLY
    )


@router.get(
    "/leaderboard/{region}/{hero_id}",
    summary="Moved to new API: http://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: http://api.deadlock-api.com/docs
- New API Endpoint: http://api.deadlock-api.com/v1/leaderboard/{region}/{hero_id},
    """,
    deprecated=True,
)
def hero_leaderboard(
    region: Literal["Europe", "Asia", "NAmerica", "SAmerica", "Oceania"], hero_id: int
) -> RedirectResponse:
    return RedirectResponse(
        f"https://api.deadlock-api.com/v1/leaderboard/{region}/{hero_id}",
        HTTP_301_MOVED_PERMANENTLY,
    )


@router.get(
    "/players/{account_id}/match-history",
    response_model_exclude_none=True,
    summary="Rate Limit 60req/min, API-Key RateLimit: 100req/s, Shared Rate Limit with /v2/players/{account_id}/match-history",
    deprecated=True,
)
def player_match_history(
    req: Request, res: Response, account_id: int, account_groups: str | None = None
) -> list[PlayerMatchHistoryEntry]:
    limiter.apply_limits(
        req,
        res,
        "/players/{account_id}/match-history",
        [RateLimit(limit=60, period=60)],
        [RateLimit(limit=100, period=1)],
        [RateLimit(limit=1000, period=1)] if not account_groups else [],
    )
    res.headers["Cache-Control"] = "public, max-age=60"
    account_id = utils.validate_steam_id(account_id)
    account_groups = utils.validate_account_groups(
        account_groups, req.headers.get("X-API-Key", req.query_params.get("api_key"))
    )
    return get_player_match_history(account_id, account_groups=account_groups).matches


@router.get("/matches/{match_id}/raw_metadata", include_in_schema=False)
def get_raw_metadata_file_old(match_id: int):
    return RedirectResponse(url=f"/v1/matches/{match_id}/raw-metadata", status_code=301)


# def cache_metadata_background(match_id: int, metafile: bytes, upload_to_main: bool = False):
#     if upload_to_main:
#         try:
#             s3_main_conn().put_object(
#                 Bucket=CONFIG.s3_main.meta_file_bucket_name,
#                 Key=f"ingest/metadata/{match_id}.meta.bz2",
#                 Body=metafile,
#             )
#         except Exception:
#             LOGGER.error("Failed to upload metadata to s3")
#     try:
#         cache_file(f"{match_id}.meta.bz2", metafile)
#     except Exception as e:
#         LOGGER.error(f"Failed to cache metadata: {e}")


@router.get(
    "/matches/{match_id}/raw-metadata",
    summary="Moved to new API: http://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: http://api.deadlock-api.com/docs
- New API Endpoint: http://api.deadlock-api.com/v1/matches/{match_id}/metadata/raw,
    """,
    deprecated=True,
)
def get_raw_metadata_file(match_id: int) -> RedirectResponse:
    return RedirectResponse(
        f"https://api.deadlock-api.com/v1/matches/{match_id}/metadata/raw",
        HTTP_301_MOVED_PERMANENTLY,
    )


@router.get(
    "/matches/{match_id}/metadata",
    summary="Moved to new API: http://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: http://api.deadlock-api.com/docs
- New API Endpoint: http://api.deadlock-api.com/v1/matches/{match_id}/metadata,
    """,
    deprecated=True,
)
async def get_metadata(match_id: int) -> RedirectResponse:
    return RedirectResponse(
        f"https://api.deadlock-api.com/v1/matches/{match_id}/metadata",
        HTTP_301_MOVED_PERMANENTLY,
    )


@router.get(
    "/matches/{match_id}/demo-url",
    summary="Moved to new API: http://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: http://api.deadlock-api.com/docs
- New API Endpoint: http://api.deadlock-api.com/v1/matches/{match_id}/salts,
    """,
    deprecated=True,
)
def get_demo_url(match_id: int) -> RedirectResponse:
    url = URL(f"https://api.deadlock-api.com/v1/matches/{match_id}/salts")
    url.include_query_params(needs_demo=True)
    return RedirectResponse(url, HTTP_301_MOVED_PERMANENTLY)


@router.get(
    "/matches/{match_id}/salts",
    summary="Moved to new API: http://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: http://api.deadlock-api.com/docs
- New API Endpoint: http://api.deadlock-api.com/v1/matches/{match_id}/salts,
    """,
    deprecated=True,
)
def get_match_salts(match_id: int, needs_demo: bool = False) -> RedirectResponse:
    url = URL(f"https://api.deadlock-api.com/v1/matches/{match_id}/salts")
    if needs_demo:
        url.include_query_params(needs_demo=needs_demo)
    return RedirectResponse(url, HTTP_301_MOVED_PERMANENTLY)


@router.post("/matches/{match_id}/ingest", tags=["Webhooks"], include_in_schema=False)
def match_created_event(
    match_id: int,
    api_key: APIKey = Depends(utils.get_internal_api_key),
):
    LOGGER.debug(f"Authenticated with API-Key: {api_key}")
    payload = MatchCreatedWebhookPayload(
        match_id=match_id,
        salts_url=f"https://data.deadlock-api.com/v1/matches/{match_id}/salts",
        metadata_url=f"https://data.deadlock-api.com/v1/matches/{match_id}/metadata",
        raw_metadata_url=f"https://data.deadlock-api.com/v1/matches/{match_id}/raw-metadata",
    )
    send_webhook_event("match.metadata.created", payload.model_dump_json())
    return {"status": "success"}
