from fastapi import APIRouter
from starlette.responses import RedirectResponse
from starlette.status import HTTP_301_MOVED_PERMANENTLY

router = APIRouter(prefix="/v2", tags=["V2"])


@router.get(
    "/players/{account_id}/match-history",
    summary="Moved to new API: https://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: https://api.deadlock-api.com/docs
- New API Endpoint: https://api.deadlock-api.com/v1/players/{account_id}/match-history
    """,
    deprecated=True,
)
def player_match_history(account_id: int) -> RedirectResponse:
    return RedirectResponse(
        f"https://api.deadlock-api.com/v2/players/{account_id}/match-history",
        HTTP_301_MOVED_PERMANENTLY,
    )
