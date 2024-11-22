from pydantic import BaseModel, ConfigDict
from valveprotos_py.citadel_gcmessages_client_pb2 import CMsgClientToGCGetLeaderboardResponse


class LeaderboardEntry(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    account_name: str
    rank: int

    @classmethod
    def from_msg(
        cls, msg: CMsgClientToGCGetLeaderboardResponse.LeaderboardEntry
    ) -> "LeaderboardEntry":
        return cls(account_name=msg.account_name, rank=msg.rank)


class Leaderboard(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    entries: list[LeaderboardEntry]

    @classmethod
    def from_msg(cls, msg: CMsgClientToGCGetLeaderboardResponse) -> "Leaderboard":
        return cls(entries=[LeaderboardEntry.from_msg(e) for e in msg.entries])
