import os
import sqlite3
from time import sleep

from cachetools.func import ttl_cache
from fastapi import APIRouter, HTTPException
from pydantic import TypeAdapter
from starlette.responses import Response

from deadlock_data_api.models.active_match import ActiveMatch, APIActiveMatch
from deadlock_data_api.models.build import Build
from deadlock_data_api.utils import send_webhook_message

CACHE_AGE_ACTIVE_MATCHES = 20
CACHE_AGE_BUILDS = 30 * 60
LOAD_FILE_RETRIES = 5

router = APIRouter(prefix="/v1")


@router.get("/builds", response_model_exclude_none=True)
def get_builds(response: Response) -> dict[int, list[Build]]:
    response.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_BUILDS}"
    return load_builds()


@router.get("/builds/{build_id}", response_model_exclude_none=True)
def get_build(response: Response, build_id: int) -> Build:
    response.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_BUILDS}"
    return load_build(build_id)


@router.get("/builds/by-hero-id/{hero_id}", response_model_exclude_none=True)
def get_builds_by_hero_id(response: Response, hero_id: int) -> list[Build]:
    response.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_BUILDS}"
    return load_builds_by_hero(hero_id)


@ttl_cache(ttl=CACHE_AGE_BUILDS - 1)
def load_builds() -> dict[int, list[Build]]:
    conn = sqlite3.connect("builds.db")
    cursor = conn.cursor()
    query = "SELECT hero, json_group_array(json(data)) as builds FROM hero_builds GROUP BY hero"
    cursor.execute(query)
    result = cursor.fetchall()
    ta = TypeAdapter(list[Build])
    return {hero: ta.validate_json(data) for hero, data in result}


@ttl_cache(ttl=CACHE_AGE_BUILDS - 1)
def load_builds_by_hero(hero_id: int) -> list[Build]:
    conn = sqlite3.connect("builds.db")
    cursor = conn.cursor()
    query = "SELECT json(data) as builds FROM hero_builds WHERE hero = ?"
    cursor.execute(query, (hero_id,))
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
