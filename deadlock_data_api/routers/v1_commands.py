import logging
from typing import Annotated, Literal

import requests
from cachetools.func import ttl_cache
from fastapi import APIRouter
from fastapi.params import Query
from retry import retry
from starlette.datastructures import URL
from starlette.responses import PlainTextResponse, RedirectResponse, Response
from starlette.status import HTTP_301_MOVED_PERMANENTLY

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
        rank_name = get_rank_name(leaderboard_entry["badge_level"])
        return f"{leaderboard_entry['account_name']} is {rank_name} | #{leaderboard_entry['rank']}"
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
        return f"#{leaderboard_entry['rank']} with {hero_name}"
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
    summary="Moved to new API: https://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: https://api.deadlock-api.com/docs
- New API Endpoint: https://api.deadlock-api.com/v1/commands/resolve
    """,
    deprecated=True,
    include_in_schema=False,
)
def get_record_command(account_id: int) -> RedirectResponse:
    url = URL("https://api.deadlock-api.com/v1/commands/resolve")
    url = url.include_query_params(
        region="NAmerica", account_id=account_id, template="{wins_today}W - {losses_today}L"
    )
    return RedirectResponse(url, HTTP_301_MOVED_PERMANENTLY)


class CommandResolveError(Exception):
    message: str

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return f"Failed to resolve command: {self.message}"


@ttl_cache(ttl=60)
@retry(tries=3)
def get_leaderboard_with_retry_cached(region: RegionType, hero_id: int | None = None) -> dict:
    if hero_id:
        return requests.get(
            f"https://api.deadlock-api.com/v1/leaderboard/{region}/{hero_id}"
        ).json()
    else:
        return requests.get(f"https://api.deadlock-api.com/v1/leaderboard/{region}").json()


@ttl_cache(ttl=60)
@retry(tries=3)
def get_ranks_with_retry_cached() -> dict:
    return requests.get("https://assets.deadlock-api.com/v2/ranks").json()


# @ttl_cache(ttl=60 * 60)
# @retry(tries=3)
# def get_account_name_with_retry_cached(account_id: int) -> str:
#     account_id = utils.steamid3_to_steamid64(account_id)
#     response = requests.get(
#         f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?steamids={account_id}",
#         headers={"x-webapi-key": CONFIG.steam_api_key},
#     ).json()
#     response = response.get("response", {})
#     account = next(iter(response.get("players", [])), None)
#     if account is None:
#         raise CommandResolveError(f"Failed to get account name for {account_id}")
#     return account["personaname"]


# @ttl_cache(ttl=60 * 60)
# @retry(tries=3)
# def get_hero_id_with_retry_cached(hero_name: str) -> int:
#     if not hero_name:
#         raise CommandResolveError("Hero name is empty")
#     hero_data = requests.get(
#         f"https://assets.deadlock-api.com/v2/heroes/by-name/{hero_name.strip()}"
#     ).json()
#     hero_id = hero_data.get("id")
#     if hero_id is None:
#         raise CommandResolveError(f"Failed to get hero id for {hero_name}")
#     return hero_id


# @ttl_cache(ttl=60)
# @retry(tries=3)
# def fetch_match_history_with_retry_cached(account_id: int) -> list[dict]:
#     response = requests.get(f"https://api.deadlock-api.com/v1/players/{account_id}/match-history")
#     if not response.ok:
#         raise CommandResolveError("Failed to fetch match history")
#     return response.json()


def get_rank_name(rank: int) -> str:
    rank, subrank = divmod(rank, 10)
    ranks = get_ranks_with_retry_cached()
    rank_name = next((r["name"] for r in ranks if r["tier"] == rank), None)
    if rank_name is None:
        raise CommandResolveError(f"Failed to get rank name for {rank}")
    return f"{rank_name} {subrank}"


# def get_rank_img(rank: int) -> str:
#     rank, subrank = divmod(rank, 10)
#     ranks = get_ranks_with_retry_cached()
#     rank_image = next(
#         (r["images"][f"small_subrank{subrank}"] for r in ranks if r["tier"] == rank), None
#     )
#     if rank_image is None:
#         raise CommandResolveError(f"Failed to get rank image for {rank}")
#     return rank_image


def get_leaderboard_entry(
    region: RegionType, account_name: str, hero_id: int | None = None
) -> dict:
    leaderboard = get_leaderboard_with_retry_cached(region, hero_id).get("entries", [])
    for entry in leaderboard:
        if entry["account_name"] == account_name:
            return entry
    raise CommandResolveError("Player not found in leaderboard")


# def get_daily_matches(account_id: int) -> list[dict]:
#     match_history = fetch_match_history_with_retry_cached(account_id)
#     if not match_history:
#         return []
#     first_match = match_history[0]
#
#     # If the first match is older than 8 hours ago, we can assume that the player has no matches today
#     if first_match["start_time"] < int((datetime.now() - timedelta(hours=8)).timestamp()):
#         return []
#
#     # Now we can iterate over the match history
#     # All matches that are less than 6 hours apart are considered to be from the same day
#     daily_matches = [first_match]
#     for last_match, match in itertools.pairwise(match_history):
#         break_time = abs(last_match["start_time"] - match["start_time"])
#         if break_time > timedelta(hours=6).total_seconds():
#             break
#         daily_matches.append(match)
#     return daily_matches


# @ttl_cache(ttl=60 * 60)
# def fetch_patch_notes() -> list[dict]:
#     return requests.get("https://api.deadlock-api.com/v1/patches", timeout=5).json()


# class CommandVariable:
#     def steam_account_name(self, account_id: int, *args, **kwargs) -> str:
#         """Get the steam account name"""
#         return get_account_name_with_retry_cached(account_id)
#
#     def leaderboard_rank(self, region: RegionType, account_id: int, *args, **kwargs) -> str:
#         """Get the leaderboard rank"""
#         account_name = get_account_name_with_retry_cached(account_id)
#         leaderboard_entry = get_leaderboard_entry(region, account_name)
#         return get_rank_name(leaderboard_entry["badge_level"])
#
#     def leaderboard_rank_badge_level(
#         self, region: RegionType, account_id: int, *args, **kwargs
#     ) -> str:
#         """Get the leaderboard rank badge level"""
#         account_name = get_account_name_with_retry_cached(account_id)
#         leaderboard_entry = get_leaderboard_entry(region, account_name)
#         return str(leaderboard_entry["badge_level"])
#
#     def leaderboard_rank_img(self, region: RegionType, account_id: int, *args, **kwargs) -> str:
#         """Get the leaderboard rank"""
#         account_name = get_account_name_with_retry_cached(account_id)
#         leaderboard_entry = get_leaderboard_entry(region, account_name)
#         return get_rank_img(leaderboard_entry["badge_level"])
#
#     def leaderboard_place(self, region: RegionType, account_id: int, *args, **kwargs) -> str:
#         """Get the leaderboard place"""
#         account_name = get_account_name_with_retry_cached(account_id)
#         leaderboard_entry = get_leaderboard_entry(region, account_name)
#         return f"#{leaderboard_entry['rank']}"
#
#     def hero_leaderboard_place(
#         self, region: RegionType, account_id: int, hero_name: str, *args, **kwargs
#     ) -> str:
#         """Get the leaderboard place for a specific hero"""
#         try:
#             hero_id = get_hero_id_with_retry_cached(hero_name)
#         except CommandResolveError:
#             hero_id = None
#         account_name = get_account_name_with_retry_cached(account_id)
#         leaderboard_entry = get_leaderboard_entry(region, account_name, hero_id)
#         return f"#{leaderboard_entry['rank']}"
#
#     def wins_today(self, account_id: int, *args, **kwargs) -> str:
#         """Get the number of wins today"""
#         matches = get_daily_matches(account_id)
#         wins = sum(m["match_result"] == m["player_team"] for m in matches)
#         return str(wins)
#
#     def losses_today(self, account_id: int, *args, **kwargs) -> str:
#         """Get the number of losses today"""
#         matches = get_daily_matches(account_id)
#         losses = sum(m["match_result"] != m["player_team"] for m in matches)
#         return str(losses)
#
#     def matches_today(self, account_id: int, *args, **kwargs) -> str:
#         """Get the number of matches today"""
#         matches = get_daily_matches(account_id)
#         return str(len(matches))
#
#     def winrate_today(self, account_id: int, *args, **kwargs) -> str:
#         """Get the winrate today"""
#         wins = int(self.wins_today(account_id))
#         losses = int(self.losses_today(account_id))
#         if wins + losses == 0:
#             return "0.00%"
#         return f"{wins / (wins + losses):.2%}"
#
#     def wins_losses_today(self, account_id: int, *args, **kwargs) -> str:
#         """Get the number of wins and losses today"""
#         matches = get_daily_matches(account_id)
#         wins = sum(m["match_result"] == m["player_team"] for m in matches)
#         losses = sum(m["match_result"] != m["player_team"] for m in matches)
#         return f"{wins}-{losses}"
#
#     def heroes_played_today(self, account_id: int, *args, **kwargs) -> str:
#         """Get a list of all heroes played today with the number of matches played"""
#         matches = get_daily_matches(account_id)
#         hero_counts = Counter(m["hero_id"] for m in matches)
#         hero_data = requests.get("https://assets.deadlock-api.com/v2/heroes").json()
#         hero_name = {hero["id"]: hero["name"] for hero in hero_data}
#         return ", ".join(
#             f"{hero_name.get(hero_id, {})} ({count})" for hero_id, count in hero_counts.items()
#         )
#
#     def highest_kill_count(self, account_id: int, *args, **kwargs) -> str:
#         """Get the highest kill count in a match"""
#         matches = fetch_match_history_with_retry_cached(account_id)
#         return str(max((m.get("player_kills", 0) for m in matches), default=0))
#
#     def highest_death_count(self, account_id: int, *args, **kwargs) -> str:
#         """Get the highest death count in a match"""
#         matches = fetch_match_history_with_retry_cached(account_id)
#         return str(max((m.get("player_deaths", 0) for m in matches), default=0))
#
#     def highest_net_worth(self, account_id: int, *args, **kwargs) -> str:
#         """Get the highest net worth in a match"""
#         matches = fetch_match_history_with_retry_cached(account_id)
#         return str(max((m.get("net_worth", 0) for m in matches), default=0))
#
#     def highest_last_hits(self, account_id: int, *args, **kwargs) -> str:
#         """Get the highest last hits in a match"""
#         matches = fetch_match_history_with_retry_cached(account_id)
#         return str(max((m.get("last_hits", 0) for m in matches), default=0))
#
#     def highest_denies(self, account_id: int, *args, **kwargs) -> str:
#         """Get the highest denies in a match"""
#         matches = fetch_match_history_with_retry_cached(account_id)
#         return str(max((m.get("denies", 0) for m in matches), default=0))
#
#     def most_played_hero(self, account_id: int, *args, **kwargs) -> str:
#         """Get the most played hero"""
#         matches = fetch_match_history_with_retry_cached(account_id)
#         hero_counts = Counter(m.get("hero_id") for m in matches)
#         hero_id, _ = hero_counts.most_common(1)[0]
#         hero_data = requests.get(f"https://assets.deadlock-api.com/v2/heroes/{hero_id}").json()
#         return hero_data.get("name")
#
#     def most_played_hero_count(self, account_id: int, *args, **kwargs) -> str:
#         """Get the most played hero count"""
#         matches = fetch_match_history_with_retry_cached(account_id)
#         hero_counts = Counter(m.get("hero_id") for m in matches)
#         _, count = hero_counts.most_common(1)[0]
#         return str(count)
#
#     def total_kills(self, account_id: int, *args, **kwargs) -> str:
#         """Get the total kills in all matches"""
#         matches = fetch_match_history_with_retry_cached(account_id)
#         return str(sum(m.get("player_kills", 0) for m in matches))
#
#     def hero_kills(self, account_id: int, hero_name: str, *args, **kwargs) -> str:
#         """Get the total kills in all matches for a specific hero"""
#         hero_id = get_hero_id_with_retry_cached(hero_name)
#         matches = fetch_match_history_with_retry_cached(account_id)
#         return str(sum(m.get("player_kills", 0) for m in matches if m.get("hero_id") == hero_id))
#
#     def total_kd(self, account_id: int, *args, **kwargs) -> str:
#         """Get the KD ratio"""
#         matches = fetch_match_history_with_retry_cached(account_id)
#         total_kills = sum(m.get("player_kills", 0) for m in matches)
#         total_deaths = sum(m.get("player_deaths", 0) for m in matches)
#         return f"{total_kills / total_deaths:.2f}" if total_deaths > 0 else "0.00"
#
#     def hero_kd(self, account_id: int, hero_name: str, *args, **kwargs) -> str:
#         """Get the KD ratio for a specific hero"""
#         hero_id = get_hero_id_with_retry_cached(hero_name)
#         matches = fetch_match_history_with_retry_cached(account_id)
#         total_kills = sum(m.get("player_kills", 0) for m in matches if m.get("hero_id") == hero_id)
#         total_deaths = sum(
#             m.get("player_deaths", 0) for m in matches if m.get("hero_id") == hero_id
#         )
#         return f"{total_kills / total_deaths:.2f}" if total_deaths > 0 else "0.00"
#
#     def total_wins(self, account_id: int, *args, **kwargs) -> str:
#         """Get the total number of wins"""
#         matches = fetch_match_history_with_retry_cached(account_id)
#         matches = [m for m in matches if m.get("match_result") == m.get("player_team")]
#         return str(len(matches))
#
#     def hero_wins(self, account_id: int, hero_name: str, *args, **kwargs) -> str:
#         """Get the total number of wins for a specific hero"""
#         hero_id = get_hero_id_with_retry_cached(hero_name)
#         matches = fetch_match_history_with_retry_cached(account_id)
#         matches = [
#             m
#             for m in matches
#             if m.get("match_result") == m.get("player_team") and m.get("hero_id") == hero_id
#         ]
#         return str(len(matches))
#
#     def total_losses(self, account_id: int, *args, **kwargs) -> str:
#         """Get the total number of losses"""
#         matches = fetch_match_history_with_retry_cached(account_id)
#         matches = [m for m in matches if m.get("match_result") != m.get("player_team")]
#         return str(len(matches))
#
#     def hero_losses(self, account_id: int, hero_name: str, *args, **kwargs) -> str:
#         """Get the total number of losses for a specific hero"""
#         hero_id = get_hero_id_with_retry_cached(hero_name)
#         matches = fetch_match_history_with_retry_cached(account_id)
#         matches = [
#             m
#             for m in matches
#             if m.get("match_result") != m.get("player_team") and m.get("hero_id") == hero_id
#         ]
#         return str(len(matches))
#
#     def total_winrate(self, account_id: int, *args, **kwargs) -> str:
#         """Get the total winrate"""
#         wins = int(self.total_wins(account_id))
#         losses = int(self.total_losses(account_id))
#         return f"{wins / (wins + losses):.2%}" if wins + losses > 0 else "0.00%"
#
#     def hero_winrate(self, account_id: int, hero_name: str, *args, **kwargs) -> str:
#         """Get the total winrate for a specific hero"""
#         wins = int(self.hero_wins(account_id, hero_name))
#         losses = int(self.hero_losses(account_id, hero_name))
#         return f"{wins / (wins + losses):.2%}" if wins + losses > 0 else "0.00%"
#
#     def total_matches(self, account_id: int, *args, **kwargs) -> str:
#         """Get the total number of matches played"""
#         matches = fetch_match_history_with_retry_cached(account_id)
#         return str(len(matches))
#
#     def hero_matches(self, account_id: int, hero_name: str, *args, **kwargs) -> str:
#         """Get the total number of matches played for a specific hero"""
#         hero_id = get_hero_id_with_retry_cached(hero_name)
#         matches = fetch_match_history_with_retry_cached(account_id)
#         return str(len([m for m in matches if m.get("hero_id") == hero_id]))
#
#     def hours_played(self, account_id: int, *args, **kwargs) -> str:
#         """Get the total hours played in all matches"""
#         matches = fetch_match_history_with_retry_cached(account_id)
#         return f"{sum(m.get('match_duration_s', 0) for m in matches) // 3600}h"
#
#     def hero_hours_played(self, account_id: int, hero_name: str, *args, **kwargs) -> str:
#         """Get the total hours played in all matches for a specific hero"""
#         try:
#             hero_id = get_hero_id_with_retry_cached(hero_name)
#         except CommandResolveError:
#             return "Hero not found"
#         matches = fetch_match_history_with_retry_cached(account_id)
#         return f"{
#             sum(m.get('match_duration_s', 0) for m in matches if m.get('hero_id') == hero_id)
#             // 3600
#         }h"
#
#     def latest_patchnotes_title(self, *args, **kwargs) -> str:
#         """Get the title of the latest patch notes"""
#         patch_notes = fetch_patch_notes()
#         latest = sorted(patch_notes, key=lambda x: x["pub_date"], reverse=True)[0]
#         return latest["title"]
#
#     def latest_patchnotes_link(self, *args, **kwargs) -> str:
#         """Get the link to the latest patch notes"""
#         patch_notes = fetch_patch_notes()
#         latest = sorted(patch_notes, key=lambda x: x["pub_date"], reverse=True)[0]
#         return latest["link"]


# class Variable(BaseModel):
#     name: str
#     description: str | None = None
#     extra_args: list[str] | None = None


@router.get(
    "/commands/widget-versions",
    summary="Moved to new API: https://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: https://api.deadlock-api.com/docs
- New API Endpoint: https://api.deadlock-api.com/v1/commands/widgets/versions
    """,
    deprecated=True,
)
def get_widget_versions() -> RedirectResponse:
    return RedirectResponse(
        "https://api.deadlock-api.com/v1/commands/widgets/versions", HTTP_301_MOVED_PERMANENTLY
    )


@router.get(
    "/commands/available-variables",
    summary="Moved to new API: https://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: https://api.deadlock-api.com/docs
- New API Endpoint: https://api.deadlock-api.com/v1/commands/variables/available
    """,
    deprecated=True,
)
def get_command_variables() -> RedirectResponse:
    return RedirectResponse(
        "https://api.deadlock-api.com/v1/commands/variables/available", HTTP_301_MOVED_PERMANENTLY
    )


@router.get(
    "/commands/{region}/{account_id}/resolve",
    summary="Moved to new API: https://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: https://api.deadlock-api.com/docs
- New API Endpoint: https://api.deadlock-api.com/v1/commands/resolve
    """,
    deprecated=True,
)
def get_command_resolve(
    region: RegionType,
    account_id: int,
    template: Annotated[str | None, Query(..., description="Command template")] = None,
    hero_name: Annotated[
        str | None, Query(..., description="Hero name to check for hero specific stats")
    ] = None,
) -> RedirectResponse:
    url = URL("https://api.deadlock-api.com/v1/commands/resolve")
    url = url.include_query_params(region=region, account_id=account_id, template=template)
    if hero_name:
        url = url.include_query_params(hero_name=hero_name)
    return RedirectResponse(url, HTTP_301_MOVED_PERMANENTLY)


@router.get(
    "/commands/{region}/{account_id}/resolve-variables",
    summary="Moved to new API: https://api.deadlock-api.com/",
    description="""
# Endpoint moved to new API
- New API Docs: https://api.deadlock-api.com/docs
- New API Endpoint: https://api.deadlock-api.com/v1/commands/variables/resolve
    """,
    deprecated=True,
)
def get_variables_resolve(
    region: RegionType,
    account_id: int,
    variables: Annotated[str, Query(..., description="Variables to resolve, separated by comma")],
    hero_name: Annotated[
        str | None, Query(..., description="Hero name to check for hero specific stats")
    ] = None,
) -> RedirectResponse:
    url = URL("https://api.deadlock-api.com/v1/commands/variables/resolve")
    url = url.include_query_params(region=region, account_id=account_id, variables=variables)
    if hero_name:
        url = url.include_query_params(hero_name=hero_name)
    return RedirectResponse(url, HTTP_301_MOVED_PERMANENTLY)


# def resolve_command(template: str, **kwargs) -> str:
#     variable_resolvers = inspect.getmembers(CommandVariable(), inspect.ismethod)
#     for name, resolver in variable_resolvers:
#         template_str = f"{{{name}}}"
#         if template_str in template:
#             value_str = resolver(**kwargs)
#             template = template.replace(template_str, str(value_str))
#             LOGGER.debug(f"Resolved {template_str} to {value_str}")
#     return template
