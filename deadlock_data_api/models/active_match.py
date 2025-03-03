# from pydantic import BaseModel, ConfigDict
# from valveprotos_py.citadel_gcmessages_client_pb2 import CMsgDevMatchInfo
#
#
# class ActiveMatchPlayer(BaseModel):
#     model_config = ConfigDict(populate_by_name=True)
#     account_id: int
#     team: int
#     abandoned: bool
#     hero_id: int
#
#
# class ActiveMatch(BaseModel):
#     model_config = ConfigDict(populate_by_name=True)
#
#     start_time: int
#     winning_team: int
#     match_id: int
#     players: list[ActiveMatchPlayer]
#     lobby_id: int
#     net_worth_team_0: int
#     net_worth_team_1: int
#     game_mode_version: int
#     duration_s: int
#     spectators: int
#     open_spectator_slots: int
#     objectives_mask_team0: int
#     objectives_mask_team1: int
#     match_mode: int
#     game_mode: int
#     match_score: int
#     region_mode: int
#
#     @classmethod
#     def from_msg(cls, msg: CMsgDevMatchInfo) -> "ActiveMatch":
#         return cls(
#             start_time=msg.start_time,
#             winning_team=msg.winning_team,
#             match_id=msg.match_id,
#             players=[
#                 ActiveMatchPlayer(
#                     account_id=player.account_id,
#                     team=player.team,
#                     abandoned=player.abandoned,
#                     hero_id=player.hero_id,
#                 )
#                 for player in msg.players
#             ],
#             lobby_id=msg.lobby_id,
#             net_worth_team_0=msg.net_worth_team_0,
#             net_worth_team_1=msg.net_worth_team_1,
#             game_mode_version=msg.game_mode_version,
#             duration_s=msg.duration_s,
#             spectators=msg.spectators,
#             open_spectator_slots=msg.open_spectator_slots,
#             objectives_mask_team0=msg.objectives_mask_team0,
#             objectives_mask_team1=msg.objectives_mask_team1,
#             match_mode=msg.match_mode,
#             game_mode=msg.game_mode,
#             match_score=msg.match_score,
#             region_mode=msg.region_mode,
#         )
#
#
# class APIActiveMatch(BaseModel):
#     model_config = ConfigDict(populate_by_name=True)
#
#     active_matches: list[ActiveMatch]
