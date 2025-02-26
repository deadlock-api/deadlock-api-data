import logging

from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import RedirectResponse, Response

from deadlock_data_api.routers import v1

LOGGER = logging.getLogger(__name__)

router = APIRouter(include_in_schema=False)


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
def get_builds(req: Request) -> RedirectResponse:
    return v1.get_builds(req)


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
def get_build(build_id: int, version: int) -> RedirectResponse:
    return v1.get_build(build_id, version)


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
def get_builds_by_hero_id(req: Request, hero_id: int) -> RedirectResponse:
    return v1.get_builds_by_hero_id(req, hero_id)


@router.get("/active-matches", response_model_exclude_none=True)
def get_active_matches(req: Request, res: Response) -> RedirectResponse:
    return v1.get_active_matches(req, res)
