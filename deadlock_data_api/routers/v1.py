import os
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
def get_builds(response: Response) -> dict[str, list[Build]]:
    last_modified = os.path.getmtime("builds.json")
    response.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_BUILDS}"
    response.headers["Last-Updated"] = str(int(last_modified))
    return load_builds()


@router.get("/builds/{build_id}", response_model_exclude_none=True)
def get_build(response: Response, build_id: int) -> Build:
    builds = get_builds(response)
    build = next(
        (
            b
            for bs in builds.values()
            for b in bs
            if b.hero_build.hero_build_id == build_id
        ),
        None,
    )
    if build is None:
        raise HTTPException(status_code=404, detail="Build not found")
    return build


@router.get("/builds/by-hero-id/{hero_id}", response_model_exclude_none=True)
def get_builds_by_hero_id(response: Response, hero_id: int) -> list[Build]:
    builds = get_builds(response)
    filtered = {
        k: [h for h in v if h.hero_build.hero_id == hero_id] for k, v in builds.items()
    }
    filtered = {k: v for k, v in filtered.items() if len(v) > 0}
    if len(filtered) == 0:
        raise HTTPException(status_code=404, detail="Hero not found")
    return next(v for k, v in filtered.items())


@router.get("/builds/by-hero-name/{hero_name}", response_model_exclude_none=True)
def get_builds_by_hero_name(response: Response, hero_name: str) -> list[Build]:
    builds = get_builds(response)
    filtered = next(
        (v for k, v in builds.items() if k.lower() == hero_name.lower()),
        None,
    )
    if filtered is None:
        raise HTTPException(status_code=404, detail="Hero not found")
    return filtered


@router.get(
    "/active-matches",
    response_model_exclude_none=True,
    summary="Updates every 20s | Rate Limit 10req/20s",
)
def get_active_matches(response: Response) -> list[ActiveMatch]:
    last_modified = os.path.getmtime("active_matches.json")
    response.headers["Cache-Control"] = f"public, max-age={CACHE_AGE_ACTIVE_MATCHES}"
    response.headers["Last-Updated"] = str(int(last_modified))
    return load_active_matches()


@ttl_cache(ttl=CACHE_AGE_BUILDS - 1)
def load_builds() -> dict[str, list[Build]]:
    ta = TypeAdapter(dict[str, list[Build]])
    last_exc = None
    for i in range(LOAD_FILE_RETRIES):
        try:
            with open("builds.json") as f:
                return ta.validate_json(f.read())
        except Exception as e:
            last_exc = e
            print(
                f"Error loading builds: {str(e)}, retry ({i + 1}/{LOAD_FILE_RETRIES})"
            )
        sleep(50)
    send_webhook_message(f"Error loading builds: {str(last_exc)}")
    raise HTTPException(status_code=500, detail="Failed to load builds")


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
