import bz2
import logging
from datetime import datetime, timedelta
from typing import Literal

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from fastapi.openapi.models import APIKey
from google.protobuf.json_format import MessageToDict
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse, RedirectResponse, Response
from valveprotos_py.citadel_gcmessages_client_pb2 import (
    CMsgClientToGCGetActiveMatchesResponse,
)
from valveprotos_py.citadel_gcmessages_common_pb2 import (
    CMsgMatchMetaData,
    CMsgMatchMetaDataContents,
)

from deadlock_data_api import utils
from deadlock_data_api.conf import CONFIG
from deadlock_data_api.globs import s3_main_conn
from deadlock_data_api.models.active_match import ActiveMatch
from deadlock_data_api.models.build import Build
from deadlock_data_api.models.leaderboard import Leaderboard
from deadlock_data_api.models.player_card import PlayerCard
from deadlock_data_api.models.player_match_history import (
    PlayerMatchHistoryEntry,
)
from deadlock_data_api.models.webhook import MatchCreatedWebhookPayload
from deadlock_data_api.rate_limiter import limiter
from deadlock_data_api.rate_limiter.models import RateLimit
from deadlock_data_api.routers.v1_utils import (
    fetch_active_matches_raw,
    fetch_metadata,
    fetch_patch_notes,
    get_leaderboard,
    get_match_salts_from_db,
    get_match_salts_from_steam,
    get_match_start_time,
    get_player_match_history,
    get_player_rank,
    load_build,
    load_build_version,
    load_builds,
    load_builds_by_author,
    load_builds_by_hero,
)
from deadlock_data_api.utils import cache_file, get_cached_file, send_webhook_event

CACHE_AGE_ACTIVE_MATCHES = 20
CACHE_AGE_BUILDS = 5 * 60

LOGGER = logging.getLogger(__name__)

router = APIRouter(prefix="/v1", tags=["V1"])


@router.get("/patch-notes", summary="No Rate Limits")
def get_patch_notes(res: Response):
    res.headers["Cache-Control"] = f"public, max-age={30 * 60}"
    return fetch_patch_notes()


@router.get(
    "/big-patch-days",
    description="""
            Returns a list of dates where Deadlock's "big" patch days were, usually bi-weekly.
            The exact date is the time when the announcement forum post was published.

            This list is manually maintained, and so new patch dates may be delayed by a few hours.
            """,
    summary="No Rate Limits",
)
def get_big_patch_days(res: Response) -> list[datetime]:
    res.headers["Cache-Control"] = f"public, max-age={30 * 60}"
    date_string_list = [
        "2025-01-28T02:10:06Z",
        "2025-01-17T18:40:54Z",
        "2024-12-06T20:05:10Z",
        "2024-11-21T23:21:49Z",
        "2024-11-07T21:31:34Z",
        "2024-10-24T19:39:08Z",
        "2024-10-10T20:24:45Z",
        "2024-09-26T21:17:58Z",
    ]

    return [datetime.fromisoformat(date_string) for date_string in date_string_list]


@router.get("/builds", response_model_exclude_none=True, summary="Rate Limit 100req/s")
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
    language: int | None = None,
) -> list[Build]:
    only_latest = only_latest or False
    limiter.apply_limits(req, res, "/v1/builds", [RateLimit(limit=100, period=1)])
    res.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_BUILDS}"
    return load_builds(
        start,
        limit,
        sort_by,
        sort_direction,
        search_name,
        search_description,
        only_latest,
        language,
    )


@router.get(
    "/builds/{build_id}",
    response_model_exclude_none=True,
    summary="Rate Limit 100req/s",
)
def get_build(req: Request, res: Response, build_id: int, version: int | None = None) -> Build:
    limiter.apply_limits(req, res, "/v1/builds/{id}", [RateLimit(limit=100, period=1)])
    res.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_BUILDS}"
    return load_build(build_id) if version is None else load_build_version(build_id, version)


@router.get(
    "/builds/by-hero-id/{hero_id}",
    response_model_exclude_none=True,
    summary="Rate Limit 100req/s",
)
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
    language: int | None = None,
) -> list[Build]:
    only_latest = only_latest or False
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
        language,
    )


@router.get(
    "/builds/by-author-id/{author_id}",
    response_model_exclude_none=True,
    summary="Rate Limit 100req/s",
)
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
    limiter.apply_limits(
        req,
        res,
        "/v1/builds/by-author-id/{author_id}",
        [RateLimit(limit=100, period=1)],
    )
    res.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_BUILDS}"
    return load_builds_by_author(author_id, start, limit, sort_by, sort_direction, only_latest)


@router.get(
    "/raw-active-matches",
    response_model_exclude_none=True,
    summary="Updates every 20s | Rate Limit 100req/s, Shared Rate Limit with /active-matches",
)
def get_active_matches_raw(
    req: Request, res: Response, account_groups: str | None = None
) -> Response:
    limiter.apply_limits(req, res, "/v1/active-matches", [RateLimit(limit=100, period=1)])
    account_groups = utils.validate_account_groups(
        account_groups, req.headers.get("X-API-Key", req.query_params.get("api_key"))
    )
    return Response(
        content=fetch_active_matches_raw(account_groups),
        media_type="application/octet-stream",
        headers={"Cache-Control": f"public, max-age={CACHE_AGE_ACTIVE_MATCHES}"},
    )


@router.get(
    "/active-matches",
    response_model_exclude_none=True,
    summary="Updates every 20s | Rate Limit 100req/s, Shared Rate Limit with /raw-active-matches",
)
def get_active_matches(
    req: Request, res: Response, account_id: int | None = None, account_groups: str | None = None
) -> list[ActiveMatch]:
    limiter.apply_limits(req, res, "/v1/active-matches", [RateLimit(limit=100, period=1)])
    res.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_ACTIVE_MATCHES}"

    account_id = utils.validate_steam_id_optional(account_id)
    account_groups = utils.validate_account_groups(
        account_groups, req.headers.get("X-API-Key", req.query_params.get("api_key"))
    )

    raw_active_matches = fetch_active_matches_raw(account_groups)
    msg = CMsgClientToGCGetActiveMatchesResponse.FromString(raw_active_matches)

    return [
        ActiveMatch.from_msg(am)
        for am in msg.active_matches
        if account_id is None or any(p.account_id == account_id for p in am.players)
    ]


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
    res.headers["Cache-Control"] = "public, max-age=900"
    account_id = utils.validate_steam_id(account_id)
    account_groups = utils.validate_account_groups(
        account_groups, req.headers.get("X-API-Key", req.query_params.get("api_key"))
    )
    return get_player_rank(account_id, account_groups)


@router.get(
    "/leaderboard/{region}",
    response_model_exclude_none=True,
    summary="Rate Limit 100req/s",
)
def leaderboard(
    req: Request,
    res: Response,
    region: Literal["Europe", "Asia", "NAmerica", "SAmerica", "Oceania"],
    account_groups: str = None,
) -> Leaderboard:
    limiter.apply_limits(
        req,
        res,
        "/v1/leaderboard/{region}",
        [RateLimit(limit=100, period=1)],
    )
    res.headers["Cache-Control"] = "public, max-age=900"
    account_groups = utils.validate_account_groups(
        account_groups, req.headers.get("X-API-Key", req.query_params.get("api_key"))
    )
    return get_leaderboard(region, None, account_groups)


@router.get(
    "/leaderboard/{region}/{hero_id}",
    response_model_exclude_none=True,
    summary="Rate Limit 100req/s",
)
def hero_leaderboard(
    req: Request,
    res: Response,
    region: Literal["Europe", "Asia", "NAmerica", "SAmerica", "Oceania"],
    hero_id: int,
    account_groups: str = None,
) -> Leaderboard:
    limiter.apply_limits(
        req,
        res,
        "/v1/leaderboard/{region}/{hero_id}",
        [RateLimit(limit=100, period=1)],
    )
    res.headers["Cache-Control"] = "public, max-age=900"
    account_groups = utils.validate_account_groups(
        account_groups, req.headers.get("X-API-Key", req.query_params.get("api_key"))
    )
    return get_leaderboard(region, hero_id, account_groups)


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
        [RateLimit(limit=1000, period=1)],
    )
    res.headers["Cache-Control"] = "public, max-age=900"
    account_id = utils.validate_steam_id(account_id)
    account_groups = utils.validate_account_groups(
        account_groups, req.headers.get("X-API-Key", req.query_params.get("api_key"))
    )
    return get_player_match_history(account_id, account_groups=account_groups).matches


@router.get("/matches/{match_id}/raw_metadata", include_in_schema=False)
def get_raw_metadata_file_old(match_id: int):
    return RedirectResponse(url=f"/v1/matches/{match_id}/raw-metadata", status_code=301)


def cache_metadata_background(match_id: int, metafile: bytes, upload_to_main: bool = False):
    if upload_to_main:
        try:
            s3_main_conn().put_object(
                Bucket=CONFIG.s3_main.meta_file_bucket_name,
                Key=f"ingest/metadata/{match_id}.meta.bz2",
                Body=metafile,
            )
        except Exception:
            LOGGER.error("Failed to upload metadata to s3")
    try:
        cache_file(f"{match_id}.meta.bz2", metafile)
    except Exception as e:
        LOGGER.error(f"Failed to cache metadata: {e}")


@router.get(
    "/matches/{match_id}/raw-metadata",
    description="""
# Raw Metadata

This endpoints streams the raw .meta.bz2 file for the given `match_id`.

You have to decompress it and decode the protobuf message.

Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

Relevant Protobuf Messages: CMsgMatchMetaData, CMsgMatchMetaDataContents
    """,
    summary="RateLimit: 10req/min & 100req/h, API-Key RateLimit: 100req/s, for Steam Calls: Global 30req/h, Shared Rate Limit with /metadata",
)
def get_raw_metadata_file(
    req: Request,
    res: Response,
    background_tasks: BackgroundTasks,
    match_id: int,
    account_groups: str | None = None,
) -> Response:
    limiter.apply_limits(
        req,
        res,
        "/v1/matches/{match_id}/metadata",
        [RateLimit(limit=10, period=60), RateLimit(limit=100, period=3600)],
        [RateLimit(limit=100, period=1)],
    )
    account_groups = utils.validate_account_groups(
        account_groups, req.headers.get("X-API-Key", req.query_params.get("api_key"))
    )
    try:
        meta = get_cached_file(f"{match_id}.meta.bz2")
        if meta is None:
            meta = get_cached_file(f"{match_id}.meta_hltv.bz2")
        if meta is not None:
            return Response(
                content=meta,
                media_type="application/octet-stream",
                headers={
                    "Content-Disposition": f"attachment; filename={match_id}.meta.bz2",
                    "Cache-Control": "public, max-age=1200",
                },
            )
    except Exception as e:
        LOGGER.warning(f"Failed to get metadata from cache: {e}")

    possible_keys = [
        f"processed/metadata/{match_id}.meta.bz2",
        f"processed/metadata/{match_id}.meta_hltv.bz2",
    ]
    key = None
    for test_key in possible_keys:
        try:
            s3_main_conn().head_object(Bucket=CONFIG.s3_main.meta_file_bucket_name, Key=test_key)
            key = test_key
        except Exception:
            pass
    if key is not None:
        obj = s3_main_conn().get_object(Bucket=CONFIG.s3_main.meta_file_bucket_name, Key=key)
        body = obj["Body"].read()
        background_tasks.add_task(cache_metadata_background, match_id, body)
        return Response(
            content=body,
            media_type="application/octet-stream",
            headers={
                "Content-Disposition": f"attachment; filename={match_id}.meta.bz2",
                "Cache-Control": "public, max-age=1200",
            },
        )
    salts = get_match_salts_from_db(match_id)
    if salts is None:
        limiter.apply_limits(
            req,
            res,
            "/v1/matches/{match_id}/#steam",
            [RateLimit(limit=30, period=3600)],
            [RateLimit(limit=30, period=3600)],
            [RateLimit(limit=30, period=3600)],
        )
        salts = get_match_salts_from_steam(match_id, account_groups=account_groups)
    metafile = fetch_metadata(match_id, salts)
    background_tasks.add_task(cache_metadata_background, match_id, metafile, True)
    return Response(
        content=metafile,
        media_type="application/octet-stream",
        headers={
            "Content-Disposition": f"attachment; filename={match_id}.meta.bz2",
            "Cache-Control": "public, max-age=1200",
        },
    )


@router.get(
    "/matches/{match_id}/metadata",
    summary="RateLimit: 10req/min & 100req/h, API-Key RateLimit: 100req/s, for Steam Calls: Global 30req/h, Shared Rate Limit with /raw-metadata",
)
async def get_metadata(
    req: Request,
    res: Response,
    background_tasks: BackgroundTasks,
    match_id: int,
    account_groups: str | None = None,
) -> JSONResponse:
    account_groups = utils.validate_account_groups(
        account_groups, req.headers.get("X-API-Key", req.query_params.get("api_key"))
    )
    raw_metadata = get_raw_metadata_file(req, res, background_tasks, match_id, account_groups).body
    raw_metadata_decompressed = bz2.decompress(raw_metadata)
    metadata = CMsgMatchMetaData.FromString(raw_metadata_decompressed)
    match_contents = CMsgMatchMetaDataContents.FromString(metadata.match_details)
    return JSONResponse(MessageToDict(match_contents, preserving_proto_field_name=True))


@router.get(
    "/matches/{match_id}/demo-url",
    summary="RateLimit: 10req/min & 100req/h, API-Key RateLimit: 100req/s, for Steam Calls: Global 30req/h",
    deprecated=True,
)
def get_demo_url(match_id: int) -> RedirectResponse:
    return RedirectResponse(url=f"/v1/matches/{match_id}/salts?needs_demo=true", status_code=308)


class DataUrlsResponse(BaseModel):
    match_id: int
    cluster_id: int
    metadata_salt: int
    replay_salt: int
    metadata_url: str
    demo_url: str


@router.get(
    "/matches/{match_id}/salts",
    summary="RateLimit: 10req/min & 100req/h, API-Key RateLimit: 100req/s, for Steam Calls: Global 30req/h",
)
def get_match_salts(
    req: Request,
    res: Response,
    match_id: int,
    needs_demo: bool = False,
    account_groups: str | None = None,
) -> DataUrlsResponse:
    limiter.apply_limits(
        req,
        res,
        "/v1/matches/{match_id}/salts",
        [RateLimit(limit=10, period=60), RateLimit(limit=100, period=3600)],
        [RateLimit(limit=100, period=1)],
    )
    account_groups = utils.validate_account_groups(
        account_groups, req.headers.get("X-API-Key", req.query_params.get("api_key"))
    )
    salts = get_match_salts_from_db(match_id, needs_demo)
    if salts is None:
        match_start_time = get_match_start_time(match_id)
        if (
            needs_demo
            and match_start_time is not None
            and datetime.now() - match_start_time > timedelta(days=CONFIG.demo_retention_days)
        ):
            raise HTTPException(status_code=400, detail="Match is too old")
        limiter.apply_limits(
            req,
            res,
            "/v1/matches/{match_id}/#steam",
            [RateLimit(limit=30, period=3600)],
            [RateLimit(limit=30, period=3600)],
            [RateLimit(limit=30, period=3600)],
        )
        salts = get_match_salts_from_steam(match_id, True, account_groups)
    metadata_url = f"http://replay{salts.cluster_id}.valve.net/1422450/{match_id}_{salts.metadata_salt}.meta.bz2"
    demo_url = (
        f"http://replay{salts.cluster_id}.valve.net/1422450/{match_id}_{salts.replay_salt}.dem.bz2"
    )
    return DataUrlsResponse(
        match_id=match_id,
        cluster_id=salts.cluster_id,
        metadata_salt=salts.metadata_salt,
        replay_salt=salts.replay_salt,
        metadata_url=metadata_url,
        demo_url=demo_url,
    )


@router.post("/matches/{match_id}/ingest", tags=["Webhooks"], include_in_schema=False)
def match_created_event(
    match_id: int,
    api_key: APIKey = Depends(utils.get_internal_api_key),
):
    print(f"Authenticated with API-Key: {api_key}")
    payload = MatchCreatedWebhookPayload(
        match_id=match_id,
        salts_url=f"https://data.deadlock-api.com/v1/matches/{match_id}/salts",
        metadata_url=f"https://data.deadlock-api.com/v1/matches/{match_id}/metadata",
        raw_metadata_url=f"https://data.deadlock-api.com/v1/matches/{match_id}/raw-metadata",
    )
    send_webhook_event("match.metadata.created", payload.model_dump_json())
    return {"status": "success"}
