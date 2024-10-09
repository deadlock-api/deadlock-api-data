from fastapi import APIRouter
from starlette.responses import Response

from deadlock_data_api.models.active_match import ActiveMatch
from deadlock_data_api.models.build import Build
from deadlock_data_api.routers import v1

router = APIRouter()


@router.get("/builds")
def get_builds(response: Response) -> dict[str, list[Build]]:
    return v1.get_builds(response)


@router.get("/builds/{build_id}")
def get_build(response: Response, build_id: int) -> Build:
    return v1.get_build(response, build_id)


@router.get("/builds/by-hero-id/{hero_id}")
def get_builds_by_hero_id(response: Response, hero_id: int) -> list[Build]:
    return v1.get_builds_by_hero_id(response, hero_id)


@router.get("/builds/by-hero-name/{hero_name}")
def get_builds_by_hero_name(response: Response, hero_name: str) -> list[Build]:
    return v1.get_builds_by_hero_name(response, hero_name)


@router.get("/active-matches", response_model_exclude_none=True)
def get_active_matches(response: Response) -> list[ActiveMatch]:
    return v1.get_active_matches(response)
