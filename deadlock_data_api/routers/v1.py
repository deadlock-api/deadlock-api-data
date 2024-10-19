import os
import sqlite3
from time import sleep

from cachetools.func import ttl_cache
from fastapi import APIRouter, HTTPException
from starlette.responses import Response

from deadlock_data_api.models.active_match import ActiveMatch, APIActiveMatch
from deadlock_data_api.models.build import Build
from deadlock_data_api.utils import send_webhook_message

CACHE_AGE_ACTIVE_MATCHES = 20
CACHE_AGE_BUILDS = 30 * 60
LOAD_FILE_RETRIES = 5

router = APIRouter(prefix="/v1")


@router.get("/builds", response_model_exclude_none=True)
def get_builds(
    response: Response, start: int | None = None, limit: int | None = None
) -> list[Build]:
    response.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_BUILDS}"
    return load_builds(start, limit)


@router.get("/builds/{build_id}", response_model_exclude_none=True)
def get_build(response: Response, build_id: int) -> Build:
    response.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_BUILDS}"
    return load_build(build_id)


@router.get("/builds/by-hero-id/{hero_id}", response_model_exclude_none=True)
def get_builds_by_hero_id(
    response: Response, hero_id: int, start: int | None = None, limit: int | None = None
) -> list[Build]:
    response.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_BUILDS}"
    return load_builds_by_hero(hero_id, start, limit)


@router.get("/builds/by-hero-id/{hero_id}", response_model_exclude_none=True)
def get_builds_by_author_id(
    response: Response,
    author_id: int,
    start: int | None = None,
    limit: int | None = None,
) -> list[Build]:
    response.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_BUILDS}"
    return load_builds_by_author(author_id, start, limit)


@ttl_cache(ttl=CACHE_AGE_BUILDS - 1)
def load_builds(start: int | None = None, limit: int | None = None) -> list[Build]:
    if limit is not None or start is not None:
        if start is None:
            raise HTTPException(
                status_code=400, detail="Limit cannot be provided without start"
            )
        if limit is None:
            raise HTTPException(
                status_code=400, detail="Start cannot be provided without limit"
            )
        query = "SELECT json(data) as builds FROM hero_builds LIMIT ? OFFSET ?"
        args = (limit, start)
    else:
        query = "SELECT json(data) as builds FROM hero_builds"
        args = ()

    conn = sqlite3.connect("builds.db")
    cursor = conn.cursor()
    cursor.execute(query, args)
    results = cursor.fetchall()
    return [Build.model_validate_json(result[0]) for result in results]


@ttl_cache(ttl=CACHE_AGE_BUILDS - 1)
def load_builds_by_hero(
    hero_id: int, start: int | None = None, limit: int | None = None
) -> list[Build]:
    if limit is not None or start is not None:
        if start is None:
            raise HTTPException(
                status_code=400, detail="Limit cannot be provided without start"
            )
        if limit is None:
            raise HTTPException(
                status_code=400, detail="Start cannot be provided without limit"
            )
        query = "SELECT json(data) as builds FROM hero_builds WHERE hero = ? LIMIT ? OFFSET ?"
        args = (hero_id, limit, start)
    else:
        query = "SELECT json(data) as builds FROM hero_builds WHERE hero = ?"
        args = (hero_id,)

    conn = sqlite3.connect("builds.db")
    cursor = conn.cursor()
    cursor.execute(query, args)
    results = cursor.fetchall()
    return [Build.model_validate_json(result[0]) for result in results]


@ttl_cache(ttl=CACHE_AGE_BUILDS - 1)
def load_builds_by_author(
    author_id: int, start: int | None = None, limit: int | None = None
) -> list[Build]:
    if limit is not None or start is not None:
        if start is None:
            raise HTTPException(
                status_code=400, detail="Limit cannot be provided without start"
            )
        if limit is None:
            raise HTTPException(
                status_code=400, detail="Start cannot be provided without limit"
            )
        query = "SELECT json(data) as builds FROM hero_builds WHERE author_id = ? LIMIT ? OFFSET ?"
        args = (author_id, limit, start)
    else:
        query = "SELECT json(data) as builds FROM hero_builds WHERE author_id = ?"
        args = (author_id,)

    conn = sqlite3.connect("builds.db")
    cursor = conn.cursor()
    cursor.execute(query, args)
    results = cursor.fetchall()
    return [Build.model_validate_json(result[0]) for result in results]


@ttl_cache(ttl=CACHE_AGE_BUILDS - 1)
def load_build(build_id: int) -> Build:
    conn = sqlite3.connect("builds.db")
    cursor = conn.cursor()
    query = "SELECT json(data) FROM hero_builds WHERE build_id = ?"
    cursor.execute(query, (build_id,))
    result = cursor.fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="Build not found")
    return Build.model_validate_json(result[0])


@router.get(
    "/active-matches",
    response_model_exclude_none=True,
    summary="Updates every 20s | Rate Limit 15req/20s",
)
def get_active_matches(response: Response) -> list[ActiveMatch]:
    last_modified = os.path.getmtime("active_matches.json")
    response.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_ACTIVE_MATCHES}"
    response.headers["Last-Updated"] = str(int(last_modified))
    return load_active_matches()


@ttl_cache(ttl=CACHE_AGE_ACTIVE_MATCHES - 1)
def load_active_matches() -> list[ActiveMatch]:
    last_exc = None
    for i in range(LOAD_FILE_RETRIES):
        try:
            with open("active_matches.json") as f:
                return APIActiveMatch.model_validate_json(f.read()).active_matches
        except Exception as e:
            last_exc = e
            print(
                f"Error loading active matches: {str(e)}, retry ({i + 1}/{LOAD_FILE_RETRIES})"
            )
        sleep(50)
    send_webhook_message(f"Error loading active matches: {str(last_exc)}")
    raise HTTPException(status_code=500, detail="Failed to load active matches")
