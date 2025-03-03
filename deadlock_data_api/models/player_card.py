# from clickhouse_driver import Client
# from pydantic import BaseModel, ConfigDict, computed_field
# from valveprotos_py.citadel_gcmessages_client_pb2 import CMsgCitadelProfileCard
#
# from deadlock_data_api import utils
#
#
# class PlayerCardSlotHero(BaseModel):
#     model_config = ConfigDict(populate_by_name=True)
#
#     hero_id: int | None
#     hero_kills: int | None
#     hero_wins: int | None
#
#     @classmethod
#     def from_msg(cls, msg: CMsgCitadelProfileCard.Slot.Hero) -> "PlayerCardSlotHero":
#         return cls(
#             hero_id=msg.hero_id if hasattr(msg, "hero_id") else None,
#             hero_kills=msg.hero_kills if hasattr(msg, "hero_kills") else None,
#             hero_wins=msg.hero_wins if hasattr(msg, "hero_wins") else None,
#         )
#
#
# class PlayerCardSlotStat(BaseModel):
#     model_config = ConfigDict(populate_by_name=True)
#
#     stat_id: int | str | None
#     stat_score: int | None
#
#     @classmethod
#     def from_msg(cls, msg: CMsgCitadelProfileCard.Slot.Stat) -> "PlayerCardSlotStat":
#         return cls(
#             stat_id=msg.stat_id if hasattr(msg, "stat_id") else None,
#             stat_score=msg.stat_score if hasattr(msg, "stat_score") else None,
#         )
#
#
# class PlayerCardSlot(BaseModel):
#     model_config = ConfigDict(populate_by_name=True)
#
#     slot_id: int | None
#     hero: PlayerCardSlotHero | None
#     stat: PlayerCardSlotStat | None
#
#     @classmethod
#     def from_msg(cls, msg: CMsgCitadelProfileCard.Slot) -> "PlayerCardSlot":
#         return cls(
#             slot_id=msg.slot_id if hasattr(msg, "slot_id") else None,
#             hero=(
#                 PlayerCardSlotHero.from_msg(msg.hero) if hasattr(msg, "hero") and msg.hero else None
#             ),
#             stat=(
#                 PlayerCardSlotStat.from_msg(msg.stat) if hasattr(msg, "stat") and msg.stat else None
#             ),
#         )
#
#
# class PlayerCard(BaseModel):
#     model_config = ConfigDict(populate_by_name=True)
#
#     account_id: int
#     ranked_badge_level: int
#     slots: list[PlayerCardSlot]
#
#     @computed_field
#     @property
#     def ranked_rank(self) -> int | None:
#         return self.ranked_badge_level // 10 if self.ranked_badge_level is not None else None
#
#     @computed_field
#     @property
#     def ranked_subrank(self) -> int | None:
#         return self.ranked_badge_level % 10 if self.ranked_badge_level is not None else None
#
#     @classmethod
#     def from_msg(cls, msg: CMsgCitadelProfileCard) -> "PlayerCard":
#         return cls(
#             account_id=msg.account_id,
#             ranked_badge_level=msg.ranked_badge_level,
#             slots=[PlayerCardSlot.from_msg(slot) for slot in msg.slots],
#         )
#
#     def store_clickhouse(self, client: Client, account_id: int):
#         client.execute(
#             "INSERT INTO player_card (* EXCEPT(created_at)) VALUES",
#             [
#                 {
#                     "account_id": account_id,
#                     "ranked_badge_level": self.ranked_badge_level,
#                     "slots_slots_id": [slot.slot_id for slot in self.slots],
#                     "slots_hero_id": [utils.notnone(slot.hero).hero_id for slot in self.slots],
#                     "slots_hero_kills": [
#                         utils.notnone(slot.hero).hero_kills for slot in self.slots
#                     ],
#                     "slots_hero_wins": [utils.notnone(slot.hero).hero_wins for slot in self.slots],
#                     "slots_stat_id": [utils.notnone(slot.stat).stat_id for slot in self.slots],
#                     "slots_stat_score": [
#                         utils.notnone(slot.stat).stat_score for slot in self.slots
#                     ],
#                 }
#             ],
#             types_check=True,
#         )
