from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

import gcsdk_gcmessages_pb2 as _gcsdk_gcmessages_pb2
import steammessages_pb2 as _steammessages_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor
k_ECitadelBotDifficulty_Easy: ECitadelBotDifficulty
k_ECitadelBotDifficulty_Guided: ECitadelBotDifficulty
k_ECitadelBotDifficulty_Hard: ECitadelBotDifficulty
k_ECitadelBotDifficulty_Medium: ECitadelBotDifficulty
k_ECitadelBotDifficulty_Nightmare: ECitadelBotDifficulty
k_ECitadelBotDifficulty_None: ECitadelBotDifficulty
k_ECitadelGameMode_1v1Test: ECitadelGameMode
k_ECitadelGameMode_Invalid: ECitadelGameMode
k_ECitadelGameMode_Normal: ECitadelGameMode
k_ECitadelGameMode_Sandbox: ECitadelGameMode
k_ECitadelLobbyTeam_Spectator: ECitadelLobbyTeam
k_ECitadelLobbyTeam_Team0: ECitadelLobbyTeam
k_ECitadelLobbyTeam_Team1: ECitadelLobbyTeam
k_ECitadelMatchMode_CoopBot: ECitadelMatchMode
k_ECitadelMatchMode_Invalid: ECitadelMatchMode
k_ECitadelMatchMode_PrivateLobby: ECitadelMatchMode
k_ECitadelMatchMode_Ranked: ECitadelMatchMode
k_ECitadelMatchMode_ServerTest: ECitadelMatchMode
k_ECitadelMatchMode_Tutorial: ECitadelMatchMode
k_ECitadelMatchMode_Unranked: ECitadelMatchMode
k_ECitadelRegionMode_Europe: ECitadelRegionMode
k_ECitadelRegionMode_Oceania: ECitadelRegionMode
k_ECitadelRegionMode_ROW: ECitadelRegionMode
k_ECitadelRegionMode_Russia: ECitadelRegionMode
k_ECitadelRegionMode_SAmerica: ECitadelRegionMode
k_ECitadelRegionMode_SEAsia: ECitadelRegionMode
k_ELaneColor_Blue: CMsgLaneColor
k_ELaneColor_Green: CMsgLaneColor
k_ELaneColor_Invalid: CMsgLaneColor
k_ELaneColor_Purple: CMsgLaneColor
k_ELaneColor_Yellow: CMsgLaneColor
k_EMsgAnyToGCReportAsserts: EGCCitadelCommonMessages
k_EMsgAnyToGCReportAssertsResponse: EGCCitadelCommonMessages
k_eBannedFeature_CommsRestricted: EBannedFeature
k_eBannedFeature_Invalid: EBannedFeature
k_eBannedFeature_LowPriorityMatchmaking: EBannedFeature
k_eBannedFeature_ReportingDisabled: EBannedFeature
k_eBronze: ECitadelAccountStatMedal
k_eCitadelObjective_Neutral_Mid: ECitadelObjective
k_eCitadelObjective_Team0_BarrackBoss_Lane1: ECitadelObjective
k_eCitadelObjective_Team0_BarrackBoss_Lane2: ECitadelObjective
k_eCitadelObjective_Team0_BarrackBoss_Lane3: ECitadelObjective
k_eCitadelObjective_Team0_BarrackBoss_Lane4: ECitadelObjective
k_eCitadelObjective_Team0_Core: ECitadelObjective
k_eCitadelObjective_Team0_Tier1_Lane1: ECitadelObjective
k_eCitadelObjective_Team0_Tier1_Lane2: ECitadelObjective
k_eCitadelObjective_Team0_Tier1_Lane3: ECitadelObjective
k_eCitadelObjective_Team0_Tier1_Lane4: ECitadelObjective
k_eCitadelObjective_Team0_Tier2_Lane1: ECitadelObjective
k_eCitadelObjective_Team0_Tier2_Lane2: ECitadelObjective
k_eCitadelObjective_Team0_Tier2_Lane3: ECitadelObjective
k_eCitadelObjective_Team0_Tier2_Lane4: ECitadelObjective
k_eCitadelObjective_Team0_Titan: ECitadelObjective
k_eCitadelObjective_Team0_TitanShieldGenerator_1: ECitadelObjective
k_eCitadelObjective_Team0_TitanShieldGenerator_2: ECitadelObjective
k_eCitadelObjective_Team1_BarrackBoss_Lane1: ECitadelObjective
k_eCitadelObjective_Team1_BarrackBoss_Lane2: ECitadelObjective
k_eCitadelObjective_Team1_BarrackBoss_Lane3: ECitadelObjective
k_eCitadelObjective_Team1_BarrackBoss_Lane4: ECitadelObjective
k_eCitadelObjective_Team1_Core: ECitadelObjective
k_eCitadelObjective_Team1_Tier1_Lane1: ECitadelObjective
k_eCitadelObjective_Team1_Tier1_Lane2: ECitadelObjective
k_eCitadelObjective_Team1_Tier1_Lane3: ECitadelObjective
k_eCitadelObjective_Team1_Tier1_Lane4: ECitadelObjective
k_eCitadelObjective_Team1_Tier2_Lane1: ECitadelObjective
k_eCitadelObjective_Team1_Tier2_Lane2: ECitadelObjective
k_eCitadelObjective_Team1_Tier2_Lane3: ECitadelObjective
k_eCitadelObjective_Team1_Tier2_Lane4: ECitadelObjective
k_eCitadelObjective_Team1_Titan: ECitadelObjective
k_eCitadelObjective_Team1_TitanShieldGenerator_1: ECitadelObjective
k_eCitadelObjective_Team1_TitanShieldGenerator_2: ECitadelObjective
k_eCitadelTeamObjective_BarrackBoss_Lane1: ECitadelTeamObjective
k_eCitadelTeamObjective_BarrackBoss_Lane2: ECitadelTeamObjective
k_eCitadelTeamObjective_BarrackBoss_Lane3: ECitadelTeamObjective
k_eCitadelTeamObjective_BarrackBoss_Lane4: ECitadelTeamObjective
k_eCitadelTeamObjective_Core: ECitadelTeamObjective
k_eCitadelTeamObjective_Tier1_Lane1: ECitadelTeamObjective
k_eCitadelTeamObjective_Tier1_Lane2: ECitadelTeamObjective
k_eCitadelTeamObjective_Tier1_Lane3: ECitadelTeamObjective
k_eCitadelTeamObjective_Tier1_Lane4: ECitadelTeamObjective
k_eCitadelTeamObjective_Tier2_Lane1: ECitadelTeamObjective
k_eCitadelTeamObjective_Tier2_Lane2: ECitadelTeamObjective
k_eCitadelTeamObjective_Tier2_Lane3: ECitadelTeamObjective
k_eCitadelTeamObjective_Tier2_Lane4: ECitadelTeamObjective
k_eCitadelTeamObjective_Titan: ECitadelTeamObjective
k_eCitadelTeamObjective_TitanShieldGenerator_1: ECitadelTeamObjective
k_eCitadelTeamObjective_TitanShieldGenerator_2: ECitadelTeamObjective
k_eFeatureBanReason_DevCommand: EFeatureBanReason
k_eFeatureBanReason_ExcessivePlayerReports: EFeatureBanReason
k_eFeatureBanReason_Invalid: EFeatureBanReason
k_eFeatureBanReason_MatchAbandons: EFeatureBanReason
k_eFeatureBanReason_PlayerReports: EFeatureBanReason
k_eGold: ECitadelAccountStatMedal
k_eLobbyServerState_Abandoned: ELobbyServerState
k_eLobbyServerState_Assign: ELobbyServerState
k_eLobbyServerState_InGame: ELobbyServerState
k_eLobbyServerState_PostMatch: ELobbyServerState
k_eLobbyServerState_SignedOut: ELobbyServerState
k_eNone: ECitadelAccountStatMedal
k_eSilver: ECitadelAccountStatMedal

class CLobbyData_PostMatchSurvey(_message.Message):
    __slots__ = ["surveys"]

    class PlayerSurvey(_message.Message):
        __slots__ = ["account_id", "question_id"]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
        account_id: int
        question_id: int
        def __init__(
            self, account_id: _Optional[int] = ..., question_id: _Optional[int] = ...
        ) -> None: ...

    SURVEYS_FIELD_NUMBER: _ClassVar[int]
    surveys: _containers.RepeatedCompositeFieldContainer[
        CLobbyData_PostMatchSurvey.PlayerSurvey
    ]
    def __init__(
        self,
        surveys: _Optional[
            _Iterable[_Union[CLobbyData_PostMatchSurvey.PlayerSurvey, _Mapping]]
        ] = ...,
    ) -> None: ...

class CMsgAccountBookStats(_message.Message):
    __slots__ = ["book_id", "book_max_xp", "book_xp"]
    BOOK_ID_FIELD_NUMBER: _ClassVar[int]
    BOOK_MAX_XP_FIELD_NUMBER: _ClassVar[int]
    BOOK_XP_FIELD_NUMBER: _ClassVar[int]
    book_id: int
    book_max_xp: int
    book_xp: int
    def __init__(
        self,
        book_id: _Optional[int] = ...,
        book_xp: _Optional[int] = ...,
        book_max_xp: _Optional[int] = ...,
    ) -> None: ...

class CMsgAccountHeroStats(_message.Message):
    __slots__ = [
        "hero_id",
        "medals_bronze",
        "medals_gold",
        "medals_silver",
        "stat_id",
        "total_value",
    ]
    HERO_ID_FIELD_NUMBER: _ClassVar[int]
    MEDALS_BRONZE_FIELD_NUMBER: _ClassVar[int]
    MEDALS_GOLD_FIELD_NUMBER: _ClassVar[int]
    MEDALS_SILVER_FIELD_NUMBER: _ClassVar[int]
    STAT_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    hero_id: int
    medals_bronze: _containers.RepeatedScalarFieldContainer[int]
    medals_gold: _containers.RepeatedScalarFieldContainer[int]
    medals_silver: _containers.RepeatedScalarFieldContainer[int]
    stat_id: _containers.RepeatedScalarFieldContainer[int]
    total_value: _containers.RepeatedScalarFieldContainer[int]
    def __init__(
        self,
        hero_id: _Optional[int] = ...,
        stat_id: _Optional[_Iterable[int]] = ...,
        total_value: _Optional[_Iterable[int]] = ...,
        medals_bronze: _Optional[_Iterable[int]] = ...,
        medals_silver: _Optional[_Iterable[int]] = ...,
        medals_gold: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class CMsgAccountStats(_message.Message):
    __slots__ = ["account_id", "stats"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    stats: _containers.RepeatedCompositeFieldContainer[CMsgAccountHeroStats]
    def __init__(
        self,
        account_id: _Optional[int] = ...,
        stats: _Optional[_Iterable[_Union[CMsgAccountHeroStats, _Mapping]]] = ...,
    ) -> None: ...

class CMsgAnyToGCReportAsserts(_message.Message):
    __slots__ = ["asserts", "version"]

    class TrackedAssert(_message.Message):
        __slots__ = [
            "condition",
            "filename",
            "function_name",
            "line_number",
            "sample_msg",
            "sample_stack",
            "times_fired",
            "total_times_fired",
        ]
        CONDITION_FIELD_NUMBER: _ClassVar[int]
        FILENAME_FIELD_NUMBER: _ClassVar[int]
        FUNCTION_NAME_FIELD_NUMBER: _ClassVar[int]
        LINE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        SAMPLE_MSG_FIELD_NUMBER: _ClassVar[int]
        SAMPLE_STACK_FIELD_NUMBER: _ClassVar[int]
        TIMES_FIRED_FIELD_NUMBER: _ClassVar[int]
        TOTAL_TIMES_FIRED_FIELD_NUMBER: _ClassVar[int]
        condition: str
        filename: str
        function_name: str
        line_number: int
        sample_msg: str
        sample_stack: str
        times_fired: int
        total_times_fired: int
        def __init__(
            self,
            filename: _Optional[str] = ...,
            line_number: _Optional[int] = ...,
            sample_msg: _Optional[str] = ...,
            sample_stack: _Optional[str] = ...,
            times_fired: _Optional[int] = ...,
            function_name: _Optional[str] = ...,
            condition: _Optional[str] = ...,
            total_times_fired: _Optional[int] = ...,
        ) -> None: ...

    ASSERTS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    asserts: _containers.RepeatedCompositeFieldContainer[
        CMsgAnyToGCReportAsserts.TrackedAssert
    ]
    version: int
    def __init__(
        self,
        version: _Optional[int] = ...,
        asserts: _Optional[
            _Iterable[_Union[CMsgAnyToGCReportAsserts.TrackedAssert, _Mapping]]
        ] = ...,
    ) -> None: ...

class CMsgAnyToGCReportAssertsResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class CMsgGCAccountData(_message.Message):
    __slots__ = ["account_id", "cheater_report_score"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CHEATER_REPORT_SCORE_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    cheater_report_score: float
    def __init__(
        self,
        account_id: _Optional[int] = ...,
        cheater_report_score: _Optional[float] = ...,
    ) -> None: ...

class CMsgHeroSelectionMatchInfo(_message.Message):
    __slots__ = ["hero_selections"]

    class Hero(_message.Message):
        __slots__ = ["hero_id", "priority"]
        HERO_ID_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_FIELD_NUMBER: _ClassVar[int]
        hero_id: int
        priority: int
        def __init__(
            self, hero_id: _Optional[int] = ..., priority: _Optional[int] = ...
        ) -> None: ...

    HERO_SELECTIONS_FIELD_NUMBER: _ClassVar[int]
    hero_selections: _containers.RepeatedCompositeFieldContainer[
        CMsgHeroSelectionMatchInfo.Hero
    ]
    def __init__(
        self,
        hero_selections: _Optional[
            _Iterable[_Union[CMsgHeroSelectionMatchInfo.Hero, _Mapping]]
        ] = ...,
    ) -> None: ...

class CMsgMapLine(_message.Message):
    __slots__ = ["initial", "x", "y"]
    INITIAL_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    initial: bool
    x: int
    y: int
    def __init__(
        self, x: _Optional[int] = ..., y: _Optional[int] = ..., initial: bool = ...
    ) -> None: ...

class CMsgMatchMetaData(_message.Message):
    __slots__ = ["match_details", "match_id", "version"]
    MATCH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    match_details: bytes
    match_id: int
    version: int
    def __init__(
        self,
        version: _Optional[int] = ...,
        match_details: _Optional[bytes] = ...,
        match_id: _Optional[int] = ...,
    ) -> None: ...

class CMsgMatchMetaDataContents(_message.Message):
    __slots__ = ["match_info"]

    class EGoldSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    class EMatchOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    class AbilityStat(_message.Message):
        __slots__ = ["ability_id", "ability_value"]
        ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
        ABILITY_VALUE_FIELD_NUMBER: _ClassVar[int]
        ability_id: int
        ability_value: int
        def __init__(
            self, ability_id: _Optional[int] = ..., ability_value: _Optional[int] = ...
        ) -> None: ...

    class BookReward(_message.Message):
        __slots__ = ["book_id", "starting_xp", "xp_amount"]
        BOOK_ID_FIELD_NUMBER: _ClassVar[int]
        STARTING_XP_FIELD_NUMBER: _ClassVar[int]
        XP_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        book_id: int
        starting_xp: int
        xp_amount: int
        def __init__(
            self,
            book_id: _Optional[int] = ...,
            xp_amount: _Optional[int] = ...,
            starting_xp: _Optional[int] = ...,
        ) -> None: ...

    class CustomUserStat(_message.Message):
        __slots__ = ["id", "value"]
        ID_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        id: int
        value: int
        def __init__(
            self, value: _Optional[int] = ..., id: _Optional[int] = ...
        ) -> None: ...

    class CustomUserStatInfo(_message.Message):
        __slots__ = ["id", "name"]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        id: int
        name: str
        def __init__(
            self, name: _Optional[str] = ..., id: _Optional[int] = ...
        ) -> None: ...

    class Deaths(_message.Message):
        __slots__ = [
            "death_duration_s",
            "death_pos",
            "game_time_s",
            "killer_player_slot",
            "killer_pos",
        ]
        DEATH_DURATION_S_FIELD_NUMBER: _ClassVar[int]
        DEATH_POS_FIELD_NUMBER: _ClassVar[int]
        GAME_TIME_S_FIELD_NUMBER: _ClassVar[int]
        KILLER_PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
        KILLER_POS_FIELD_NUMBER: _ClassVar[int]
        death_duration_s: int
        death_pos: CMsgMatchMetaDataContents.Position
        game_time_s: int
        killer_player_slot: int
        killer_pos: CMsgMatchMetaDataContents.Position
        def __init__(
            self,
            game_time_s: _Optional[int] = ...,
            killer_player_slot: _Optional[int] = ...,
            death_pos: _Optional[
                _Union[CMsgMatchMetaDataContents.Position, _Mapping]
            ] = ...,
            killer_pos: _Optional[
                _Union[CMsgMatchMetaDataContents.Position, _Mapping]
            ] = ...,
            death_duration_s: _Optional[int] = ...,
        ) -> None: ...

    class GoldSource(_message.Message):
        __slots__ = ["damage", "gold", "gold_orbs", "kills", "source"]
        DAMAGE_FIELD_NUMBER: _ClassVar[int]
        GOLD_FIELD_NUMBER: _ClassVar[int]
        GOLD_ORBS_FIELD_NUMBER: _ClassVar[int]
        KILLS_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        damage: int
        gold: int
        gold_orbs: int
        kills: int
        source: CMsgMatchMetaDataContents.EGoldSource
        def __init__(
            self,
            source: _Optional[_Union[CMsgMatchMetaDataContents.EGoldSource, str]] = ...,
            kills: _Optional[int] = ...,
            damage: _Optional[int] = ...,
            gold: _Optional[int] = ...,
            gold_orbs: _Optional[int] = ...,
        ) -> None: ...

    class Items(_message.Message):
        __slots__ = [
            "flags",
            "game_time_s",
            "imbued_ability_id",
            "item_id",
            "sold_time_s",
            "upgrade_id",
        ]
        FLAGS_FIELD_NUMBER: _ClassVar[int]
        GAME_TIME_S_FIELD_NUMBER: _ClassVar[int]
        IMBUED_ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
        ITEM_ID_FIELD_NUMBER: _ClassVar[int]
        SOLD_TIME_S_FIELD_NUMBER: _ClassVar[int]
        UPGRADE_ID_FIELD_NUMBER: _ClassVar[int]
        flags: int
        game_time_s: int
        imbued_ability_id: int
        item_id: int
        sold_time_s: int
        upgrade_id: int
        def __init__(
            self,
            game_time_s: _Optional[int] = ...,
            item_id: _Optional[int] = ...,
            upgrade_id: _Optional[int] = ...,
            sold_time_s: _Optional[int] = ...,
            flags: _Optional[int] = ...,
            imbued_ability_id: _Optional[int] = ...,
        ) -> None: ...

    class MatchInfo(_message.Message):
        __slots__ = [
            "custom_user_stats",
            "damage_matrix",
            "duration_s",
            "game_mode",
            "legacy_objectives_mask",
            "match_id",
            "match_mode",
            "match_outcome",
            "match_paths",
            "match_pauses",
            "mid_boss",
            "objectives",
            "objectives_mask_team0",
            "objectives_mask_team1",
            "players",
            "start_time",
            "watched_death_replays",
            "winning_team",
        ]
        CUSTOM_USER_STATS_FIELD_NUMBER: _ClassVar[int]
        DAMAGE_MATRIX_FIELD_NUMBER: _ClassVar[int]
        DURATION_S_FIELD_NUMBER: _ClassVar[int]
        GAME_MODE_FIELD_NUMBER: _ClassVar[int]
        LEGACY_OBJECTIVES_MASK_FIELD_NUMBER: _ClassVar[int]
        MATCH_ID_FIELD_NUMBER: _ClassVar[int]
        MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
        MATCH_OUTCOME_FIELD_NUMBER: _ClassVar[int]
        MATCH_PATHS_FIELD_NUMBER: _ClassVar[int]
        MATCH_PAUSES_FIELD_NUMBER: _ClassVar[int]
        MID_BOSS_FIELD_NUMBER: _ClassVar[int]
        OBJECTIVES_FIELD_NUMBER: _ClassVar[int]
        OBJECTIVES_MASK_TEAM0_FIELD_NUMBER: _ClassVar[int]
        OBJECTIVES_MASK_TEAM1_FIELD_NUMBER: _ClassVar[int]
        PLAYERS_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        WATCHED_DEATH_REPLAYS_FIELD_NUMBER: _ClassVar[int]
        WINNING_TEAM_FIELD_NUMBER: _ClassVar[int]
        custom_user_stats: _containers.RepeatedCompositeFieldContainer[
            CMsgMatchMetaDataContents.CustomUserStatInfo
        ]
        damage_matrix: CMsgMatchPlayerDamageMatrix
        duration_s: int
        game_mode: ECitadelGameMode
        legacy_objectives_mask: int
        match_id: int
        match_mode: ECitadelMatchMode
        match_outcome: CMsgMatchMetaDataContents.EMatchOutcome
        match_paths: CMsgMatchPlayerPathsData
        match_pauses: _containers.RepeatedCompositeFieldContainer[
            CMsgMatchMetaDataContents.Pause
        ]
        mid_boss: _containers.RepeatedCompositeFieldContainer[
            CMsgMatchMetaDataContents.MidBoss
        ]
        objectives: _containers.RepeatedCompositeFieldContainer[
            CMsgMatchMetaDataContents.Objective
        ]
        objectives_mask_team0: int
        objectives_mask_team1: int
        players: _containers.RepeatedCompositeFieldContainer[
            CMsgMatchMetaDataContents.Players
        ]
        start_time: int
        watched_death_replays: _containers.RepeatedCompositeFieldContainer[
            CMsgMatchMetaDataContents.WatchedDeathReplay
        ]
        winning_team: ECitadelLobbyTeam
        def __init__(
            self,
            duration_s: _Optional[int] = ...,
            match_outcome: _Optional[
                _Union[CMsgMatchMetaDataContents.EMatchOutcome, str]
            ] = ...,
            winning_team: _Optional[_Union[ECitadelLobbyTeam, str]] = ...,
            players: _Optional[
                _Iterable[_Union[CMsgMatchMetaDataContents.Players, _Mapping]]
            ] = ...,
            start_time: _Optional[int] = ...,
            match_id: _Optional[int] = ...,
            legacy_objectives_mask: _Optional[int] = ...,
            game_mode: _Optional[_Union[ECitadelGameMode, str]] = ...,
            match_mode: _Optional[_Union[ECitadelMatchMode, str]] = ...,
            objectives: _Optional[
                _Iterable[_Union[CMsgMatchMetaDataContents.Objective, _Mapping]]
            ] = ...,
            match_paths: _Optional[_Union[CMsgMatchPlayerPathsData, _Mapping]] = ...,
            damage_matrix: _Optional[
                _Union[CMsgMatchPlayerDamageMatrix, _Mapping]
            ] = ...,
            match_pauses: _Optional[
                _Iterable[_Union[CMsgMatchMetaDataContents.Pause, _Mapping]]
            ] = ...,
            custom_user_stats: _Optional[
                _Iterable[
                    _Union[CMsgMatchMetaDataContents.CustomUserStatInfo, _Mapping]
                ]
            ] = ...,
            watched_death_replays: _Optional[
                _Iterable[
                    _Union[CMsgMatchMetaDataContents.WatchedDeathReplay, _Mapping]
                ]
            ] = ...,
            objectives_mask_team0: _Optional[int] = ...,
            objectives_mask_team1: _Optional[int] = ...,
            mid_boss: _Optional[
                _Iterable[_Union[CMsgMatchMetaDataContents.MidBoss, _Mapping]]
            ] = ...,
        ) -> None: ...

    class MidBoss(_message.Message):
        __slots__ = ["destroyed_time_s", "team_claimed", "team_killed"]
        DESTROYED_TIME_S_FIELD_NUMBER: _ClassVar[int]
        TEAM_CLAIMED_FIELD_NUMBER: _ClassVar[int]
        TEAM_KILLED_FIELD_NUMBER: _ClassVar[int]
        destroyed_time_s: int
        team_claimed: ECitadelLobbyTeam
        team_killed: ECitadelLobbyTeam
        def __init__(
            self,
            team_killed: _Optional[_Union[ECitadelLobbyTeam, str]] = ...,
            team_claimed: _Optional[_Union[ECitadelLobbyTeam, str]] = ...,
            destroyed_time_s: _Optional[int] = ...,
        ) -> None: ...

    class Objective(_message.Message):
        __slots__ = [
            "creep_damage",
            "creep_damage_mitigated",
            "destroyed_time_s",
            "first_damage_time_s",
            "legacy_objective_id",
            "player_damage",
            "player_damage_mitigated",
            "team",
            "team_objective_id",
        ]
        CREEP_DAMAGE_FIELD_NUMBER: _ClassVar[int]
        CREEP_DAMAGE_MITIGATED_FIELD_NUMBER: _ClassVar[int]
        DESTROYED_TIME_S_FIELD_NUMBER: _ClassVar[int]
        FIRST_DAMAGE_TIME_S_FIELD_NUMBER: _ClassVar[int]
        LEGACY_OBJECTIVE_ID_FIELD_NUMBER: _ClassVar[int]
        PLAYER_DAMAGE_FIELD_NUMBER: _ClassVar[int]
        PLAYER_DAMAGE_MITIGATED_FIELD_NUMBER: _ClassVar[int]
        TEAM_FIELD_NUMBER: _ClassVar[int]
        TEAM_OBJECTIVE_ID_FIELD_NUMBER: _ClassVar[int]
        creep_damage: int
        creep_damage_mitigated: int
        destroyed_time_s: int
        first_damage_time_s: int
        legacy_objective_id: ECitadelObjective
        player_damage: int
        player_damage_mitigated: int
        team: ECitadelLobbyTeam
        team_objective_id: ECitadelTeamObjective
        def __init__(
            self,
            legacy_objective_id: _Optional[_Union[ECitadelObjective, str]] = ...,
            destroyed_time_s: _Optional[int] = ...,
            creep_damage: _Optional[int] = ...,
            creep_damage_mitigated: _Optional[int] = ...,
            player_damage: _Optional[int] = ...,
            player_damage_mitigated: _Optional[int] = ...,
            first_damage_time_s: _Optional[int] = ...,
            team_objective_id: _Optional[_Union[ECitadelTeamObjective, str]] = ...,
            team: _Optional[_Union[ECitadelLobbyTeam, str]] = ...,
        ) -> None: ...

    class Pause(_message.Message):
        __slots__ = ["game_time_s", "pause_duration_s", "player_slot"]
        GAME_TIME_S_FIELD_NUMBER: _ClassVar[int]
        PAUSE_DURATION_S_FIELD_NUMBER: _ClassVar[int]
        PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
        game_time_s: int
        pause_duration_s: int
        player_slot: int
        def __init__(
            self,
            game_time_s: _Optional[int] = ...,
            pause_duration_s: _Optional[int] = ...,
            player_slot: _Optional[int] = ...,
        ) -> None: ...

    class Ping(_message.Message):
        __slots__ = ["game_time_s", "ping_data", "ping_type"]
        GAME_TIME_S_FIELD_NUMBER: _ClassVar[int]
        PING_DATA_FIELD_NUMBER: _ClassVar[int]
        PING_TYPE_FIELD_NUMBER: _ClassVar[int]
        game_time_s: int
        ping_data: int
        ping_type: int
        def __init__(
            self,
            ping_type: _Optional[int] = ...,
            ping_data: _Optional[int] = ...,
            game_time_s: _Optional[int] = ...,
        ) -> None: ...

    class PlayerStats(_message.Message):
        __slots__ = [
            "ability_points",
            "absorption_provided",
            "assists",
            "boss_damage",
            "creep_damage",
            "creep_kills",
            "custom_user_stats",
            "damage_absorbed",
            "damage_mitigated",
            "deaths",
            "denies",
            "gold_boss",
            "gold_boss_orb",
            "gold_death_loss",
            "gold_denied",
            "gold_lane_creep",
            "gold_lane_creep_orbs",
            "gold_neutral_creep",
            "gold_neutral_creep_orbs",
            "gold_player",
            "gold_player_orbs",
            "gold_sources",
            "gold_treasure",
            "heal_lost",
            "heal_prevented",
            "hero_bullets_hit",
            "hero_bullets_hit_crit",
            "kills",
            "level",
            "max_health",
            "net_worth",
            "neutral_damage",
            "neutral_kills",
            "player_damage",
            "player_damage_taken",
            "player_healing",
            "possible_creeps",
            "self_healing",
            "shots_hit",
            "shots_missed",
            "tech_power",
            "time_stamp_s",
            "weapon_power",
        ]
        ABILITY_POINTS_FIELD_NUMBER: _ClassVar[int]
        ABSORPTION_PROVIDED_FIELD_NUMBER: _ClassVar[int]
        ASSISTS_FIELD_NUMBER: _ClassVar[int]
        BOSS_DAMAGE_FIELD_NUMBER: _ClassVar[int]
        CREEP_DAMAGE_FIELD_NUMBER: _ClassVar[int]
        CREEP_KILLS_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_USER_STATS_FIELD_NUMBER: _ClassVar[int]
        DAMAGE_ABSORBED_FIELD_NUMBER: _ClassVar[int]
        DAMAGE_MITIGATED_FIELD_NUMBER: _ClassVar[int]
        DEATHS_FIELD_NUMBER: _ClassVar[int]
        DENIES_FIELD_NUMBER: _ClassVar[int]
        GOLD_BOSS_FIELD_NUMBER: _ClassVar[int]
        GOLD_BOSS_ORB_FIELD_NUMBER: _ClassVar[int]
        GOLD_DEATH_LOSS_FIELD_NUMBER: _ClassVar[int]
        GOLD_DENIED_FIELD_NUMBER: _ClassVar[int]
        GOLD_LANE_CREEP_FIELD_NUMBER: _ClassVar[int]
        GOLD_LANE_CREEP_ORBS_FIELD_NUMBER: _ClassVar[int]
        GOLD_NEUTRAL_CREEP_FIELD_NUMBER: _ClassVar[int]
        GOLD_NEUTRAL_CREEP_ORBS_FIELD_NUMBER: _ClassVar[int]
        GOLD_PLAYER_FIELD_NUMBER: _ClassVar[int]
        GOLD_PLAYER_ORBS_FIELD_NUMBER: _ClassVar[int]
        GOLD_SOURCES_FIELD_NUMBER: _ClassVar[int]
        GOLD_TREASURE_FIELD_NUMBER: _ClassVar[int]
        HEAL_LOST_FIELD_NUMBER: _ClassVar[int]
        HEAL_PREVENTED_FIELD_NUMBER: _ClassVar[int]
        HERO_BULLETS_HIT_CRIT_FIELD_NUMBER: _ClassVar[int]
        HERO_BULLETS_HIT_FIELD_NUMBER: _ClassVar[int]
        KILLS_FIELD_NUMBER: _ClassVar[int]
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        MAX_HEALTH_FIELD_NUMBER: _ClassVar[int]
        NET_WORTH_FIELD_NUMBER: _ClassVar[int]
        NEUTRAL_DAMAGE_FIELD_NUMBER: _ClassVar[int]
        NEUTRAL_KILLS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_DAMAGE_FIELD_NUMBER: _ClassVar[int]
        PLAYER_DAMAGE_TAKEN_FIELD_NUMBER: _ClassVar[int]
        PLAYER_HEALING_FIELD_NUMBER: _ClassVar[int]
        POSSIBLE_CREEPS_FIELD_NUMBER: _ClassVar[int]
        SELF_HEALING_FIELD_NUMBER: _ClassVar[int]
        SHOTS_HIT_FIELD_NUMBER: _ClassVar[int]
        SHOTS_MISSED_FIELD_NUMBER: _ClassVar[int]
        TECH_POWER_FIELD_NUMBER: _ClassVar[int]
        TIME_STAMP_S_FIELD_NUMBER: _ClassVar[int]
        WEAPON_POWER_FIELD_NUMBER: _ClassVar[int]
        ability_points: int
        absorption_provided: int
        assists: int
        boss_damage: int
        creep_damage: int
        creep_kills: int
        custom_user_stats: _containers.RepeatedCompositeFieldContainer[
            CMsgMatchMetaDataContents.CustomUserStat
        ]
        damage_absorbed: int
        damage_mitigated: int
        deaths: int
        denies: int
        gold_boss: int
        gold_boss_orb: int
        gold_death_loss: int
        gold_denied: int
        gold_lane_creep: int
        gold_lane_creep_orbs: int
        gold_neutral_creep: int
        gold_neutral_creep_orbs: int
        gold_player: int
        gold_player_orbs: int
        gold_sources: _containers.RepeatedCompositeFieldContainer[
            CMsgMatchMetaDataContents.GoldSource
        ]
        gold_treasure: int
        heal_lost: int
        heal_prevented: int
        hero_bullets_hit: int
        hero_bullets_hit_crit: int
        kills: int
        level: int
        max_health: int
        net_worth: int
        neutral_damage: int
        neutral_kills: int
        player_damage: int
        player_damage_taken: int
        player_healing: int
        possible_creeps: int
        self_healing: int
        shots_hit: int
        shots_missed: int
        tech_power: int
        time_stamp_s: int
        weapon_power: int
        def __init__(
            self,
            time_stamp_s: _Optional[int] = ...,
            net_worth: _Optional[int] = ...,
            gold_player: _Optional[int] = ...,
            gold_player_orbs: _Optional[int] = ...,
            gold_lane_creep_orbs: _Optional[int] = ...,
            gold_neutral_creep_orbs: _Optional[int] = ...,
            gold_boss: _Optional[int] = ...,
            gold_boss_orb: _Optional[int] = ...,
            gold_treasure: _Optional[int] = ...,
            gold_denied: _Optional[int] = ...,
            gold_death_loss: _Optional[int] = ...,
            gold_lane_creep: _Optional[int] = ...,
            gold_neutral_creep: _Optional[int] = ...,
            kills: _Optional[int] = ...,
            deaths: _Optional[int] = ...,
            assists: _Optional[int] = ...,
            creep_kills: _Optional[int] = ...,
            neutral_kills: _Optional[int] = ...,
            possible_creeps: _Optional[int] = ...,
            creep_damage: _Optional[int] = ...,
            player_damage: _Optional[int] = ...,
            neutral_damage: _Optional[int] = ...,
            boss_damage: _Optional[int] = ...,
            denies: _Optional[int] = ...,
            player_healing: _Optional[int] = ...,
            ability_points: _Optional[int] = ...,
            self_healing: _Optional[int] = ...,
            player_damage_taken: _Optional[int] = ...,
            max_health: _Optional[int] = ...,
            weapon_power: _Optional[int] = ...,
            tech_power: _Optional[int] = ...,
            shots_hit: _Optional[int] = ...,
            shots_missed: _Optional[int] = ...,
            damage_absorbed: _Optional[int] = ...,
            absorption_provided: _Optional[int] = ...,
            hero_bullets_hit: _Optional[int] = ...,
            hero_bullets_hit_crit: _Optional[int] = ...,
            heal_prevented: _Optional[int] = ...,
            heal_lost: _Optional[int] = ...,
            gold_sources: _Optional[
                _Iterable[_Union[CMsgMatchMetaDataContents.GoldSource, _Mapping]]
            ] = ...,
            custom_user_stats: _Optional[
                _Iterable[_Union[CMsgMatchMetaDataContents.CustomUserStat, _Mapping]]
            ] = ...,
            damage_mitigated: _Optional[int] = ...,
            level: _Optional[int] = ...,
        ) -> None: ...

    class Players(_message.Message):
        __slots__ = [
            "abandon_match_time_s",
            "ability_points",
            "ability_stats",
            "account_id",
            "assigned_lane",
            "assists",
            "book_rewards",
            "death_details",
            "deaths",
            "denies",
            "hero_id",
            "items",
            "kills",
            "last_hits",
            "level",
            "net_worth",
            "party",
            "pings",
            "player_slot",
            "ranked_badge_detail",
            "ranked_badge_level",
            "stats",
            "stats_type_stat",
            "team",
        ]
        ABANDON_MATCH_TIME_S_FIELD_NUMBER: _ClassVar[int]
        ABILITY_POINTS_FIELD_NUMBER: _ClassVar[int]
        ABILITY_STATS_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        ASSIGNED_LANE_FIELD_NUMBER: _ClassVar[int]
        ASSISTS_FIELD_NUMBER: _ClassVar[int]
        BOOK_REWARDS_FIELD_NUMBER: _ClassVar[int]
        DEATHS_FIELD_NUMBER: _ClassVar[int]
        DEATH_DETAILS_FIELD_NUMBER: _ClassVar[int]
        DENIES_FIELD_NUMBER: _ClassVar[int]
        HERO_ID_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        KILLS_FIELD_NUMBER: _ClassVar[int]
        LAST_HITS_FIELD_NUMBER: _ClassVar[int]
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        NET_WORTH_FIELD_NUMBER: _ClassVar[int]
        PARTY_FIELD_NUMBER: _ClassVar[int]
        PINGS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
        RANKED_BADGE_DETAIL_FIELD_NUMBER: _ClassVar[int]
        RANKED_BADGE_LEVEL_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        STATS_TYPE_STAT_FIELD_NUMBER: _ClassVar[int]
        TEAM_FIELD_NUMBER: _ClassVar[int]
        abandon_match_time_s: int
        ability_points: int
        ability_stats: _containers.RepeatedCompositeFieldContainer[
            CMsgMatchMetaDataContents.AbilityStat
        ]
        account_id: int
        assigned_lane: int
        assists: int
        book_rewards: _containers.RepeatedCompositeFieldContainer[
            CMsgMatchMetaDataContents.BookReward
        ]
        death_details: _containers.RepeatedCompositeFieldContainer[
            CMsgMatchMetaDataContents.Deaths
        ]
        deaths: int
        denies: int
        hero_id: int
        items: _containers.RepeatedCompositeFieldContainer[
            CMsgMatchMetaDataContents.Items
        ]
        kills: int
        last_hits: int
        level: int
        net_worth: int
        party: int
        pings: _containers.RepeatedCompositeFieldContainer[
            CMsgMatchMetaDataContents.Ping
        ]
        player_slot: int
        ranked_badge_detail: int
        ranked_badge_level: int
        stats: _containers.RepeatedCompositeFieldContainer[
            CMsgMatchMetaDataContents.PlayerStats
        ]
        stats_type_stat: _containers.RepeatedScalarFieldContainer[float]
        team: ECitadelLobbyTeam
        def __init__(
            self,
            account_id: _Optional[int] = ...,
            player_slot: _Optional[int] = ...,
            death_details: _Optional[
                _Iterable[_Union[CMsgMatchMetaDataContents.Deaths, _Mapping]]
            ] = ...,
            items: _Optional[
                _Iterable[_Union[CMsgMatchMetaDataContents.Items, _Mapping]]
            ] = ...,
            stats: _Optional[
                _Iterable[_Union[CMsgMatchMetaDataContents.PlayerStats, _Mapping]]
            ] = ...,
            team: _Optional[_Union[ECitadelLobbyTeam, str]] = ...,
            kills: _Optional[int] = ...,
            deaths: _Optional[int] = ...,
            assists: _Optional[int] = ...,
            net_worth: _Optional[int] = ...,
            hero_id: _Optional[int] = ...,
            last_hits: _Optional[int] = ...,
            denies: _Optional[int] = ...,
            ability_points: _Optional[int] = ...,
            party: _Optional[int] = ...,
            assigned_lane: _Optional[int] = ...,
            level: _Optional[int] = ...,
            pings: _Optional[
                _Iterable[_Union[CMsgMatchMetaDataContents.Ping, _Mapping]]
            ] = ...,
            ability_stats: _Optional[
                _Iterable[_Union[CMsgMatchMetaDataContents.AbilityStat, _Mapping]]
            ] = ...,
            stats_type_stat: _Optional[_Iterable[float]] = ...,
            book_rewards: _Optional[
                _Iterable[_Union[CMsgMatchMetaDataContents.BookReward, _Mapping]]
            ] = ...,
            abandon_match_time_s: _Optional[int] = ...,
            ranked_badge_level: _Optional[int] = ...,
            ranked_badge_detail: _Optional[int] = ...,
        ) -> None: ...

    class Position(_message.Message):
        __slots__ = ["x", "y", "z"]
        X_FIELD_NUMBER: _ClassVar[int]
        Y_FIELD_NUMBER: _ClassVar[int]
        Z_FIELD_NUMBER: _ClassVar[int]
        x: float
        y: float
        z: float
        def __init__(
            self,
            x: _Optional[float] = ...,
            y: _Optional[float] = ...,
            z: _Optional[float] = ...,
        ) -> None: ...

    class WatchedDeathReplay(_message.Message):
        __slots__ = ["game_time_s", "player_slot"]
        GAME_TIME_S_FIELD_NUMBER: _ClassVar[int]
        PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
        game_time_s: int
        player_slot: int
        def __init__(
            self, game_time_s: _Optional[int] = ..., player_slot: _Optional[int] = ...
        ) -> None: ...

    MATCH_INFO_FIELD_NUMBER: _ClassVar[int]
    k_eAssists: CMsgMatchMetaDataContents.EGoldSource
    k_eBosses: CMsgMatchMetaDataContents.EGoldSource
    k_eDenies: CMsgMatchMetaDataContents.EGoldSource
    k_eLaneCreeps: CMsgMatchMetaDataContents.EGoldSource
    k_eNeutrals: CMsgMatchMetaDataContents.EGoldSource
    k_eOutcome_Error: CMsgMatchMetaDataContents.EMatchOutcome
    k_eOutcome_TeamWin: CMsgMatchMetaDataContents.EMatchOutcome
    k_ePlayers: CMsgMatchMetaDataContents.EGoldSource
    k_eTreasure: CMsgMatchMetaDataContents.EGoldSource
    match_info: CMsgMatchMetaDataContents.MatchInfo
    def __init__(
        self,
        match_info: _Optional[
            _Union[CMsgMatchMetaDataContents.MatchInfo, _Mapping]
        ] = ...,
    ) -> None: ...

class CMsgMatchPlayerDamageMatrix(_message.Message):
    __slots__ = ["damage_dealers", "sample_time_s", "source_details"]

    class EStatType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    class DamageDealer(_message.Message):
        __slots__ = ["damage_sources", "dealer_player_slot"]
        DAMAGE_SOURCES_FIELD_NUMBER: _ClassVar[int]
        DEALER_PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
        damage_sources: _containers.RepeatedCompositeFieldContainer[
            CMsgMatchPlayerDamageMatrix.DamageSource
        ]
        dealer_player_slot: int
        def __init__(
            self,
            dealer_player_slot: _Optional[int] = ...,
            damage_sources: _Optional[
                _Iterable[_Union[CMsgMatchPlayerDamageMatrix.DamageSource, _Mapping]]
            ] = ...,
        ) -> None: ...

    class DamageSource(_message.Message):
        __slots__ = ["damage_to_players", "source_details_index"]
        DAMAGE_TO_PLAYERS_FIELD_NUMBER: _ClassVar[int]
        SOURCE_DETAILS_INDEX_FIELD_NUMBER: _ClassVar[int]
        damage_to_players: _containers.RepeatedCompositeFieldContainer[
            CMsgMatchPlayerDamageMatrix.DamageToPlayer
        ]
        source_details_index: int
        def __init__(
            self,
            damage_to_players: _Optional[
                _Iterable[_Union[CMsgMatchPlayerDamageMatrix.DamageToPlayer, _Mapping]]
            ] = ...,
            source_details_index: _Optional[int] = ...,
        ) -> None: ...

    class DamageToPlayer(_message.Message):
        __slots__ = ["damage", "target_player_slot"]
        DAMAGE_FIELD_NUMBER: _ClassVar[int]
        TARGET_PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
        damage: _containers.RepeatedScalarFieldContainer[int]
        target_player_slot: int
        def __init__(
            self,
            target_player_slot: _Optional[int] = ...,
            damage: _Optional[_Iterable[int]] = ...,
        ) -> None: ...

    class SourceDetails(_message.Message):
        __slots__ = ["source_name", "stat_type"]
        SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
        STAT_TYPE_FIELD_NUMBER: _ClassVar[int]
        source_name: _containers.RepeatedScalarFieldContainer[str]
        stat_type: _containers.RepeatedScalarFieldContainer[
            CMsgMatchPlayerDamageMatrix.EStatType
        ]
        def __init__(
            self,
            stat_type: _Optional[
                _Iterable[_Union[CMsgMatchPlayerDamageMatrix.EStatType, str]]
            ] = ...,
            source_name: _Optional[_Iterable[str]] = ...,
        ) -> None: ...

    DAMAGE_DEALERS_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_TIME_S_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    damage_dealers: _containers.RepeatedCompositeFieldContainer[
        CMsgMatchPlayerDamageMatrix.DamageDealer
    ]
    k_eType_Damage: CMsgMatchPlayerDamageMatrix.EStatType
    k_eType_HealPrevented: CMsgMatchPlayerDamageMatrix.EStatType
    k_eType_Healing: CMsgMatchPlayerDamageMatrix.EStatType
    k_eType_LethalDamage: CMsgMatchPlayerDamageMatrix.EStatType
    k_eType_Mitigated: CMsgMatchPlayerDamageMatrix.EStatType
    sample_time_s: _containers.RepeatedScalarFieldContainer[int]
    source_details: CMsgMatchPlayerDamageMatrix.SourceDetails
    def __init__(
        self,
        damage_dealers: _Optional[
            _Iterable[_Union[CMsgMatchPlayerDamageMatrix.DamageDealer, _Mapping]]
        ] = ...,
        sample_time_s: _Optional[_Iterable[int]] = ...,
        source_details: _Optional[
            _Union[CMsgMatchPlayerDamageMatrix.SourceDetails, _Mapping]
        ] = ...,
    ) -> None: ...

class CMsgMatchPlayerPathsData(_message.Message):
    __slots__ = ["interval_s", "paths", "version", "x_resolution", "y_resolution"]

    class Path(_message.Message):
        __slots__ = [
            "alive",
            "health",
            "player_slot",
            "x_max",
            "x_min",
            "x_pos",
            "y_max",
            "y_min",
            "y_pos",
        ]
        ALIVE_FIELD_NUMBER: _ClassVar[int]
        HEALTH_FIELD_NUMBER: _ClassVar[int]
        PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
        X_MAX_FIELD_NUMBER: _ClassVar[int]
        X_MIN_FIELD_NUMBER: _ClassVar[int]
        X_POS_FIELD_NUMBER: _ClassVar[int]
        Y_MAX_FIELD_NUMBER: _ClassVar[int]
        Y_MIN_FIELD_NUMBER: _ClassVar[int]
        Y_POS_FIELD_NUMBER: _ClassVar[int]
        alive: _containers.RepeatedScalarFieldContainer[bool]
        health: _containers.RepeatedScalarFieldContainer[int]
        player_slot: int
        x_max: float
        x_min: float
        x_pos: _containers.RepeatedScalarFieldContainer[int]
        y_max: float
        y_min: float
        y_pos: _containers.RepeatedScalarFieldContainer[int]
        def __init__(
            self,
            player_slot: _Optional[int] = ...,
            x_min: _Optional[float] = ...,
            y_min: _Optional[float] = ...,
            x_max: _Optional[float] = ...,
            y_max: _Optional[float] = ...,
            x_pos: _Optional[_Iterable[int]] = ...,
            y_pos: _Optional[_Iterable[int]] = ...,
            alive: _Optional[_Iterable[bool]] = ...,
            health: _Optional[_Iterable[int]] = ...,
        ) -> None: ...

    INTERVAL_S_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    X_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    Y_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    interval_s: float
    paths: _containers.RepeatedCompositeFieldContainer[CMsgMatchPlayerPathsData.Path]
    version: int
    x_resolution: int
    y_resolution: int
    def __init__(
        self,
        version: _Optional[int] = ...,
        interval_s: _Optional[float] = ...,
        x_resolution: _Optional[int] = ...,
        y_resolution: _Optional[int] = ...,
        paths: _Optional[
            _Iterable[_Union[CMsgMatchPlayerPathsData.Path, _Mapping]]
        ] = ...,
    ) -> None: ...

class CMsgRegionPingTimesClient(_message.Message):
    __slots__ = ["data_center_codes", "ping_times"]
    DATA_CENTER_CODES_FIELD_NUMBER: _ClassVar[int]
    PING_TIMES_FIELD_NUMBER: _ClassVar[int]
    data_center_codes: _containers.RepeatedScalarFieldContainer[int]
    ping_times: _containers.RepeatedScalarFieldContainer[int]
    def __init__(
        self,
        data_center_codes: _Optional[_Iterable[int]] = ...,
        ping_times: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class CMsgStartFindingMatchInfo(_message.Message):
    __slots__ = [
        "bot_difficulty",
        "game_mode",
        "match_mode",
        "region_mode",
        "server_command_string",
        "server_search_key",
        "solo_match",
    ]
    BOT_DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    GAME_MODE_FIELD_NUMBER: _ClassVar[int]
    MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    REGION_MODE_FIELD_NUMBER: _ClassVar[int]
    SERVER_COMMAND_STRING_FIELD_NUMBER: _ClassVar[int]
    SERVER_SEARCH_KEY_FIELD_NUMBER: _ClassVar[int]
    SOLO_MATCH_FIELD_NUMBER: _ClassVar[int]
    bot_difficulty: ECitadelBotDifficulty
    game_mode: ECitadelGameMode
    match_mode: ECitadelMatchMode
    region_mode: ECitadelRegionMode
    server_command_string: str
    server_search_key: str
    solo_match: bool
    def __init__(
        self,
        server_search_key: _Optional[str] = ...,
        server_command_string: _Optional[str] = ...,
        match_mode: _Optional[_Union[ECitadelMatchMode, str]] = ...,
        game_mode: _Optional[_Union[ECitadelGameMode, str]] = ...,
        solo_match: bool = ...,
        bot_difficulty: _Optional[_Union[ECitadelBotDifficulty, str]] = ...,
        region_mode: _Optional[_Union[ECitadelRegionMode, str]] = ...,
    ) -> None: ...

class CSOCitadelLobby(_message.Message):
    __slots__ = [
        "compatibility_version",
        "extra_messages",
        "game_mode",
        "lobby_id",
        "match_id",
        "match_mode",
        "safe_to_abandon",
        "sdr_address",
        "server_state",
        "server_steam_id",
        "server_version",
        "udp_connect_ip",
        "udp_connect_port",
    ]
    COMPATIBILITY_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXTRA_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    GAME_MODE_FIELD_NUMBER: _ClassVar[int]
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    SAFE_TO_ABANDON_FIELD_NUMBER: _ClassVar[int]
    SDR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SERVER_STATE_FIELD_NUMBER: _ClassVar[int]
    SERVER_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    UDP_CONNECT_IP_FIELD_NUMBER: _ClassVar[int]
    UDP_CONNECT_PORT_FIELD_NUMBER: _ClassVar[int]
    compatibility_version: int
    extra_messages: _containers.RepeatedCompositeFieldContainer[
        _gcsdk_gcmessages_pb2.CExtraMsgBlock
    ]
    game_mode: ECitadelGameMode
    lobby_id: int
    match_id: int
    match_mode: ECitadelMatchMode
    safe_to_abandon: bool
    sdr_address: bytes
    server_state: ELobbyServerState
    server_steam_id: int
    server_version: int
    udp_connect_ip: int
    udp_connect_port: int
    def __init__(
        self,
        lobby_id: _Optional[int] = ...,
        match_id: _Optional[int] = ...,
        match_mode: _Optional[_Union[ECitadelMatchMode, str]] = ...,
        game_mode: _Optional[_Union[ECitadelGameMode, str]] = ...,
        compatibility_version: _Optional[int] = ...,
        extra_messages: _Optional[
            _Iterable[_Union[_gcsdk_gcmessages_pb2.CExtraMsgBlock, _Mapping]]
        ] = ...,
        server_steam_id: _Optional[int] = ...,
        server_state: _Optional[_Union[ELobbyServerState, str]] = ...,
        udp_connect_ip: _Optional[int] = ...,
        udp_connect_port: _Optional[int] = ...,
        sdr_address: _Optional[bytes] = ...,
        server_version: _Optional[int] = ...,
        safe_to_abandon: bool = ...,
    ) -> None: ...

class CSOCitadelParty(_message.Message):
    __slots__ = [
        "bot_difficulty",
        "chat_mode",
        "dev_server_command",
        "game_mode",
        "invites",
        "is_high_skill_range_party",
        "is_private_lobby",
        "join_code",
        "left_members",
        "match_making_start_time",
        "match_mode",
        "members",
        "party_id",
        "private_lobby_settings",
        "region_mode",
        "server_search_key",
    ]

    class EChatMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    class EMemberRights(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    class EPlayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    class Invite(_message.Message):
        __slots__ = ["account_id", "invited_by", "persona_name"]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        INVITED_BY_FIELD_NUMBER: _ClassVar[int]
        PERSONA_NAME_FIELD_NUMBER: _ClassVar[int]
        account_id: int
        invited_by: int
        persona_name: str
        def __init__(
            self,
            account_id: _Optional[int] = ...,
            persona_name: _Optional[str] = ...,
            invited_by: _Optional[int] = ...,
        ) -> None: ...

    class LeftMember(_message.Message):
        __slots__ = ["account_id", "player_type", "rights_flags"]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        PLAYER_TYPE_FIELD_NUMBER: _ClassVar[int]
        RIGHTS_FLAGS_FIELD_NUMBER: _ClassVar[int]
        account_id: int
        player_type: CSOCitadelParty.EPlayerType
        rights_flags: int
        def __init__(
            self,
            account_id: _Optional[int] = ...,
            rights_flags: _Optional[int] = ...,
            player_type: _Optional[_Union[CSOCitadelParty.EPlayerType, str]] = ...,
        ) -> None: ...

    class Member(_message.Message):
        __slots__ = [
            "account_id",
            "compatibility_version",
            "hero_roster",
            "is_ready",
            "new_player_progress",
            "owned_heroes",
            "permissions",
            "persona_name",
            "platform",
            "player_type",
            "rights_flags",
            "team",
        ]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        COMPATIBILITY_VERSION_FIELD_NUMBER: _ClassVar[int]
        HERO_ROSTER_FIELD_NUMBER: _ClassVar[int]
        IS_READY_FIELD_NUMBER: _ClassVar[int]
        NEW_PLAYER_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        OWNED_HEROES_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        PERSONA_NAME_FIELD_NUMBER: _ClassVar[int]
        PLATFORM_FIELD_NUMBER: _ClassVar[int]
        PLAYER_TYPE_FIELD_NUMBER: _ClassVar[int]
        RIGHTS_FLAGS_FIELD_NUMBER: _ClassVar[int]
        TEAM_FIELD_NUMBER: _ClassVar[int]
        account_id: int
        compatibility_version: int
        hero_roster: CMsgHeroSelectionMatchInfo
        is_ready: bool
        new_player_progress: int
        owned_heroes: _containers.RepeatedScalarFieldContainer[int]
        permissions: int
        persona_name: str
        platform: _steammessages_pb2.EGCPlatform
        player_type: CSOCitadelParty.EPlayerType
        rights_flags: int
        team: int
        def __init__(
            self,
            account_id: _Optional[int] = ...,
            persona_name: _Optional[str] = ...,
            rights_flags: _Optional[int] = ...,
            is_ready: bool = ...,
            player_type: _Optional[_Union[CSOCitadelParty.EPlayerType, str]] = ...,
            compatibility_version: _Optional[int] = ...,
            platform: _Optional[_Union[_steammessages_pb2.EGCPlatform, str]] = ...,
            team: _Optional[int] = ...,
            hero_roster: _Optional[_Union[CMsgHeroSelectionMatchInfo, _Mapping]] = ...,
            permissions: _Optional[int] = ...,
            new_player_progress: _Optional[int] = ...,
            owned_heroes: _Optional[_Iterable[int]] = ...,
        ) -> None: ...

    class PrivateLobbySettings(_message.Message):
        __slots__ = [
            "available_regions",
            "cheats_enabled",
            "duplicate_heroes_enabled",
            "is_publicly_visible",
            "match_slots",
            "min_roster_size",
            "randomize_lanes",
            "server_region",
        ]
        AVAILABLE_REGIONS_FIELD_NUMBER: _ClassVar[int]
        CHEATS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        DUPLICATE_HEROES_ENABLED_FIELD_NUMBER: _ClassVar[int]
        IS_PUBLICLY_VISIBLE_FIELD_NUMBER: _ClassVar[int]
        MATCH_SLOTS_FIELD_NUMBER: _ClassVar[int]
        MIN_ROSTER_SIZE_FIELD_NUMBER: _ClassVar[int]
        RANDOMIZE_LANES_FIELD_NUMBER: _ClassVar[int]
        SERVER_REGION_FIELD_NUMBER: _ClassVar[int]
        available_regions: _containers.RepeatedCompositeFieldContainer[
            CSOCitadelParty.ServerRegion
        ]
        cheats_enabled: bool
        duplicate_heroes_enabled: bool
        is_publicly_visible: bool
        match_slots: _containers.RepeatedCompositeFieldContainer[
            CSOCitadelParty.PrivateLobbySlot
        ]
        min_roster_size: int
        randomize_lanes: bool
        server_region: int
        def __init__(
            self,
            min_roster_size: _Optional[int] = ...,
            match_slots: _Optional[
                _Iterable[_Union[CSOCitadelParty.PrivateLobbySlot, _Mapping]]
            ] = ...,
            randomize_lanes: bool = ...,
            server_region: _Optional[int] = ...,
            is_publicly_visible: bool = ...,
            cheats_enabled: bool = ...,
            available_regions: _Optional[
                _Iterable[_Union[CSOCitadelParty.ServerRegion, _Mapping]]
            ] = ...,
            duplicate_heroes_enabled: bool = ...,
        ) -> None: ...

    class PrivateLobbySlot(_message.Message):
        __slots__ = ["player_account_id", "slot_id"]
        PLAYER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        SLOT_ID_FIELD_NUMBER: _ClassVar[int]
        player_account_id: int
        slot_id: int
        def __init__(
            self, slot_id: _Optional[int] = ..., player_account_id: _Optional[int] = ...
        ) -> None: ...

    class ServerRegion(_message.Message):
        __slots__ = ["region_id"]
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        region_id: int
        def __init__(self, region_id: _Optional[int] = ...) -> None: ...

    BOT_DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    CHAT_MODE_FIELD_NUMBER: _ClassVar[int]
    DEV_SERVER_COMMAND_FIELD_NUMBER: _ClassVar[int]
    GAME_MODE_FIELD_NUMBER: _ClassVar[int]
    INVITES_FIELD_NUMBER: _ClassVar[int]
    IS_HIGH_SKILL_RANGE_PARTY_FIELD_NUMBER: _ClassVar[int]
    IS_PRIVATE_LOBBY_FIELD_NUMBER: _ClassVar[int]
    JOIN_CODE_FIELD_NUMBER: _ClassVar[int]
    LEFT_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    MATCH_MAKING_START_TIME_FIELD_NUMBER: _ClassVar[int]
    MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_LOBBY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    REGION_MODE_FIELD_NUMBER: _ClassVar[int]
    SERVER_SEARCH_KEY_FIELD_NUMBER: _ClassVar[int]
    bot_difficulty: ECitadelBotDifficulty
    chat_mode: CSOCitadelParty.EChatMode
    dev_server_command: str
    game_mode: ECitadelGameMode
    invites: _containers.RepeatedCompositeFieldContainer[CSOCitadelParty.Invite]
    is_high_skill_range_party: bool
    is_private_lobby: bool
    join_code: int
    k_eMemberRights_Admin: CSOCitadelParty.EMemberRights
    k_eMemberRights_Creator: CSOCitadelParty.EMemberRights
    k_eNone: CSOCitadelParty.EChatMode
    k_ePartyChat: CSOCitadelParty.EChatMode
    k_ePlayerType_Player: CSOCitadelParty.EPlayerType
    k_ePlayerType_Spectator: CSOCitadelParty.EPlayerType
    k_eTeamChat: CSOCitadelParty.EChatMode
    left_members: _containers.RepeatedCompositeFieldContainer[
        CSOCitadelParty.LeftMember
    ]
    match_making_start_time: int
    match_mode: ECitadelMatchMode
    members: _containers.RepeatedCompositeFieldContainer[CSOCitadelParty.Member]
    party_id: int
    private_lobby_settings: CSOCitadelParty.PrivateLobbySettings
    region_mode: ECitadelRegionMode
    server_search_key: str
    def __init__(
        self,
        party_id: _Optional[int] = ...,
        members: _Optional[_Iterable[_Union[CSOCitadelParty.Member, _Mapping]]] = ...,
        invites: _Optional[_Iterable[_Union[CSOCitadelParty.Invite, _Mapping]]] = ...,
        dev_server_command: _Optional[str] = ...,
        left_members: _Optional[
            _Iterable[_Union[CSOCitadelParty.LeftMember, _Mapping]]
        ] = ...,
        join_code: _Optional[int] = ...,
        bot_difficulty: _Optional[_Union[ECitadelBotDifficulty, str]] = ...,
        match_mode: _Optional[_Union[ECitadelMatchMode, str]] = ...,
        game_mode: _Optional[_Union[ECitadelGameMode, str]] = ...,
        match_making_start_time: _Optional[int] = ...,
        server_search_key: _Optional[str] = ...,
        is_high_skill_range_party: bool = ...,
        chat_mode: _Optional[_Union[CSOCitadelParty.EChatMode, str]] = ...,
        region_mode: _Optional[_Union[ECitadelRegionMode, str]] = ...,
        is_private_lobby: bool = ...,
        private_lobby_settings: _Optional[
            _Union[CSOCitadelParty.PrivateLobbySettings, _Mapping]
        ] = ...,
    ) -> None: ...

class CMsgLaneColor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EGCCitadelCommonMessages(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ECitadelMatchMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ECitadelLobbyTeam(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ECitadelAccountStatMedal(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ECitadelObjective(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ECitadelTeamObjective(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ECitadelBotDifficulty(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ECitadelRegionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ECitadelGameMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ELobbyServerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EBannedFeature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EFeatureBanReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
