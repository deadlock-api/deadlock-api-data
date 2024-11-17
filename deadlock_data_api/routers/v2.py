from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import Response

from deadlock_data_api import utils
from deadlock_data_api.models.player_match_history import PlayerMatchHistory
from deadlock_data_api.rate_limiter import limiter
from deadlock_data_api.rate_limiter.models import RateLimit
from deadlock_data_api.routers.v1_utils import (
    get_player_match_history,
)

router = APIRouter(prefix="/v2", tags=["V2"])


@router.get(
    "/players/{account_id}/match-history",
    response_model_exclude_none=True,
    summary="Rate Limit 60req/min, API-Key RateLimit: 20req/s",
)
def player_match_history(
    req: Request,
    res: Response,
    account_id: int,
    continue_cursor: int | None = None,
) -> PlayerMatchHistory:
    limiter.apply_limits(
        req,
        res,
        "/v2/players/{account_id}/match-history",
        [RateLimit(limit=60, period=60)],
        [RateLimit(limit=20, period=1)],
    )
    res.headers["Cache-Control"] = "public, max-age=900"
    account_id = utils.validate_steam_id(account_id)
    return get_player_match_history(account_id, continue_cursor)
