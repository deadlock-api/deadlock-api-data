from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import Response

from deadlock_data_api.models.active_match import ActiveMatch
from deadlock_data_api.models.build import Build
from deadlock_data_api.routers import v1

router = APIRouter(include_in_schema=False)


@router.get("/builds", response_model_exclude_none=True)
def get_builds(req: Request, res: Response) -> list[Build]:
    return v1.get_builds(req, res)


@router.get("/builds/{build_id}", response_model_exclude_none=True)
def get_build(req: Request, res: Response, build_id: int) -> Build:
    return v1.get_build(req, res, build_id)


@router.get("/builds/by-hero-id/{hero_id}", response_model_exclude_none=True)
def get_builds_by_hero_id(req: Request, res: Response, hero_id: int) -> list[Build]:
    return v1.get_builds_by_hero_id(req, res, hero_id)


@router.get("/active-matches", response_model_exclude_none=True)
def get_active_matches(req: Request, res: Response) -> list[ActiveMatch]:
    return v1.get_active_matches(req, res)
