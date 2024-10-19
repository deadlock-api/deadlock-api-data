import logging
import os
import sqlite3
from time import sleep
from typing import Literal

from cachetools.func import ttl_cache
from fastapi import APIRouter, HTTPException
from starlette.requests import Request
from starlette.responses import Response

from deadlock_data_api.models.active_match import ActiveMatch, APIActiveMatch
from deadlock_data_api.models.build import Build
from deadlock_data_api.rate_limiter import limiter
from deadlock_data_api.rate_limiter.models import RateLimit
from deadlock_data_api.utils import send_webhook_message

CACHE_AGE_ACTIVE_MATCHES = 20
CACHE_AGE_BUILDS = 30 * 60
LOAD_FILE_RETRIES = 5

LOGGER = logging.getLogger(__name__)

router = APIRouter(prefix="/v1")


@router.get("/builds", response_model_exclude_none=True)
def get_builds(
    req: Request,
    res: Response,
    start: int | None = None,
    limit: int | None = None,
    sort_by: Literal["favorites", "ignores", "reports", "updated_at"] | None = None,
    sort_direction: Literal["asc", "desc"] | None = None,
) -> list[Build]:
    LOGGER.info("get_builds")
    limiter.apply_limits(req, res, "/v1/builds", [RateLimit(limit=10, period=1)])
    res.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_BUILDS}"
    return load_builds(start, limit, sort_by, sort_direction)


@router.get("/builds/{build_id}", response_model_exclude_none=True)
def get_build(req: Request, res: Response, build_id: int) -> Build:
    LOGGER.info("get_build")
    limiter.apply_limits(req, res, "/v1/builds/{id}", [RateLimit(limit=100, period=1)])
    res.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_BUILDS}"
    return load_build(build_id)


@router.get("/builds/by-hero-id/{hero_id}", response_model_exclude_none=True)
def get_builds_by_hero_id(
    req: Request,
    res: Response,
    hero_id: int,
    start: int | None = None,
    limit: int | None = None,
    sort_by: Literal["favorites", "ignores", "reports", "updated_at"] | None = None,
    sort_direction: Literal["asc", "desc"] | None = None,
) -> list[Build]:
    LOGGER.info("get_builds_by_hero_id")
    limiter.apply_limits(
        req, res, "/v1/builds/by-hero-id/{hero_id}", [RateLimit(limit=100, period=1)]
    )
    res.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_BUILDS}"
    return load_builds_by_hero(hero_id, start, limit, sort_by, sort_direction)


@router.get("/builds/by-author-id/{author_id}", response_model_exclude_none=True)
def get_builds_by_author_id(
    req: Request,
    res: Response,
    author_id: int,
    start: int | None = None,
    limit: int | None = None,
    sort_by: Literal["favorites", "ignores", "reports", "updated_at"] | None = None,
    sort_direction: Literal["asc", "desc"] | None = None,
) -> list[Build]:
    LOGGER.info("get_builds_by_author_id")
    limiter.apply_limits(
        req,
        res,
        "/v1/builds/by-author-id/{author_id}",
        [RateLimit(limit=100, period=1)],
    )
    res.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_BUILDS}"
    return load_builds_by_author(author_id, start, limit, sort_by, sort_direction)


@router.get(
    "/active-matches",
    response_model_exclude_none=True,
    summary="Updates every 20s | Rate Limit 15req/20s",
)
def get_active_matches(req: Request, res: Response) -> list[ActiveMatch]:
    LOGGER.info("get_active_matches")
    limiter.apply_limits(
        req, res, "/v1/active-matches", [RateLimit(limit=15, period=20)]
    )
    last_modified = os.path.getmtime("active_matches.json")
    res.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_ACTIVE_MATCHES}"
    res.headers["Last-Updated"] = str(int(last_modified))
    return load_active_matches()


@ttl_cache(ttl=CACHE_AGE_BUILDS - 1)
def load_builds(
    start: int | None = None,
    limit: int | None = None,
    sort_by: Literal["favorites", "ignores", "reports", "updated_at"] | None = None,
    sort_direction: Literal["asc", "desc"] | None = None,
) -> list[Build]:
    LOGGER.debug("load_builds")
    query = "SELECT json(data) as builds FROM hero_builds"
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
            raise HTTPException(
                status_code=400, detail="Start cannot be provided without limit"
            )
        query += " LIMIT ? OFFSET ?"
        args += [limit, start]

    conn = sqlite3.connect("builds.db")
    cursor = conn.cursor()
    cursor.execute(query, tuple(args))
    results = cursor.fetchall()
    return [Build.model_validate_json(result[0]) for result in results]


@ttl_cache(ttl=CACHE_AGE_BUILDS - 1)
def load_builds_by_hero(
    hero_id: int,
    start: int | None = None,
    limit: int | None = None,
    sort_by: Literal["favorites", "ignores", "reports", "updated_at"] | None = None,
    sort_direction: Literal["asc", "desc"] | None = None,
) -> list[Build]:
    LOGGER.debug("load_builds_by_hero")
    query = "SELECT json(data) as builds FROM hero_builds WHERE hero = ?"
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
            raise HTTPException(
                status_code=400, detail="Start cannot be provided without limit"
            )
        query += " LIMIT ? OFFSET ?"
        args += [limit, start]

    conn = sqlite3.connect("builds.db")
    cursor = conn.cursor()
    cursor.execute(query, tuple(args))
    results = cursor.fetchall()
    return [Build.model_validate_json(result[0]) for result in results]


@ttl_cache(ttl=CACHE_AGE_BUILDS - 1)
def load_builds_by_author(
    author_id: int,
    start: int | None = None,
    limit: int | None = None,
    sort_by: Literal["favorites", "ignores", "reports", "updated_at"] | None = None,
    sort_direction: Literal["asc", "desc"] | None = None,
) -> list[Build]:
    LOGGER.debug("load_builds_by_author")
    query = "SELECT json(data) as builds FROM hero_builds WHERE author_id = ?"
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
            raise HTTPException(
                status_code=400, detail="Start cannot be provided without limit"
            )
        query += " LIMIT ? OFFSET ?"
        args += [limit, start]

    conn = sqlite3.connect("builds.db")
    cursor = conn.cursor()
    cursor.execute(query, tuple(args))
    results = cursor.fetchall()
    return [Build.model_validate_json(result[0]) for result in results]


@ttl_cache(ttl=CACHE_AGE_BUILDS - 1)
def load_build(build_id: int) -> Build:
    LOGGER.debug("load_build")
    conn = sqlite3.connect("builds.db")
    cursor = conn.cursor()
    query = "SELECT json(data) FROM hero_builds WHERE build_id = ?"
    cursor.execute(query, (build_id,))
    result = cursor.fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="Build not found")
    return Build.model_validate_json(result[0])


@ttl_cache(ttl=CACHE_AGE_ACTIVE_MATCHES - 1)
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
