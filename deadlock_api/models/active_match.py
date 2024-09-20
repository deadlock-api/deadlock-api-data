from pydantic import BaseModel, ConfigDict, computed_field


class ActiveMatchPlayer(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    account_id: int
    team: int
    abandoned: bool
    hero_id: int


class ActiveMatchObjectives(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    core: bool
    tier1_lane1: bool
    tier1_lane2: bool
    tier1_lane3: bool
    tier1_lane4: bool
    tier2_lane1: bool
    tier2_lane2: bool
    tier2_lane3: bool
    tier2_lane4: bool
    titan: bool
    titan_shield_generator_1: bool
    titan_shield_generator_2: bool
    barrack_boss_lane1: bool
    barrack_boss_lane2: bool
    barrack_boss_lane3: bool
    barrack_boss_lane4: bool

    @classmethod
    def from_mask(cls, mask: int):
        return cls(
            core=bool(mask & (1 << 0)),
            tier1_lane1=bool(mask & (1 << 1)),
            tier1_lane2=bool(mask & (1 << 2)),
            tier1_lane3=bool(mask & (1 << 3)),
            tier1_lane4=bool(mask & (1 << 4)),
            tier2_lane1=bool(mask & (1 << 5)),
            tier2_lane2=bool(mask & (1 << 6)),
            tier2_lane3=bool(mask & (1 << 7)),
            tier2_lane4=bool(mask & (1 << 8)),
            titan=bool(mask & (1 << 9)),
            titan_shield_generator_1=bool(mask & (1 << 10)),
            titan_shield_generator_2=bool(mask & (1 << 11)),
            barrack_boss_lane1=bool(mask & (1 << 12)),
            barrack_boss_lane2=bool(mask & (1 << 13)),
            barrack_boss_lane3=bool(mask & (1 << 14)),
            barrack_boss_lane4=bool(mask & (1 << 15)),
        )


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

    @computed_field
    @property
    def objectives_team0(self) -> ActiveMatchObjectives:
        return ActiveMatchObjectives.from_mask(self.objectives_mask_team0)

    @computed_field
    @property
    def objectives_team1(self) -> ActiveMatchObjectives:
        return ActiveMatchObjectives.from_mask(self.objectives_mask_team1)


class APIActiveMatch(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    active_matches: list[ActiveMatch]
