import requests
from fastapi import APIRouter

router = APIRouter(prefix="/v2", tags=["V2"])


@router.get(
    "/players/{account_id}/match-history",
    summary="Moved to new API: http://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: http://api.deadlock-api.com/docs
- New API Endpoint: https://api.deadlock-api.com/v1/players/{account_id}/match-history
    """,
    deprecated=True,
)
def player_match_history(account_id: int) -> dict:
    data = requests.get(
        f"https://api.deadlock-api.com/v1/players/{account_id}/match-history"
    ).json()
    return {"cursor": 0, "matches": data}
