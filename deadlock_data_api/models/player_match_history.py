from citadel_gcmessages_client_pb2 import CMsgClientToGCGetMatchHistoryResponse
from clickhouse_driver import Client
from pydantic import BaseModel, ConfigDict


class PlayerMatchHistoryEntry(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    match_id: int
    hero_id: int
    hero_level: int
    start_time: int
    game_mode: int
    match_mode: int
    player_team: int
    player_kills: int
    player_deaths: int
    player_assists: int
    denies: int
    net_worth: int
    last_hits: int
    team_abandoned: bool
    abandoned_time_s: int
    match_duration_s: int
    match_result: int
    objectives_mask_team0: int
    objectives_mask_team1: int

    @classmethod
    def from_msg(
        cls, msg: CMsgClientToGCGetMatchHistoryResponse.Match
    ) -> "PlayerMatchHistoryEntry":
        return cls(
            abandoned_time_s=msg.abandoned_time_s,
            denies=msg.denies,
            game_mode=msg.game_mode,
            hero_id=msg.hero_id,
            hero_level=msg.hero_level,
            last_hits=msg.last_hits,
            match_duration_s=msg.match_duration_s,
            match_id=msg.match_id,
            match_mode=msg.match_mode,
            match_result=msg.match_result,
            net_worth=msg.net_worth,
            objectives_mask_team0=msg.objectives_mask_team0,
            objectives_mask_team1=msg.objectives_mask_team1,
            player_assists=msg.player_assists,
            player_deaths=msg.player_deaths,
            player_kills=msg.player_kills,
            player_team=msg.player_team,
            start_time=msg.start_time,
            team_abandoned=msg.team_abandoned,
        )

    @staticmethod
    def store_clickhouse(
        client: Client, account_id: int, entries: list["PlayerMatchHistoryEntry"]
    ):
        client.execute(
            f"INSERT INTO player_match_history VALUES",
            [
                (
                    account_id,
                    e.match_id,
                    e.hero_id,
                    e.hero_level,
                    e.start_time,
                    e.game_mode,
                    e.match_mode,
                    e.player_team,
                    e.player_kills,
                    e.player_deaths,
                    e.player_assists,
                    e.denies,
                    e.net_worth,
                    e.last_hits,
                    e.team_abandoned,
                    e.abandoned_time_s,
                    e.match_duration_s,
                    e.match_result,
                    e.objectives_mask_team0,
                    e.objectives_mask_team1,
                )
                for e in entries
            ],
        )
