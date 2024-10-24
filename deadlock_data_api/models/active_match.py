from pydantic import BaseModel, ConfigDict, Field


class ActiveMatchPlayer(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    account_id: int
    team: int
    abandoned: bool
    hero_id: int


class ActiveMatch(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    start_time: int
    winning_team: int
    match_id: int
    players: list[ActiveMatchPlayer]
    lobby_id: int
    net_worth_team_0: int
    net_worth_team_1: int
    duration_s: int
    spectators: int
    open_spectator_slots: int
    objectives_mask_team0: int
    objectives_mask_team1: int
    match_mode: int
    game_mode: int
    match_score: int
    region_mode: int
    compat_version: int | None = Field(None)
    ranked_badge_level: int | None = Field(None)


class APIActiveMatch(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    active_matches: list[ActiveMatch]
