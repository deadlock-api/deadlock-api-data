import base64
import inspect
import itertools
import json
import logging
import os.path
from collections import Counter
from collections.abc import Generator
from datetime import datetime, timedelta
from typing import Annotated, Literal

import requests
from cachetools.func import ttl_cache
from fastapi import APIRouter, HTTPException
from fastapi.params import Query
from more_itertools import peekable
from pydantic import BaseModel
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
    if not hero_name:
        return "Missing hero name"
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
        "{wins_today}W - {losses_today}L", account_id=account_id, last_n_hours=last_n_hours
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
    if not hero_name:
        raise CommandResolveError("Hero name is empty")
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


def get_rank_img(rank: int) -> str:
    rank, subrank = divmod(rank, 10)
    ranks = get_ranks_with_retry_cached()
    rank_image = next(
        (r["images"][f"small_subrank{subrank}"] for r in ranks if r["tier"] == rank), None
    )
    if rank_image is None:
        raise CommandResolveError(f"Failed to get rank image for {rank}")
    return rank_image


def get_leaderboard_entry(
    region: RegionType, account_name: str, hero_id: int | None = None
) -> LeaderboardEntry:
    leaderboard = get_leaderboard_with_retry_cached(region, hero_id)
    for entry in leaderboard.entries:
        if entry.account_name == account_name:
            return entry
    raise CommandResolveError("Player not found in leaderboard")


def next_match_generator(account_id: int) -> Generator[PlayerMatchHistoryEntry, None, None]:
    last_match_id = None
    while last_match_id is None or last_match_id > 0:
        match_history = v2.get_player_match_history(
            account_id, last_match_id, insert_to_ch=False
        ).matches
        if not match_history:
            raise StopIteration
        for match in sorted(match_history, key=lambda x: x.start_time, reverse=True):
            last_match_id = match.match_id
            yield match
    raise StopIteration


def get_daily_matches(account_id: int) -> list[PlayerMatchHistoryEntry]:
    match_history = peekable(next_match_generator(account_id))
    first_match = match_history.peek()

    # If the first match is older than 8 hours ago, we can assume that the player has no matches today
    if first_match.start_time < int((datetime.now() - timedelta(hours=8)).timestamp()):
        return []

    # Now we can iterate over the match history
    # All matches that are less than 6 hours apart are considered to be from the same day
    daily_matches = [first_match]
    for last_match, match in itertools.pairwise(match_history):
        break_time = abs(last_match.start_time - match.start_time)
        if break_time > timedelta(hours=6).total_seconds():
            break
        daily_matches.append(match)
    return daily_matches


class CommandVariable:
    def steam_account_name(self, account_id: int, *args, **kwargs) -> str:
        """Get the steam account name"""
        return get_account_name_with_retry_cached(account_id)

    def leaderboard_rank(self, region: RegionType, account_id: int, *args, **kwargs) -> str:
        """Get the leaderboard rank"""
        account_name = get_account_name_with_retry_cached(account_id)
        leaderboard_entry = get_leaderboard_entry(region, account_name)
        return get_rank_name(leaderboard_entry.badge_level)

    def leaderboard_rank_img(self, region: RegionType, account_id: int, *args, **kwargs) -> str:
        """Get the leaderboard rank"""
        account_name = get_account_name_with_retry_cached(account_id)
        leaderboard_entry = get_leaderboard_entry(region, account_name)
        return get_rank_img(leaderboard_entry.badge_level)

    def leaderboard_place(self, region: RegionType, account_id: int, *args, **kwargs) -> str:
        """Get the leaderboard place"""
        account_name = get_account_name_with_retry_cached(account_id)
        leaderboard_entry = get_leaderboard_entry(region, account_name)
        return f"#{leaderboard_entry.rank}"

    def hero_leaderboard_place(
        self, region: RegionType, account_id: int, hero_name: str, *args, **kwargs
    ) -> str:
        """Get the leaderboard place for a specific hero"""
        try:
            hero_id = get_hero_id_with_retry_cached(hero_name)
        except CommandResolveError:
            hero_id = None
        account_name = get_account_name_with_retry_cached(account_id)
        leaderboard_entry = get_leaderboard_entry(region, account_name, hero_id)
        return f"#{leaderboard_entry.rank}"

    def wins_today(self, account_id: int, *args, **kwargs) -> str:
        """Get the number of wins today"""
        matches = get_daily_matches(account_id)
        wins = sum(m.match_result == m.player_team for m in matches)
        return str(wins)

    def losses_today(self, account_id: int, *args, **kwargs) -> str:
        """Get the number of losses today"""
        matches = get_daily_matches(account_id)
        losses = sum(m.match_result != m.player_team for m in matches)
        return str(losses)

    def matches_today(self, account_id: int, *args, **kwargs) -> str:
        """Get the number of matches today"""
        matches = get_daily_matches(account_id)
        return str(len(matches))

    def winrate_today(self, account_id: int, *args, **kwargs) -> str:
        """Get the winrate today"""
        wins = int(self.wins_today(account_id))
        losses = int(self.losses_today(account_id))
        if wins + losses == 0:
            return "0.00%"
        return f"{wins / (wins + losses):.2%}"

    def wins_losses_today(self, account_id: int, *args, **kwargs) -> str:
        """Get the number of wins and losses today"""
        matches = get_daily_matches(account_id)
        wins = sum(m.match_result == m.player_team for m in matches)
        losses = sum(m.match_result != m.player_team for m in matches)
        return f"{wins}-{losses}"

    def highest_kill_count(self, account_id: int, *args, **kwargs) -> str:
        """Get the highest kill count in a match"""
        matches = requests.get(
            f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
        ).json()
        if not matches:
            return "No matches found"
        return str(max((m.get("player_kills", 0) for m in matches), default=0))

    def highest_death_count(self, account_id: int, *args, **kwargs) -> str:
        """Get the highest death count in a match"""
        matches = requests.get(
            f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
        ).json()
        return str(max((m.get("player_deaths", 0) for m in matches), default=0))

    def highest_net_worth(self, account_id: int, *args, **kwargs) -> str:
        """Get the highest net worth in a match"""
        matches = requests.get(
            f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
        ).json()
        return str(max((m.get("net_worth", 0) for m in matches), default=0))

    def highest_last_hits(self, account_id: int, *args, **kwargs) -> str:
        """Get the highest last hits in a match"""
        matches = requests.get(
            f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
        ).json()
        return str(max((m.get("last_hits", 0) for m in matches), default=0))

    def highest_denies(self, account_id: int, *args, **kwargs) -> str:
        """Get the highest denies in a match"""
        matches = requests.get(
            f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
        ).json()
        return str(max((m.get("denies", 0) for m in matches), default=0))

    def most_played_hero(self, account_id: int, *args, **kwargs) -> str:
        """Get the most played hero"""
        matches = requests.get(
            f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
        ).json()
        hero_counts = Counter(m.get("hero_id") for m in matches)
        hero_id, _ = hero_counts.most_common(1)[0]
        hero_data = requests.get(f"https://assets.deadlock-api.com/v2/heroes/{hero_id}").json()
        return hero_data.get("name")

    def most_played_hero_count(self, account_id: int, *args, **kwargs) -> str:
        """Get the most played hero count"""
        matches = requests.get(
            f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
        ).json()
        hero_counts = Counter(m.get("hero_id") for m in matches)
        _, count = hero_counts.most_common(1)[0]
        return str(count)

    def hero_level(self, account_id: int, hero_name: str, *args, **kwargs) -> str:
        """Get the hero level"""
        hero_id = get_hero_id_with_retry_cached(hero_name)
        matches = requests.get(
            f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
        ).json()
        return str(
            max((m.get("hero_level", 0) for m in matches if m.get("hero_id") == hero_id), default=0)
        )

    def total_kills(self, account_id: int, *args, **kwargs) -> str:
        """Get the total kills in all matches"""
        matches = requests.get(
            f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
        ).json()
        return str(sum(m.get("player_kills", 0) for m in matches))

    def hero_kills(self, account_id: int, hero_name: str, *args, **kwargs) -> str:
        """Get the total kills in all matches for a specific hero"""
        hero_id = get_hero_id_with_retry_cached(hero_name)
        matches = requests.get(
            f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
        ).json()
        return str(sum(m.get("player_kills", 0) for m in matches if m.get("hero_id") == hero_id))

    def total_kd(self, account_id: int, *args, **kwargs) -> str:
        """Get the KD ratio"""
        matches = requests.get(
            f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
        ).json()
        total_kills = sum(m.get("player_kills", 0) for m in matches)
        total_deaths = sum(m.get("player_deaths", 0) for m in matches)
        return f"{total_kills / total_deaths:.2f}" if total_deaths > 0 else "0.00"

    def hero_kd(self, account_id: int, hero_name: str, *args, **kwargs) -> str:
        """Get the KD ratio for a specific hero"""
        hero_id = get_hero_id_with_retry_cached(hero_name)
        matches = requests.get(
            f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
        ).json()
        total_kills = sum(m.get("player_kills", 0) for m in matches if m.get("hero_id") == hero_id)
        total_deaths = sum(
            m.get("player_deaths", 0) for m in matches if m.get("hero_id") == hero_id
        )
        return f"{total_kills / total_deaths:.2f}" if total_deaths > 0 else "0.00"

    def total_wins(self, account_id: int, *args, **kwargs) -> str:
        """Get the total number of wins"""
        matches = requests.get(
            f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
        ).json()

        def team_index(team: str) -> int:
            if team == "Team0":
                return 0
            elif team == "Team1":
                return 1
            else:
                return -1

        matches = [m for m in matches if m.get("match_result") == team_index(m.get("player_team"))]
        return str(len(matches))

    def hero_wins(self, account_id: int, hero_name: str, *args, **kwargs) -> str:
        """Get the total number of wins for a specific hero"""
        hero_id = get_hero_id_with_retry_cached(hero_name)
        matches = requests.get(
            f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
        ).json()

        def team_index(team: str) -> int:
            if team == "Team0":
                return 0
            elif team == "Team1":
                return 1
            else:
                return -1

        matches = [
            m
            for m in matches
            if m.get("match_result") == team_index(m.get("player_team"))
            and m.get("hero_id") == hero_id
        ]
        return str(len(matches))

    def total_losses(self, account_id: int, *args, **kwargs) -> str:
        """Get the total number of losses"""
        matches = requests.get(
            f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
        ).json()

        def team_index(team: str) -> int:
            if team == "Team0":
                return 0
            elif team == "Team1":
                return 1
            else:
                return -1

        matches = [m for m in matches if m.get("match_result") != team_index(m.get("player_team"))]
        return str(len(matches))

    def hero_losses(self, account_id: int, hero_name: str, *args, **kwargs) -> str:
        """Get the total number of losses for a specific hero"""
        hero_id = get_hero_id_with_retry_cached(hero_name)
        matches = requests.get(
            f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
        ).json()

        def team_index(team: str) -> int:
            if team == "Team0":
                return 0
            elif team == "Team1":
                return 1
            else:
                return -1

        matches = [
            m
            for m in matches
            if m.get("match_result") != team_index(m.get("player_team"))
            and m.get("hero_id") == hero_id
        ]
        return str(len(matches))

    def total_winrate(self, account_id: int, *args, **kwargs) -> str:
        """Get the total winrate"""
        wins = int(self.total_wins(account_id))
        losses = int(self.total_losses(account_id))
        return f"{wins / (wins + losses):.2%}"

    def hero_winrate(self, account_id: int, hero_name: str, *args, **kwargs) -> str:
        """Get the total winrate for a specific hero"""
        wins = int(self.hero_wins(account_id, hero_name))
        losses = int(self.hero_losses(account_id, hero_name))
        return f"{wins / (wins + losses):.2%}"

    def total_matches(self, account_id: int, *args, **kwargs) -> str:
        """Get the total number of matches played"""
        matches = requests.get(
            f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
        ).json()
        return str(len(matches))

    def hero_matches(self, account_id: int, hero_name: str, *args, **kwargs) -> str:
        """Get the total number of matches played for a specific hero"""
        hero_id = get_hero_id_with_retry_cached(hero_name)
        matches = requests.get(
            f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
        ).json()
        return str(len([m for m in matches if m.get("hero_id") == hero_id]))

    def hours_played(self, account_id: int, *args, **kwargs) -> str:
        """Get the total hours played in all matches"""
        matches = requests.get(
            f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
        ).json()
        return f"{sum(m.get('match_duration_s', 0) for m in matches) // 3600}h"

    def hero_hours_played(self, account_id: int, hero_name: str, *args, **kwargs) -> str:
        """Get the total hours played in all matches for a specific hero"""
        try:
            hero_id = get_hero_id_with_retry_cached(hero_name)
        except CommandResolveError:
            return "Hero not found"
        matches = requests.get(
            f"https://analytics.deadlock-api.com/v2/players/{account_id}/match-history"
        ).json()
        return f"{
            sum(m.get('match_duration_s', 0) for m in matches if m.get('hero_id') == hero_id)
            // 3600
        }h"

    def latest_patchnotes_title(self, *args, **kwargs) -> str:
        """Get the title of the latest patch notes"""
        patch_notes = fetch_patch_notes()
        latest = sorted(patch_notes, key=lambda x: x.pub_date, reverse=True)[0]
        return latest.title

    def latest_patchnotes_link(self, *args, **kwargs) -> str:
        """Get the link to the latest patch notes"""
        patch_notes = fetch_patch_notes()
        latest = sorted(patch_notes, key=lambda x: x.pub_date, reverse=True)[0]
        return latest.link


class Variable(BaseModel):
    name: str
    description: str | None = None
    extra_args: list[str] | None = None


@router.get("/commands/widget-versions")
def get_widget_versions(res: Response) -> dict[str, int]:
    res.headers["Cache-Control"] = "public, max-age=60"
    try:
        with open("widget_versions.json") as f:
            return json.load(f)
    except FileNotFoundError | json.JSONDecodeError as e:
        LOGGER.error(
            f"Failed to load widget versions from {os.path.join(os.getcwd(), 'widget_versions.json')}: {e}"
        )
        raise HTTPException(status_code=500, detail="Failed to load widget versions")


@router.get("/commands/available-variables")
def get_command_variables(res: Response) -> list[Variable]:
    res.headers["Cache-Control"] = "public, max-age=60"
    variable_resolvers = inspect.getmembers(CommandVariable(), inspect.ismethod)

    def to_variable(name, resolver):
        args = inspect.signature(resolver).parameters.keys() - {
            "self",
            "region",
            "account_id",
            "args",
            "kwargs",
        }
        return Variable(
            name=name,
            description=resolver.__doc__ if resolver.__doc__ else None,
            extra_args=list(args) if args else None,
        )

    return [to_variable(name, resolver) for name, resolver in variable_resolvers]


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
) -> str:
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
    try:
        command = resolve_command(**kwargs)
    except CommandResolveError as e:
        return str(e)
    LOGGER.info(f"Resolved command: {command}")
    return command


@router.get("/commands/{region}/{account_id}/resolve-variables")
def get_variables_resolve(
    res: Response,
    region: RegionType,
    account_id: int,
    variables: Annotated[str, Query(..., description="Variables to resolve, separated by comma")],
    hero_name: Annotated[
        str | None, Query(..., description="Hero name to check for hero specific stats")
    ] = None,
) -> dict[str, str | None]:
    res.headers["Cache-Control"] = "public, max-age=60"
    account_id = utils.validate_steam_id(account_id)
    variable_resolvers = inspect.getmembers(CommandVariable(), inspect.ismethod)
    variables = set(variables.lower().split(","))
    kwargs = {
        "region": region,
        "account_id": account_id,
        "hero_name": hero_name,
    }
    try:
        resolved_variables = {}
        for name, resolver in variable_resolvers:
            if name in variables:
                try:
                    resolved_variables[name] = resolver(**kwargs)
                except CommandResolveError:
                    resolved_variables[name] = None
        LOGGER.info(f"Resolved variables: {resolved_variables}")
        return resolved_variables
    except CommandResolveError as e:
        raise HTTPException(status_code=400, detail=str(e))


def resolve_command(template: str, **kwargs) -> str:
    variable_resolvers = inspect.getmembers(CommandVariable(), inspect.ismethod)
    for name, resolver in variable_resolvers:
        template_str = f"{{{name}}}"
        if template_str in template:
            value_str = resolver(**kwargs)
            template = template.replace(template_str, str(value_str))
            LOGGER.debug(f"Resolved {template_str} to {value_str}")
    return template


if __name__ == "__main__":
    for name, resolver in inspect.getmembers(CommandVariable(), inspect.ismethod):
        print(
            name, resolver(**{"region": "NAmerica", "account_id": 74963221, "hero_name": "bebop"})
        )
