import base64
import inspect
import itertools
import logging
from datetime import datetime, timedelta
from typing import Annotated, Literal

import requests
from cachetools.func import ttl_cache
from fastapi import APIRouter
from fastapi.params import Query
from retry import retry
from starlette.responses import PlainTextResponse, Response

from deadlock_data_api import utils
from deadlock_data_api.conf import CONFIG
from deadlock_data_api.models.leaderboard import Leaderboard, LeaderboardEntry
from deadlock_data_api.models.player_match_history import PlayerMatchHistoryEntry
from deadlock_data_api.routers import v2
from deadlock_data_api.routers.v1_utils import fetch_patch_notes, get_leaderboard

LOGGER = logging.getLogger(__name__)

router = APIRouter(prefix="/v1", tags=["V1"])

RegionType = Literal["Europe", "Asia", "NAmerica", "SAmerica", "Oceania"]


@router.get(
    "/commands/leaderboard-rank/{region}/{account_name}",
    summary="Rate Limit 100req/s | Sync with /v1/leaderboard/{region}",
    deprecated=True,
    include_in_schema=False,
    response_class=PlainTextResponse,
)
def get_leaderboard_rank_command(
    res: Response,
    region: RegionType,
    account_name: str,
):
    res.headers["Cache-Control"] = "public, max-age=60"
    try:
        leaderboard_entry = get_leaderboard_entry(region, account_name)
        rank_name = get_rank_name(leaderboard_entry.badge_level)
        return f"{leaderboard_entry.account_name} is {rank_name} | #{leaderboard_entry.rank}"
    except CommandResolveError as e:
        return str(e)
    except Exception:
        return "Failed to get fetch leaderboard"


@router.get(
    "/commands/leaderboard-rank/{region}/{account_name}/{hero_id}",
    summary="Rate Limit 100req/s | Sync with /v1/leaderboard/{region}/{hero_id}",
    deprecated=True,
    include_in_schema=False,
    response_class=PlainTextResponse,
)
def get_hero_leaderboard_rank_command(
    res: Response,
    region: RegionType,
    account_name: str,
    hero_id: int,
):
    res.headers["Cache-Control"] = "public, max-age=60"
    try:
        response = requests.get(f"https://assets.deadlock-api.com/v2/heroes/{hero_id}").json()
        hero_name = response.get("name")
        leaderboard_entry = get_leaderboard_entry(region, account_name, hero_id)
        return f"#{leaderboard_entry.rank} with {hero_name}"
    except CommandResolveError as e:
        return str(e)
    except Exception:
        return "Failed to get fetch leaderboard"


@router.get(
    "/commands/leaderboard-rank/{region}/{account_name}/by-hero-name/{hero_name}",
    summary="Rate Limit 100req/s | Sync with /v1/leaderboard/{region}/{hero_id}",
    deprecated=True,
    include_in_schema=False,
    response_class=PlainTextResponse,
)
def get_hero_leaderboard_rank_command_by_name(
    res: Response,
    region: RegionType,
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
    include_in_schema=False,
    response_class=PlainTextResponse,
)
def get_record_command(
    res: Response,
    account_id: int,
    last_n_hours: Annotated[int, Query(..., description="Last N hours to check", gt=0)] = 8,
):
    res.headers["Cache-Control"] = "public, max-age=60"
    account_id = utils.validate_steam_id(account_id)
    return resolve_command(
        "{dl_wins_today}W - {dl_losses_today}L", account_id=account_id, last_n_hours=last_n_hours
    )


class CommandResolveError(Exception):
    message: str

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return f"Failed to resolve command: {self.message}"


@ttl_cache(ttl=60)
@retry(tries=3)
def get_leaderboard_with_retry_cached(
    region: RegionType, hero_id: int | None = None
) -> Leaderboard:
    return get_leaderboard(region, hero_id)


@ttl_cache(ttl=60)
@retry(tries=3)
def get_ranks_with_retry_cached() -> dict:
    return requests.get("https://assets.deadlock-api.com/v2/ranks").json()


@ttl_cache(ttl=60)
@retry(tries=3)
def get_account_name_with_retry_cached(account_id: int) -> str:
    account_id = utils.steamid3_to_steamid64(account_id)
    response = requests.get(
        f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?steamids={account_id}",
        headers={"x-webapi-key": CONFIG.steam_api_key},
    ).json()
    response = response.get("response", {})
    account = next(iter(response.get("players", [])), None)
    if account is None:
        raise CommandResolveError(f"Failed to get account name for {account_id}")
    return account["personaname"]


@ttl_cache(ttl=60)
@retry(tries=3)
def get_hero_id_with_retry_cached(hero_name: str) -> int:
    hero_data = requests.get(
        f"https://assets.deadlock-api.com/v2/heroes/by-name/{hero_name.strip()}"
    ).json()
    hero_id = hero_data.get("id")
    if hero_id is None:
        raise CommandResolveError(f"Failed to get hero id for {hero_name}")
    return hero_id


def get_rank_name(rank: int) -> str:
    rank, subrank = divmod(rank, 10)
    ranks = get_ranks_with_retry_cached()
    rank_name = next((r["name"] for r in ranks if r["tier"] == rank), None)
    if rank_name is None:
        raise CommandResolveError(f"Failed to get rank name for {rank}")
    return f"{rank_name} {subrank}"


def get_leaderboard_entry(
    region: RegionType, account_name: str, hero_id: int | None = None
) -> LeaderboardEntry:
    leaderboard = get_leaderboard_with_retry_cached(region, hero_id)
    for entry in leaderboard.entries:
        if entry.account_name == account_name:
            return entry
    raise CommandResolveError("Player not found in leaderboard")


def get_daily_matches(account_id: int) -> list[PlayerMatchHistoryEntry]:
    match_history = v2.get_player_match_history(account_id).matches
    match_history.sort(key=lambda x: x.start_time, reverse=True)

    if not match_history:
        return []

    # If the first match is older than 8 hours ago, we can assume that the player has no matches today
    if match_history[0].start_time < int((datetime.now() - timedelta(hours=8)).timestamp()):
        return []

    # Now we can iterate over the match history
    # All matches that are less than 6 hours apart are considered to be from the same day
    daily_matches = []
    for last_match, match in itertools.pairwise(match_history):
        break_time = abs(last_match.start_time - match.start_time)
        if break_time > timedelta(hours=6).total_seconds():
            break
        daily_matches.append(match)
    return daily_matches


class CommandVariable:
    def steam_account_name(self, account_id: int, *args, **kwargs) -> str:
        return get_account_name_with_retry_cached(account_id)

    def dl_leaderboard_rank(self, region: RegionType, account_id: int, *args, **kwargs) -> str:
        account_name = get_account_name_with_retry_cached(account_id)
        leaderboard_entry = get_leaderboard_entry(region, account_name)
        return get_rank_name(leaderboard_entry.badge_level)

    def dl_leaderboard_place(self, region: RegionType, account_id: int, *args, **kwargs) -> str:
        account_name = get_account_name_with_retry_cached(account_id)
        leaderboard_entry = get_leaderboard_entry(region, account_name)
        return str(leaderboard_entry.rank)

    def dl_hero_leaderboard_place(
        self, region: RegionType, account_id: int, hero_name: str, *args, **kwargs
    ) -> str:
        try:
            hero_id = get_hero_id_with_retry_cached(hero_name)
        except CommandResolveError:
            hero_id = None
        account_name = get_account_name_with_retry_cached(account_id)
        leaderboard_entry = get_leaderboard_entry(region, account_name, hero_id)
        return str(leaderboard_entry.rank)

    def dl_wins_today(
        self,
        account_id: int,
        *args,
        **kwargs,
    ) -> str:
        account_id = utils.validate_steam_id(account_id)
        matches = get_daily_matches(account_id)
        wins = sum(m.match_result for m in matches)
        return str(wins)

    def dl_losses_today(
        self,
        account_id: int,
        *args,
        **kwargs,
    ) -> str:
        account_id = utils.validate_steam_id(account_id)
        matches = get_daily_matches(account_id)
        losses = len(matches) - sum(m.match_result for m in matches)
        return str(losses)

    def dl_latest_patchnotes_title(
        self,
        *args,
        **kwargs,
    ) -> str:
        patch_notes = fetch_patch_notes()
        latest = sorted(patch_notes, key=lambda x: x.pub_date, reverse=True)[0]
        return latest.title

    def dl_latest_patchnotes_link(
        self,
        *args,
        **kwargs,
    ) -> str:
        patch_notes = fetch_patch_notes()
        latest = sorted(patch_notes, key=lambda x: x.pub_date, reverse=True)[0]
        return latest.link


@router.get("/commands/available-variables")
def get_command_variables(res: Response) -> list[str]:
    res.headers["Cache-Control"] = "public, max-age=60"
    variable_resolvers = inspect.getmembers(CommandVariable(), inspect.ismethod)
    return [name for name, _ in variable_resolvers]


@router.get(
    "/commands/{region}/{account_id}/resolve",
    response_class=PlainTextResponse,
)
def get_command_resolve(
    res: Response,
    region: RegionType,
    account_id: int,
    template: Annotated[str | None, Query(..., description="Command template")] = None,
    template_base64: Annotated[
        str | None, Query(..., description="Command template base64 encoded")
    ] = None,
    hero_name: Annotated[
        str | None, Query(..., description="Hero name to check for hero specific stats")
    ] = None,
):
    res.headers["Cache-Control"] = "public, max-age=60"
    account_id = utils.validate_steam_id(account_id)
    if template is None and template_base64 is None:
        return "Missing template"
    if template is None and template_base64 is not None:
        template = base64.b64decode(template_base64).decode("utf-8")
    kwargs = {
        "region": region,
        "account_id": account_id,
        "template": template,
        "hero_name": hero_name,
    }
    LOGGER.info(f"Resolving command: {kwargs['template']}")
    command = resolve_command(**kwargs)
    LOGGER.info(f"Resolved command: {command}")
    return command


def resolve_command(template: str, **kwargs) -> str:
    variable_resolvers = inspect.getmembers(CommandVariable(), inspect.ismethod)
    for name, resolver in variable_resolvers:
        template_str = f"{{{name}}}"
        if template_str in template:
            value_str = resolver(**kwargs)
            template = template.replace(template_str, value_str)
            LOGGER.debug(f"Resolved {template_str} to {value_str}")
    return template
