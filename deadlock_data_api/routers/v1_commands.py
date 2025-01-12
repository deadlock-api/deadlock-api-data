from datetime import datetime, timedelta
from time import sleep
from typing import Annotated, Literal

import requests
from fastapi.params import Query
from starlette.responses import PlainTextResponse, Response

from deadlock_data_api import utils
from deadlock_data_api.routers import v2
from deadlock_data_api.routers.v1 import LOGGER, router
from deadlock_data_api.routers.v1_utils import get_leaderboard


@router.get(
    "/commands/leaderboard-rank/{region}/{account_name}",
    summary="Rate Limit 100req/s | Sync with /v1/leaderboard/{region}",
    response_class=PlainTextResponse,
)
def get_leaderboard_rank_command(
    res: Response,
    region: Literal["Europe", "Asia", "NAmerica", "SAmerica", "Oceania"],
    account_name: str,
):
    res.headers["Cache-Control"] = "public, max-age=60"
    for retry in range(3):
        try:
            ranks = requests.get("https://assets.deadlock-api.com/v2/ranks").json()
            leaderboard = get_leaderboard(region, None, None)
        except Exception as e:
            LOGGER.error(f"Failed to get leaderboard: {e}")
            sleep(0.1)
            if retry == 2:
                return "Failed to get leaderboard"
    for entry in leaderboard.entries:
        if entry.account_name == account_name:
            rank = entry.ranked_rank
            rank_name = next((r["name"] for r in ranks if r["tier"] == rank), None)
            if rank_name is None:
                return f"Failed to get rank name for {rank}"
            return f"{entry.account_name} is {rank_name} {entry.ranked_subrank} | #{entry.rank}"
    return "Player not found in leaderboard"


@router.get(
    "/commands/leaderboard-rank/{region}/{account_name}/{hero_id}",
    summary="Rate Limit 100req/s | Sync with /v1/leaderboard/{region}/{hero_id}",
    response_class=PlainTextResponse,
)
def get_hero_leaderboard_rank_command(
    res: Response,
    region: Literal["Europe", "Asia", "NAmerica", "SAmerica", "Oceania"],
    account_name: str,
    hero_id: int,
):
    res.headers["Cache-Control"] = "public, max-age=60"
    for retry in range(3):
        try:
            hero_name = (
                requests.get(f"https://assets.deadlock-api.com/v2/heroes/{hero_id}")
                .json()
                .get("name")
            )
            leaderboard = get_leaderboard(region, hero_id, None)
        except Exception as e:
            LOGGER.error(f"Failed to get leaderboard: {e}")
            sleep(0.1)
            if retry == 2:
                return "Failed to get leaderboard"
    for entry in leaderboard.entries:
        if entry.account_name == account_name:
            return f"#{entry.rank} with {hero_name}"
    return "Player not found in leaderboard"


@router.get(
    "/commands/leaderboard-rank/{region}/{account_name}/by-hero-name/{hero_name}",
    summary="Rate Limit 100req/s | Sync with /v1/leaderboard/{region}/{hero_id}",
    response_class=PlainTextResponse,
)
def get_hero_leaderboard_rank_command_by_name(
    res: Response,
    region: Literal["Europe", "Asia", "NAmerica", "SAmerica", "Oceania"],
    account_name: str,
    hero_name: str,
):
    hero_data = requests.get(
        f"https://assets.deadlock-api.com/v2/heroes/by-name/{hero_name.strip()}"
    ).json()
    hero_id = hero_data.get("id")
    if hero_id is None:
        return "Hero not found"
    return get_hero_leaderboard_rank_command(res, region, account_name, hero_id)


@router.get(
    "/commands/record/{account_id}",
    summary="Rate Limit 100req/s | Sync with /v2/players/{account_id}/match-history",
    response_class=PlainTextResponse,
)
def get_record_command(
    res: Response,
    account_id: int,
    last_n_hours: Annotated[int, Query(..., description="Last N hours to check", gt=0, le=24)] = 8,
):
    res.headers["Cache-Control"] = "public, max-age=60"
    account_id = utils.validate_steam_id(account_id)
    match_history = None
    for retry in range(3):
        try:
            match_history = v2.get_player_match_history(account_id).matches
        except Exception as e:
            LOGGER.error(f"Failed to get match history: {e}")
            sleep(0.1)
    if not match_history:
        for retry in range(3):
            try:
                match_history = requests.get(
                    f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
                ).json()
            except Exception as e:
                LOGGER.error(f"Failed to get match history: {e}")
                sleep(0.1)
                if retry == 2:
                    return "Failed to get match history"
    if not match_history:
        return "No match history found"
    min_unix_time = int((datetime.now() - timedelta(hours=last_n_hours)).timestamp())
    matches = [m for m in match_history if m.start_time > min_unix_time]
    wins = sum(m.match_result for m in matches)
    losses = len(matches) - wins
    return f"{wins}W - {losses}L"
