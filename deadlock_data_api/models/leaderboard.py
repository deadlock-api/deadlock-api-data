from pydantic import BaseModel, ConfigDict, computed_field
from valveprotos_py.citadel_gcmessages_client_pb2 import CMsgClientToGCGetLeaderboardResponse


class LeaderboardEntry(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    account_name: str
    rank: int
    badge_level: int
    top_hero_ids: list[int]

    @computed_field
    @property
    def ranked_rank(self) -> int | None:
        return self.badge_level // 10 if self.badge_level is not None else None

    @computed_field
    @property
    def ranked_subrank(self) -> int | None:
        return self.badge_level % 10 if self.badge_level is not None else None

    @classmethod
    def from_msg(
        cls, msg: CMsgClientToGCGetLeaderboardResponse.LeaderboardEntry
    ) -> "LeaderboardEntry":
        return cls(
            account_name=msg.account_name,
            rank=msg.rank,
            badge_level=msg.badge_level,
            top_hero_ids=msg.top_hero_ids,
        )


class Leaderboard(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    entries: list[LeaderboardEntry]

    @classmethod
    def from_msg(cls, msg: CMsgClientToGCGetLeaderboardResponse) -> "Leaderboard":
        return cls(entries=[LeaderboardEntry.from_msg(e) for e in msg.entries])
