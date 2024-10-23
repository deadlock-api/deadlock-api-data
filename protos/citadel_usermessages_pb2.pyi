from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

import citadel_gcmessages_common_pb2 as _citadel_gcmessages_common_pb2
import gameevents_pb2 as _gameevents_pb2
import networkbasetypes_pb2 as _networkbasetypes_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

CITADEL_CHAT_MESSAGE_AUTO_UNPAUSED: ECitadelChatMessage
CITADEL_CHAT_MESSAGE_CANTPAUSE: ECitadelChatMessage
CITADEL_CHAT_MESSAGE_CANTPAUSEYET: ECitadelChatMessage
CITADEL_CHAT_MESSAGE_CANTUNPAUSETEAM: ECitadelChatMessage
CITADEL_CHAT_MESSAGE_COMMS_RESTRICTED: ECitadelChatMessage
CITADEL_CHAT_MESSAGE_NOPAUSESLEFT: ECitadelChatMessage
CITADEL_CHAT_MESSAGE_NOTEAMPAUSESLEFT: ECitadelChatMessage
CITADEL_CHAT_MESSAGE_PAUSED: ECitadelChatMessage
CITADEL_CHAT_MESSAGE_PAUSE_COUNTDOWN: ECitadelChatMessage
CITADEL_CHAT_MESSAGE_PREGAME_COUNTDOWN: ECitadelChatMessage
CITADEL_CHAT_MESSAGE_UNPAUSED: ECitadelChatMessage
CITADEL_CHAT_MESSAGE_UNPAUSE_COUNTDOWN: ECitadelChatMessage
CITADEL_CHAT_MESSAGE_YOUPAUSED: ECitadelChatMessage
DESCRIPTOR: _descriptor.FileDescriptor
PostProcState_Black: PostProcessingGameStates
PostProcState_Blinded: PostProcessingGameStates
PostProcState_Killed: PostProcessingGameStates
PostProcState_ShivPossessed: PostProcessingGameStates
k_EAction_AddOp: CameraAction
k_EAction_ClearAllOps: CameraAction
k_EAction_ClearOpsForContext: CameraAction
k_ECameraOp_Approach: CameraOperation
k_ECameraOp_Lag: CameraOperation
k_ECameraOp_Lerp: CameraOperation
k_ECameraOp_Maintain: CameraOperation
k_ECameraOp_Spring: CameraOperation
k_EEntityMsg_BreakablePropSpawnDebris: CitadelEntityMessageIds
k_EParamMode_AllowInMultipleContexts: CameraParamMode
k_EParamMode_AllowInOneContext: CameraParamMode
k_EParam_ClearAllOps: CameraParam
k_EParam_ClearAllOpsForContext: CameraParam
k_EParam_Distance: CameraParam
k_EParam_FOV: CameraParam
k_EParam_HorizOffset: CameraParam
k_EParam_TargetPosition: CameraParam
k_EParam_VertOffset: CameraParam
k_EPingMarkerInfo_HideMarkerAndSound: ChatMsgPingMarkerInfo
k_EPingMarkerInfo_OnlyPlaySound: ChatMsgPingMarkerInfo
k_EPingMarkerInfo_OnlyShowMarker: ChatMsgPingMarkerInfo
k_EPingMarkerInfo_ShowMarkerAndSound: ChatMsgPingMarkerInfo
k_EPingMarkerInfo_ShowMarkerOnSender: ChatMsgPingMarkerInfo
k_EUserMsg_AbilitiesChanged: CitadelUserMessageIds
k_EUserMsg_AbilityFailed: CitadelUserMessageIds
k_EUserMsg_AbilityInterrupted: CitadelUserMessageIds
k_EUserMsg_AbilityLateFailure: CitadelUserMessageIds
k_EUserMsg_AbilityNotify: CitadelUserMessageIds
k_EUserMsg_AbilityPing: CitadelUserMessageIds
k_EUserMsg_AuraModifierApplied: CitadelUserMessageIds
k_EUserMsg_BossDamaged: CitadelUserMessageIds
k_EUserMsg_BossKilled: CitadelUserMessageIds
k_EUserMsg_BulletHit: CitadelUserMessageIds
k_EUserMsg_CallCheaterVote: CitadelUserMessageIds
k_EUserMsg_CameraController: CitadelUserMessageIds
k_EUserMsg_ChatEvent: CitadelUserMessageIds
k_EUserMsg_ChatMsg: CitadelUserMessageIds
k_EUserMsg_ChatWheel: CitadelUserMessageIds
k_EUserMsg_CurrencyChanged: CitadelUserMessageIds
k_EUserMsg_Damage: CitadelUserMessageIds
k_EUserMsg_DeathReplayData: CitadelUserMessageIds
k_EUserMsg_ForceShopClosed: CitadelUserMessageIds
k_EUserMsg_GameOver: CitadelUserMessageIds
k_EUserMsg_GetDamageStatsResponse: CitadelUserMessageIds
k_EUserMsg_GoldHistory: CitadelUserMessageIds
k_EUserMsg_HeroKilled: CitadelUserMessageIds
k_EUserMsg_KillStreak: CitadelUserMessageIds
k_EUserMsg_MapLine: CitadelUserMessageIds
k_EUserMsg_MapPing: CitadelUserMessageIds
k_EUserMsg_MidBossSpawned: CitadelUserMessageIds
k_EUserMsg_ModifierApplied: CitadelUserMessageIds
k_EUserMsg_ObjectiveMask: CitadelUserMessageIds
k_EUserMsg_ObstructedShotFired: CitadelUserMessageIds
k_EUserMsg_ParticipantSetLibraryStackFields: CitadelUserMessageIds
k_EUserMsg_ParticipantSetSoundEventParams: CitadelUserMessageIds
k_EUserMsg_ParticipantStartSoundEvent: CitadelUserMessageIds
k_EUserMsg_ParticipantStopSoundEvent: CitadelUserMessageIds
k_EUserMsg_ParticipantStopSoundEventHash: CitadelUserMessageIds
k_EUserMsg_PlayerLifetimeStatInfo: CitadelUserMessageIds
k_EUserMsg_PlayerRespawned: CitadelUserMessageIds
k_EUserMsg_PostMatchDetails: CitadelUserMessageIds
k_EUserMsg_PostProcessingAnim: CitadelUserMessageIds
k_EUserMsg_QuickResponse: CitadelUserMessageIds
k_EUserMsg_RecentDamageSummary: CitadelUserMessageIds
k_EUserMsg_RejuvStatus: CitadelUserMessageIds
k_EUserMsg_ReturnIdol: CitadelUserMessageIds
k_EUserMsg_SetClientCameraAngles: CitadelUserMessageIds
k_EUserMsg_SpectatorTeamChanged: CitadelUserMessageIds
k_EUserMsg_StaminaDrained: CitadelUserMessageIds
k_EUserMsg_TeamMsg: CitadelUserMessageIds
k_EUserMsg_TeamRewards: CitadelUserMessageIds
k_EUserMsg_TriggerDamageFlash: CitadelUserMessageIds

class CCitadelEntityMsg_BreakablePropSpawnDebris(_message.Message):
    __slots__ = ["damage", "damage_pos", "entity_msg"]
    DAMAGE_FIELD_NUMBER: _ClassVar[int]
    DAMAGE_POS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_MSG_FIELD_NUMBER: _ClassVar[int]
    damage: float
    damage_pos: _networkbasetypes_pb2.CMsgVector
    entity_msg: _networkbasetypes_pb2.CEntityMsg
    def __init__(
        self,
        entity_msg: _Optional[_Union[_networkbasetypes_pb2.CEntityMsg, _Mapping]] = ...,
        damage_pos: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...,
        damage: _Optional[float] = ...,
    ) -> None: ...

class CCitadelUserMessage_AbilityNotify(_message.Message):
    __slots__ = ["ability_id", "entindex_attacker", "entindex_victim"]
    ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_ATTACKER_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_VICTIM_FIELD_NUMBER: _ClassVar[int]
    ability_id: int
    entindex_attacker: int
    entindex_victim: int
    def __init__(
        self,
        entindex_victim: _Optional[int] = ...,
        entindex_attacker: _Optional[int] = ...,
        ability_id: _Optional[int] = ...,
    ) -> None: ...

class CCitadelUserMessage_AuraModifierApplied(_message.Message):
    __slots__ = [
        "aura_end_time",
        "aura_start_time",
        "entindex_caster",
        "entindex_target",
        "modifier_serial_number",
        "modifier_type_id",
    ]
    AURA_END_TIME_FIELD_NUMBER: _ClassVar[int]
    AURA_START_TIME_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_CASTER_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_TARGET_FIELD_NUMBER: _ClassVar[int]
    MODIFIER_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MODIFIER_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    aura_end_time: float
    aura_start_time: float
    entindex_caster: int
    entindex_target: int
    modifier_serial_number: int
    modifier_type_id: int
    def __init__(
        self,
        entindex_caster: _Optional[int] = ...,
        entindex_target: _Optional[int] = ...,
        modifier_type_id: _Optional[int] = ...,
        modifier_serial_number: _Optional[int] = ...,
        aura_start_time: _Optional[float] = ...,
        aura_end_time: _Optional[float] = ...,
    ) -> None: ...

class CCitadelUserMessage_BulletHit(_message.Message):
    __slots__ = ["hit_entindex", "pellet", "shotid"]
    HIT_ENTINDEX_FIELD_NUMBER: _ClassVar[int]
    PELLET_FIELD_NUMBER: _ClassVar[int]
    SHOTID_FIELD_NUMBER: _ClassVar[int]
    hit_entindex: int
    pellet: int
    shotid: int
    def __init__(
        self,
        shotid: _Optional[int] = ...,
        pellet: _Optional[int] = ...,
        hit_entindex: _Optional[int] = ...,
    ) -> None: ...

class CCitadelUserMessage_CurrencyChanged(_message.Message):
    __slots__ = [
        "ability_id",
        "currency_source",
        "currency_type",
        "delta",
        "entindex_hero_pawn",
        "entindex_victim",
        "notification",
        "playsound",
        "victim_pos",
    ]
    ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DELTA_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_HERO_PAWN_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_VICTIM_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    PLAYSOUND_FIELD_NUMBER: _ClassVar[int]
    VICTIM_POS_FIELD_NUMBER: _ClassVar[int]
    ability_id: int
    currency_source: int
    currency_type: int
    delta: int
    entindex_hero_pawn: int
    entindex_victim: int
    notification: bool
    playsound: int
    victim_pos: _networkbasetypes_pb2.CMsgVector
    def __init__(
        self,
        entindex_hero_pawn: _Optional[int] = ...,
        currency_type: _Optional[int] = ...,
        currency_source: _Optional[int] = ...,
        delta: _Optional[int] = ...,
        notification: bool = ...,
        entindex_victim: _Optional[int] = ...,
        victim_pos: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...,
        playsound: _Optional[int] = ...,
        ability_id: _Optional[int] = ...,
    ) -> None: ...

class CCitadelUserMessage_Damage(_message.Message):
    __slots__ = [
        "ability_id",
        "attacker_class",
        "citadel_type",
        "damage",
        "damage_absorbed",
        "entindex_ability",
        "entindex_attacker",
        "entindex_inflictor",
        "entindex_victim",
        "flags",
        "health_lost",
        "hits",
        "origin",
        "pre_damage",
        "type",
        "victim_class",
        "victim_health_max",
        "victim_health_new",
        "victim_shield_max",
        "victim_shield_new",
    ]
    ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
    ATTACKER_CLASS_FIELD_NUMBER: _ClassVar[int]
    CITADEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    DAMAGE_ABSORBED_FIELD_NUMBER: _ClassVar[int]
    DAMAGE_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_ABILITY_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_ATTACKER_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_INFLICTOR_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_VICTIM_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    HEALTH_LOST_FIELD_NUMBER: _ClassVar[int]
    HITS_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PRE_DAMAGE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VICTIM_CLASS_FIELD_NUMBER: _ClassVar[int]
    VICTIM_HEALTH_MAX_FIELD_NUMBER: _ClassVar[int]
    VICTIM_HEALTH_NEW_FIELD_NUMBER: _ClassVar[int]
    VICTIM_SHIELD_MAX_FIELD_NUMBER: _ClassVar[int]
    VICTIM_SHIELD_NEW_FIELD_NUMBER: _ClassVar[int]
    ability_id: int
    attacker_class: int
    citadel_type: int
    damage: int
    damage_absorbed: int
    entindex_ability: int
    entindex_attacker: int
    entindex_inflictor: int
    entindex_victim: int
    flags: int
    health_lost: int
    hits: int
    origin: _networkbasetypes_pb2.CMsgVector
    pre_damage: int
    type: int
    victim_class: int
    victim_health_max: int
    victim_health_new: int
    victim_shield_max: int
    victim_shield_new: int
    def __init__(
        self,
        damage: _Optional[int] = ...,
        pre_damage: _Optional[int] = ...,
        type: _Optional[int] = ...,
        citadel_type: _Optional[int] = ...,
        origin: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...,
        entindex_victim: _Optional[int] = ...,
        entindex_inflictor: _Optional[int] = ...,
        entindex_attacker: _Optional[int] = ...,
        entindex_ability: _Optional[int] = ...,
        damage_absorbed: _Optional[int] = ...,
        victim_health_max: _Optional[int] = ...,
        victim_health_new: _Optional[int] = ...,
        flags: _Optional[int] = ...,
        ability_id: _Optional[int] = ...,
        attacker_class: _Optional[int] = ...,
        victim_class: _Optional[int] = ...,
        victim_shield_max: _Optional[int] = ...,
        victim_shield_new: _Optional[int] = ...,
        hits: _Optional[int] = ...,
        health_lost: _Optional[int] = ...,
    ) -> None: ...

class CCitadelUserMessage_GameOver(_message.Message):
    __slots__ = ["just_a_test", "winning_team"]
    JUST_A_TEST_FIELD_NUMBER: _ClassVar[int]
    WINNING_TEAM_FIELD_NUMBER: _ClassVar[int]
    just_a_test: bool
    winning_team: int
    def __init__(
        self, winning_team: _Optional[int] = ..., just_a_test: bool = ...
    ) -> None: ...

class CCitadelUserMessage_ModifierApplied(_message.Message):
    __slots__ = ["entindex_caster", "entindex_parent", "serial_number"]
    ENTINDEX_CASTER_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_PARENT_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    entindex_caster: int
    entindex_parent: int
    serial_number: int
    def __init__(
        self,
        entindex_caster: _Optional[int] = ...,
        entindex_parent: _Optional[int] = ...,
        serial_number: _Optional[int] = ...,
    ) -> None: ...

class CCitadelUserMessage_ObjectiveMask(_message.Message):
    __slots__ = ["objective_mask_team0", "objective_mask_team1"]
    OBJECTIVE_MASK_TEAM0_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVE_MASK_TEAM1_FIELD_NUMBER: _ClassVar[int]
    objective_mask_team0: int
    objective_mask_team1: int
    def __init__(
        self,
        objective_mask_team0: _Optional[int] = ...,
        objective_mask_team1: _Optional[int] = ...,
    ) -> None: ...

class CCitadelUserMsg_AbilitiesChanged(_message.Message):
    __slots__ = ["ability_id", "change", "entindex_ability", "entindex_purchaser"]

    class Change(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    EInvalid: CCitadelUserMsg_AbilitiesChanged.Change
    ENTINDEX_ABILITY_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_PURCHASER_FIELD_NUMBER: _ClassVar[int]
    EPurchased: CCitadelUserMsg_AbilitiesChanged.Change
    ESold: CCitadelUserMsg_AbilitiesChanged.Change
    ESwappedActivatedAbility: CCitadelUserMsg_AbilitiesChanged.Change
    EUpgraded: CCitadelUserMsg_AbilitiesChanged.Change
    ability_id: int
    change: CCitadelUserMsg_AbilitiesChanged.Change
    entindex_ability: int
    entindex_purchaser: int
    def __init__(
        self,
        entindex_purchaser: _Optional[int] = ...,
        entindex_ability: _Optional[int] = ...,
        ability_id: _Optional[int] = ...,
        change: _Optional[_Union[CCitadelUserMsg_AbilitiesChanged.Change, str]] = ...,
    ) -> None: ...

class CCitadelUserMsg_AbilityInterrupted(_message.Message):
    __slots__ = [
        "ability_id_interrupted",
        "ability_id_interrupter",
        "entindex_interrupter",
        "entindex_victim",
        "hero_id_interrupter",
    ]
    ABILITY_ID_INTERRUPTED_FIELD_NUMBER: _ClassVar[int]
    ABILITY_ID_INTERRUPTER_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_INTERRUPTER_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_VICTIM_FIELD_NUMBER: _ClassVar[int]
    HERO_ID_INTERRUPTER_FIELD_NUMBER: _ClassVar[int]
    ability_id_interrupted: int
    ability_id_interrupter: int
    entindex_interrupter: int
    entindex_victim: int
    hero_id_interrupter: int
    def __init__(
        self,
        entindex_victim: _Optional[int] = ...,
        entindex_interrupter: _Optional[int] = ...,
        ability_id_interrupted: _Optional[int] = ...,
        ability_id_interrupter: _Optional[int] = ...,
        hero_id_interrupter: _Optional[int] = ...,
    ) -> None: ...

class CCitadelUserMsg_AbilityLateFailure(_message.Message):
    __slots__ = ["entindex_ability", "entindex_caster", "failure_type"]
    ENTINDEX_ABILITY_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_CASTER_FIELD_NUMBER: _ClassVar[int]
    FAILURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    entindex_ability: int
    entindex_caster: int
    failure_type: int
    def __init__(
        self,
        entindex_caster: _Optional[int] = ...,
        entindex_ability: _Optional[int] = ...,
        failure_type: _Optional[int] = ...,
    ) -> None: ...

class CCitadelUserMsg_AbilityPing(_message.Message):
    __slots__ = [
        "ability_cooldown",
        "ability_id",
        "ping_data",
        "ping_marker_and_sound_info",
    ]
    ABILITY_COOLDOWN_FIELD_NUMBER: _ClassVar[int]
    ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
    PING_DATA_FIELD_NUMBER: _ClassVar[int]
    PING_MARKER_AND_SOUND_INFO_FIELD_NUMBER: _ClassVar[int]
    ability_cooldown: float
    ability_id: int
    ping_data: PingCommonData
    ping_marker_and_sound_info: ChatMsgPingMarkerInfo
    def __init__(
        self,
        ping_data: _Optional[_Union[PingCommonData, _Mapping]] = ...,
        ability_id: _Optional[int] = ...,
        ability_cooldown: _Optional[float] = ...,
        ping_marker_and_sound_info: _Optional[_Union[ChatMsgPingMarkerInfo, str]] = ...,
    ) -> None: ...

class CCitadelUserMsg_BossDamaged(_message.Message):
    __slots__ = ["entity_damaged", "objective_id", "objective_team"]
    ENTITY_DAMAGED_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVE_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVE_TEAM_FIELD_NUMBER: _ClassVar[int]
    entity_damaged: int
    objective_id: int
    objective_team: int
    def __init__(
        self,
        objective_team: _Optional[int] = ...,
        objective_id: _Optional[int] = ...,
        entity_damaged: _Optional[int] = ...,
    ) -> None: ...

class CCitadelUserMsg_BossKilled(_message.Message):
    __slots__ = [
        "bosses_remaining",
        "entity_killed",
        "entity_killed_class",
        "entity_killer",
        "entity_position",
        "gametime",
        "objective_mask_change",
        "objective_team",
    ]
    BOSSES_REMAINING_FIELD_NUMBER: _ClassVar[int]
    ENTITY_KILLED_CLASS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_KILLED_FIELD_NUMBER: _ClassVar[int]
    ENTITY_KILLER_FIELD_NUMBER: _ClassVar[int]
    ENTITY_POSITION_FIELD_NUMBER: _ClassVar[int]
    GAMETIME_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVE_MASK_CHANGE_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVE_TEAM_FIELD_NUMBER: _ClassVar[int]
    bosses_remaining: int
    entity_killed: int
    entity_killed_class: int
    entity_killer: int
    entity_position: _networkbasetypes_pb2.CMsgVector
    gametime: float
    objective_mask_change: int
    objective_team: int
    def __init__(
        self,
        objective_team: _Optional[int] = ...,
        objective_mask_change: _Optional[int] = ...,
        entity_killed: _Optional[int] = ...,
        entity_killed_class: _Optional[int] = ...,
        entity_killer: _Optional[int] = ...,
        gametime: _Optional[float] = ...,
        bosses_remaining: _Optional[int] = ...,
        entity_position: _Optional[
            _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
        ] = ...,
    ) -> None: ...

class CCitadelUserMsg_CallCheaterVote(_message.Message):
    __slots__ = ["player_slot"]
    PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
    player_slot: int
    def __init__(self, player_slot: _Optional[int] = ...) -> None: ...

class CCitadelUserMsg_CameraController(_message.Message):
    __slots__ = [
        "action",
        "approach",
        "context_symbol_id",
        "delay",
        "lag",
        "lerp",
        "maintain",
        "operation",
        "param",
        "param_mode",
        "priority",
        "relative_values",
        "spring",
    ]

    class Approach(_message.Message):
        __slots__ = [
            "acceleration",
            "approach_float",
            "approach_vector",
            "chase_default",
            "default_speed",
            "min_duration",
            "speed",
        ]
        ACCELERATION_FIELD_NUMBER: _ClassVar[int]
        APPROACH_FLOAT_FIELD_NUMBER: _ClassVar[int]
        APPROACH_VECTOR_FIELD_NUMBER: _ClassVar[int]
        CHASE_DEFAULT_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_SPEED_FIELD_NUMBER: _ClassVar[int]
        MIN_DURATION_FIELD_NUMBER: _ClassVar[int]
        SPEED_FIELD_NUMBER: _ClassVar[int]
        acceleration: float
        approach_float: float
        approach_vector: _networkbasetypes_pb2.CMsgVector
        chase_default: bool
        default_speed: float
        min_duration: float
        speed: float
        def __init__(
            self,
            speed: _Optional[float] = ...,
            default_speed: _Optional[float] = ...,
            acceleration: _Optional[float] = ...,
            min_duration: _Optional[float] = ...,
            approach_float: _Optional[float] = ...,
            approach_vector: _Optional[
                _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
            ] = ...,
            chase_default: bool = ...,
        ) -> None: ...

    class Lag(_message.Message):
        __slots__ = [
            "increase_spring_strength_to_keep_target_on_screen",
            "lag_time",
            "max_speed",
            "min_duration",
            "spring_strength",
        ]
        INCREASE_SPRING_STRENGTH_TO_KEEP_TARGET_ON_SCREEN_FIELD_NUMBER: _ClassVar[int]
        LAG_TIME_FIELD_NUMBER: _ClassVar[int]
        MAX_SPEED_FIELD_NUMBER: _ClassVar[int]
        MIN_DURATION_FIELD_NUMBER: _ClassVar[int]
        SPRING_STRENGTH_FIELD_NUMBER: _ClassVar[int]
        increase_spring_strength_to_keep_target_on_screen: bool
        lag_time: float
        max_speed: float
        min_duration: float
        spring_strength: float
        def __init__(
            self,
            min_duration: _Optional[float] = ...,
            lag_time: _Optional[float] = ...,
            max_speed: _Optional[float] = ...,
            spring_strength: _Optional[float] = ...,
            increase_spring_strength_to_keep_target_on_screen: bool = ...,
        ) -> None: ...

    class Lerp(_message.Message):
        __slots__ = [
            "bias",
            "duration",
            "end_float",
            "end_vector",
            "gain",
            "start_float",
            "start_vector",
        ]
        BIAS_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        END_FLOAT_FIELD_NUMBER: _ClassVar[int]
        END_VECTOR_FIELD_NUMBER: _ClassVar[int]
        GAIN_FIELD_NUMBER: _ClassVar[int]
        START_FLOAT_FIELD_NUMBER: _ClassVar[int]
        START_VECTOR_FIELD_NUMBER: _ClassVar[int]
        bias: float
        duration: float
        end_float: float
        end_vector: _networkbasetypes_pb2.CMsgVector
        gain: float
        start_float: float
        start_vector: _networkbasetypes_pb2.CMsgVector
        def __init__(
            self,
            start_float: _Optional[float] = ...,
            start_vector: _Optional[
                _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
            ] = ...,
            end_float: _Optional[float] = ...,
            end_vector: _Optional[
                _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
            ] = ...,
            bias: _Optional[float] = ...,
            gain: _Optional[float] = ...,
            duration: _Optional[float] = ...,
        ) -> None: ...

    class Maintain(_message.Message):
        __slots__ = [
            "duration",
            "maintain_current",
            "maintain_float",
            "maintain_vector",
        ]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        MAINTAIN_CURRENT_FIELD_NUMBER: _ClassVar[int]
        MAINTAIN_FLOAT_FIELD_NUMBER: _ClassVar[int]
        MAINTAIN_VECTOR_FIELD_NUMBER: _ClassVar[int]
        duration: float
        maintain_current: bool
        maintain_float: float
        maintain_vector: _networkbasetypes_pb2.CMsgVector
        def __init__(
            self,
            duration: _Optional[float] = ...,
            maintain_vector: _Optional[
                _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
            ] = ...,
            maintain_float: _Optional[float] = ...,
            maintain_current: bool = ...,
        ) -> None: ...

    class Spring(_message.Message):
        __slots__ = [
            "max_duration",
            "min_speed",
            "spring_strength",
            "target_float",
            "target_vector",
        ]
        MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
        MIN_SPEED_FIELD_NUMBER: _ClassVar[int]
        SPRING_STRENGTH_FIELD_NUMBER: _ClassVar[int]
        TARGET_FLOAT_FIELD_NUMBER: _ClassVar[int]
        TARGET_VECTOR_FIELD_NUMBER: _ClassVar[int]
        max_duration: float
        min_speed: float
        spring_strength: float
        target_float: float
        target_vector: _networkbasetypes_pb2.CMsgVector
        def __init__(
            self,
            spring_strength: _Optional[float] = ...,
            min_speed: _Optional[float] = ...,
            max_duration: _Optional[float] = ...,
            target_float: _Optional[float] = ...,
            target_vector: _Optional[
                _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
            ] = ...,
        ) -> None: ...

    ACTION_FIELD_NUMBER: _ClassVar[int]
    APPROACH_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_SYMBOL_ID_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    LAG_FIELD_NUMBER: _ClassVar[int]
    LERP_FIELD_NUMBER: _ClassVar[int]
    MAINTAIN_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    PARAM_MODE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_VALUES_FIELD_NUMBER: _ClassVar[int]
    SPRING_FIELD_NUMBER: _ClassVar[int]
    action: CameraAction
    approach: CCitadelUserMsg_CameraController.Approach
    context_symbol_id: int
    delay: float
    lag: CCitadelUserMsg_CameraController.Lag
    lerp: CCitadelUserMsg_CameraController.Lerp
    maintain: CCitadelUserMsg_CameraController.Maintain
    operation: CameraOperation
    param: CameraParam
    param_mode: CameraParamMode
    priority: int
    relative_values: bool
    spring: CCitadelUserMsg_CameraController.Spring
    def __init__(
        self,
        action: _Optional[_Union[CameraAction, str]] = ...,
        operation: _Optional[_Union[CameraOperation, str]] = ...,
        param: _Optional[_Union[CameraParam, str]] = ...,
        param_mode: _Optional[_Union[CameraParamMode, str]] = ...,
        delay: _Optional[float] = ...,
        relative_values: bool = ...,
        context_symbol_id: _Optional[int] = ...,
        priority: _Optional[int] = ...,
        maintain: _Optional[
            _Union[CCitadelUserMsg_CameraController.Maintain, _Mapping]
        ] = ...,
        approach: _Optional[
            _Union[CCitadelUserMsg_CameraController.Approach, _Mapping]
        ] = ...,
        spring: _Optional[
            _Union[CCitadelUserMsg_CameraController.Spring, _Mapping]
        ] = ...,
        lerp: _Optional[_Union[CCitadelUserMsg_CameraController.Lerp, _Mapping]] = ...,
        lag: _Optional[_Union[CCitadelUserMsg_CameraController.Lag, _Mapping]] = ...,
    ) -> None: ...

class CCitadelUserMsg_ChatEvent(_message.Message):
    __slots__ = ["player_slots", "type", "values"]
    PLAYER_SLOTS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    player_slots: _containers.RepeatedScalarFieldContainer[int]
    type: ECitadelChatMessage
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(
        self,
        type: _Optional[_Union[ECitadelChatMessage, str]] = ...,
        values: _Optional[_Iterable[int]] = ...,
        player_slots: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class CCitadelUserMsg_ChatMsg(_message.Message):
    __slots__ = ["all_chat", "lane_color", "player_slot", "text"]
    ALL_CHAT_FIELD_NUMBER: _ClassVar[int]
    LANE_COLOR_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    all_chat: bool
    lane_color: _citadel_gcmessages_common_pb2.CMsgLaneColor
    player_slot: int
    text: str
    def __init__(
        self,
        player_slot: _Optional[int] = ...,
        text: _Optional[str] = ...,
        all_chat: bool = ...,
        lane_color: _Optional[
            _Union[_citadel_gcmessages_common_pb2.CMsgLaneColor, str]
        ] = ...,
    ) -> None: ...

class CCitadelUserMsg_ChatWheel(_message.Message):
    __slots__ = [
        "account_id",
        "chat_message_id",
        "hero_id",
        "lane_color",
        "param_1",
        "pawn_entindex",
        "player_slot",
    ]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    HERO_ID_FIELD_NUMBER: _ClassVar[int]
    LANE_COLOR_FIELD_NUMBER: _ClassVar[int]
    PARAM_1_FIELD_NUMBER: _ClassVar[int]
    PAWN_ENTINDEX_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    chat_message_id: int
    hero_id: int
    lane_color: _citadel_gcmessages_common_pb2.CMsgLaneColor
    param_1: str
    pawn_entindex: int
    player_slot: int
    def __init__(
        self,
        chat_message_id: _Optional[int] = ...,
        player_slot: _Optional[int] = ...,
        pawn_entindex: _Optional[int] = ...,
        account_id: _Optional[int] = ...,
        hero_id: _Optional[int] = ...,
        param_1: _Optional[str] = ...,
        lane_color: _Optional[
            _Union[_citadel_gcmessages_common_pb2.CMsgLaneColor, str]
        ] = ...,
    ) -> None: ...

class CCitadelUserMsg_DeathReplayData(_message.Message):
    __slots__ = ["damage_summary", "killer_inflictor", "killer_scorer"]
    DAMAGE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    KILLER_INFLICTOR_FIELD_NUMBER: _ClassVar[int]
    KILLER_SCORER_FIELD_NUMBER: _ClassVar[int]
    damage_summary: CCitadelUserMsg_RecentDamageSummary
    killer_inflictor: int
    killer_scorer: int
    def __init__(
        self,
        killer_scorer: _Optional[int] = ...,
        killer_inflictor: _Optional[int] = ...,
        damage_summary: _Optional[
            _Union[CCitadelUserMsg_RecentDamageSummary, _Mapping]
        ] = ...,
    ) -> None: ...

class CCitadelUserMsg_ForceShopClosed(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CCitadelUserMsg_GetDamageStatsResponse(_message.Message):
    __slots__ = ["ability_name", "damage", "healing", "player_slot"]

    class StatType(_message.Message):
        __slots__ = ["target_player_slot", "value"]
        TARGET_PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        target_player_slot: _containers.RepeatedScalarFieldContainer[int]
        value: _containers.RepeatedScalarFieldContainer[int]
        def __init__(
            self,
            target_player_slot: _Optional[_Iterable[int]] = ...,
            value: _Optional[_Iterable[int]] = ...,
        ) -> None: ...

    ABILITY_NAME_FIELD_NUMBER: _ClassVar[int]
    DAMAGE_FIELD_NUMBER: _ClassVar[int]
    HEALING_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
    ability_name: str
    damage: CCitadelUserMsg_GetDamageStatsResponse.StatType
    healing: CCitadelUserMsg_GetDamageStatsResponse.StatType
    player_slot: int
    def __init__(
        self,
        player_slot: _Optional[int] = ...,
        ability_name: _Optional[str] = ...,
        damage: _Optional[
            _Union[CCitadelUserMsg_GetDamageStatsResponse.StatType, _Mapping]
        ] = ...,
        healing: _Optional[
            _Union[CCitadelUserMsg_GetDamageStatsResponse.StatType, _Mapping]
        ] = ...,
    ) -> None: ...

class CCitadelUserMsg_GoldHistory(_message.Message):
    __slots__ = ["entindex_player", "minute_records"]

    class GoldRecord(_message.Message):
        __slots__ = ["currency_source", "events", "gold"]
        CURRENCY_SOURCE_FIELD_NUMBER: _ClassVar[int]
        EVENTS_FIELD_NUMBER: _ClassVar[int]
        GOLD_FIELD_NUMBER: _ClassVar[int]
        currency_source: int
        events: int
        gold: int
        def __init__(
            self,
            currency_source: _Optional[int] = ...,
            gold: _Optional[int] = ...,
            events: _Optional[int] = ...,
        ) -> None: ...

    class MinuteRecord(_message.Message):
        __slots__ = ["gold_records", "match_minute"]
        GOLD_RECORDS_FIELD_NUMBER: _ClassVar[int]
        MATCH_MINUTE_FIELD_NUMBER: _ClassVar[int]
        gold_records: _containers.RepeatedCompositeFieldContainer[
            CCitadelUserMsg_GoldHistory.GoldRecord
        ]
        match_minute: int
        def __init__(
            self,
            match_minute: _Optional[int] = ...,
            gold_records: _Optional[
                _Iterable[_Union[CCitadelUserMsg_GoldHistory.GoldRecord, _Mapping]]
            ] = ...,
        ) -> None: ...

    ENTINDEX_PLAYER_FIELD_NUMBER: _ClassVar[int]
    MINUTE_RECORDS_FIELD_NUMBER: _ClassVar[int]
    entindex_player: int
    minute_records: _containers.RepeatedCompositeFieldContainer[
        CCitadelUserMsg_GoldHistory.MinuteRecord
    ]
    def __init__(
        self,
        entindex_player: _Optional[int] = ...,
        minute_records: _Optional[
            _Iterable[_Union[CCitadelUserMsg_GoldHistory.MinuteRecord, _Mapping]]
        ] = ...,
    ) -> None: ...

class CCitadelUserMsg_HeroKilled(_message.Message):
    __slots__ = [
        "entindex_assisters",
        "entindex_attacker",
        "entindex_inflictor",
        "entindex_scorer",
        "entindex_victim",
        "respawn_reason",
        "victim_team_number",
    ]
    ENTINDEX_ASSISTERS_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_ATTACKER_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_INFLICTOR_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_SCORER_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_VICTIM_FIELD_NUMBER: _ClassVar[int]
    RESPAWN_REASON_FIELD_NUMBER: _ClassVar[int]
    VICTIM_TEAM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    entindex_assisters: _containers.RepeatedScalarFieldContainer[int]
    entindex_attacker: int
    entindex_inflictor: int
    entindex_scorer: int
    entindex_victim: int
    respawn_reason: int
    victim_team_number: int
    def __init__(
        self,
        entindex_victim: _Optional[int] = ...,
        entindex_inflictor: _Optional[int] = ...,
        entindex_attacker: _Optional[int] = ...,
        entindex_assisters: _Optional[_Iterable[int]] = ...,
        entindex_scorer: _Optional[int] = ...,
        respawn_reason: _Optional[int] = ...,
        victim_team_number: _Optional[int] = ...,
    ) -> None: ...

class CCitadelUserMsg_KillStreak(_message.Message):
    __slots__ = ["is_first_blood", "num_kills", "player_pawn"]
    IS_FIRST_BLOOD_FIELD_NUMBER: _ClassVar[int]
    NUM_KILLS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_PAWN_FIELD_NUMBER: _ClassVar[int]
    is_first_blood: bool
    num_kills: int
    player_pawn: int
    def __init__(
        self,
        player_pawn: _Optional[int] = ...,
        num_kills: _Optional[int] = ...,
        is_first_blood: bool = ...,
    ) -> None: ...

class CCitadelUserMsg_MapLine(_message.Message):
    __slots__ = ["mapline", "sender_player_slot"]
    MAPLINE_FIELD_NUMBER: _ClassVar[int]
    SENDER_PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
    mapline: _citadel_gcmessages_common_pb2.CMsgMapLine
    sender_player_slot: int
    def __init__(
        self,
        sender_player_slot: _Optional[int] = ...,
        mapline: _Optional[
            _Union[_citadel_gcmessages_common_pb2.CMsgMapLine, _Mapping]
        ] = ...,
    ) -> None: ...

class CCitadelUserMsg_MapPing(_message.Message):
    __slots__ = [
        "event_type",
        "is_blind_ping",
        "is_minimap_ping",
        "ping_data",
        "ping_marker_and_sound_info",
        "pinged_enemy_entity",
        "pinged_entity_class",
        "pinged_hero_name",
    ]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_BLIND_PING_FIELD_NUMBER: _ClassVar[int]
    IS_MINIMAP_PING_FIELD_NUMBER: _ClassVar[int]
    PINGED_ENEMY_ENTITY_FIELD_NUMBER: _ClassVar[int]
    PINGED_ENTITY_CLASS_FIELD_NUMBER: _ClassVar[int]
    PINGED_HERO_NAME_FIELD_NUMBER: _ClassVar[int]
    PING_DATA_FIELD_NUMBER: _ClassVar[int]
    PING_MARKER_AND_SOUND_INFO_FIELD_NUMBER: _ClassVar[int]
    event_type: int
    is_blind_ping: bool
    is_minimap_ping: bool
    ping_data: PingCommonData
    ping_marker_and_sound_info: ChatMsgPingMarkerInfo
    pinged_enemy_entity: bool
    pinged_entity_class: int
    pinged_hero_name: str
    def __init__(
        self,
        ping_data: _Optional[_Union[PingCommonData, _Mapping]] = ...,
        event_type: _Optional[int] = ...,
        ping_marker_and_sound_info: _Optional[_Union[ChatMsgPingMarkerInfo, str]] = ...,
        pinged_enemy_entity: bool = ...,
        pinged_entity_class: _Optional[int] = ...,
        is_minimap_ping: bool = ...,
        pinged_hero_name: _Optional[str] = ...,
        is_blind_ping: bool = ...,
    ) -> None: ...

class CCitadelUserMsg_MidBossSpawned(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CCitadelUserMsg_ObstructedShotFired(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CCitadelUserMsg_ParticipantSetLibraryStackFields(_message.Message):
    __slots__ = ["event", "player_slots"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SLOTS_FIELD_NUMBER: _ClassVar[int]
    event: _gameevents_pb2.CMsgSosSetLibraryStackFields
    player_slots: _containers.RepeatedScalarFieldContainer[int]
    def __init__(
        self,
        event: _Optional[
            _Union[_gameevents_pb2.CMsgSosSetLibraryStackFields, _Mapping]
        ] = ...,
        player_slots: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class CCitadelUserMsg_ParticipantSetSoundEventParams(_message.Message):
    __slots__ = ["event", "player_slots"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SLOTS_FIELD_NUMBER: _ClassVar[int]
    event: _gameevents_pb2.CMsgSosSetSoundEventParams
    player_slots: _containers.RepeatedScalarFieldContainer[int]
    def __init__(
        self,
        event: _Optional[
            _Union[_gameevents_pb2.CMsgSosSetSoundEventParams, _Mapping]
        ] = ...,
        player_slots: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class CCitadelUserMsg_ParticipantStartSoundEvent(_message.Message):
    __slots__ = ["event", "player_slots"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SLOTS_FIELD_NUMBER: _ClassVar[int]
    event: _gameevents_pb2.CMsgSosStartSoundEvent
    player_slots: _containers.RepeatedScalarFieldContainer[int]
    def __init__(
        self,
        event: _Optional[
            _Union[_gameevents_pb2.CMsgSosStartSoundEvent, _Mapping]
        ] = ...,
        player_slots: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class CCitadelUserMsg_ParticipantStopSoundEvent(_message.Message):
    __slots__ = ["event", "player_slots"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SLOTS_FIELD_NUMBER: _ClassVar[int]
    event: _gameevents_pb2.CMsgSosStopSoundEvent
    player_slots: _containers.RepeatedScalarFieldContainer[int]
    def __init__(
        self,
        event: _Optional[_Union[_gameevents_pb2.CMsgSosStopSoundEvent, _Mapping]] = ...,
        player_slots: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class CCitadelUserMsg_ParticipantStopSoundEventHash(_message.Message):
    __slots__ = ["event", "player_slots"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SLOTS_FIELD_NUMBER: _ClassVar[int]
    event: _gameevents_pb2.CMsgSosStopSoundEventHash
    player_slots: _containers.RepeatedScalarFieldContainer[int]
    def __init__(
        self,
        event: _Optional[
            _Union[_gameevents_pb2.CMsgSosStopSoundEventHash, _Mapping]
        ] = ...,
        player_slots: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class CCitadelUserMsg_PingWheel(_message.Message):
    __slots__ = ["ping_data", "ping_wheel_option_id"]
    PING_DATA_FIELD_NUMBER: _ClassVar[int]
    PING_WHEEL_OPTION_ID_FIELD_NUMBER: _ClassVar[int]
    ping_data: PingCommonData
    ping_wheel_option_id: int
    def __init__(
        self,
        ping_data: _Optional[_Union[PingCommonData, _Mapping]] = ...,
        ping_wheel_option_id: _Optional[int] = ...,
    ) -> None: ...

class CCitadelUserMsg_PlayerLifetimeStatInfo(_message.Message):
    __slots__ = ["end_of_match", "is_official_match", "match_id", "stats"]

    class Stat(_message.Message):
        __slots__ = [
            "lifetime_value",
            "match_total",
            "prev_lifetime_max",
            "priority",
            "stat_name",
            "stat_type",
            "stat_type_id",
        ]
        LIFETIME_VALUE_FIELD_NUMBER: _ClassVar[int]
        MATCH_TOTAL_FIELD_NUMBER: _ClassVar[int]
        PREV_LIFETIME_MAX_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_FIELD_NUMBER: _ClassVar[int]
        STAT_NAME_FIELD_NUMBER: _ClassVar[int]
        STAT_TYPE_FIELD_NUMBER: _ClassVar[int]
        STAT_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
        lifetime_value: int
        match_total: int
        prev_lifetime_max: int
        priority: int
        stat_name: str
        stat_type: int
        stat_type_id: int
        def __init__(
            self,
            stat_name: _Optional[str] = ...,
            match_total: _Optional[int] = ...,
            lifetime_value: _Optional[int] = ...,
            priority: _Optional[int] = ...,
            prev_lifetime_max: _Optional[int] = ...,
            stat_type: _Optional[int] = ...,
            stat_type_id: _Optional[int] = ...,
        ) -> None: ...

    END_OF_MATCH_FIELD_NUMBER: _ClassVar[int]
    IS_OFFICIAL_MATCH_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    end_of_match: bool
    is_official_match: bool
    match_id: int
    stats: _containers.RepeatedCompositeFieldContainer[
        CCitadelUserMsg_PlayerLifetimeStatInfo.Stat
    ]
    def __init__(
        self,
        stats: _Optional[
            _Iterable[_Union[CCitadelUserMsg_PlayerLifetimeStatInfo.Stat, _Mapping]]
        ] = ...,
        match_id: _Optional[int] = ...,
        end_of_match: bool = ...,
        is_official_match: bool = ...,
    ) -> None: ...

class CCitadelUserMsg_PlayerRespawned(_message.Message):
    __slots__ = ["facing_yaw", "player_pawn"]
    FACING_YAW_FIELD_NUMBER: _ClassVar[int]
    PLAYER_PAWN_FIELD_NUMBER: _ClassVar[int]
    facing_yaw: float
    player_pawn: int
    def __init__(
        self, player_pawn: _Optional[int] = ..., facing_yaw: _Optional[float] = ...
    ) -> None: ...

class CCitadelUserMsg_PostMatchDetails(_message.Message):
    __slots__ = ["match_details"]
    MATCH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    match_details: bytes
    def __init__(self, match_details: _Optional[bytes] = ...) -> None: ...

class CCitadelUserMsg_PostProcessingAnim(_message.Message):
    __slots__ = [
        "clear_all_states",
        "entindex_owner",
        "fade_in_time",
        "fade_out_time",
        "hold_time",
        "scale",
        "start_time",
        "state",
    ]
    CLEAR_ALL_STATES_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_OWNER_FIELD_NUMBER: _ClassVar[int]
    FADE_IN_TIME_FIELD_NUMBER: _ClassVar[int]
    FADE_OUT_TIME_FIELD_NUMBER: _ClassVar[int]
    HOLD_TIME_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    clear_all_states: bool
    entindex_owner: int
    fade_in_time: float
    fade_out_time: float
    hold_time: float
    scale: float
    start_time: float
    state: PostProcessingGameStates
    def __init__(
        self,
        entindex_owner: _Optional[int] = ...,
        clear_all_states: bool = ...,
        state: _Optional[_Union[PostProcessingGameStates, str]] = ...,
        start_time: _Optional[float] = ...,
        fade_in_time: _Optional[float] = ...,
        hold_time: _Optional[float] = ...,
        fade_out_time: _Optional[float] = ...,
        scale: _Optional[float] = ...,
    ) -> None: ...

class CCitadelUserMsg_QuickResponse(_message.Message):
    __slots__ = [
        "lane_color",
        "ping_data",
        "responding_to_ping_message_id",
        "responding_to_player_slot",
    ]
    LANE_COLOR_FIELD_NUMBER: _ClassVar[int]
    PING_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONDING_TO_PING_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONDING_TO_PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
    lane_color: _citadel_gcmessages_common_pb2.CMsgLaneColor
    ping_data: PingCommonData
    responding_to_ping_message_id: int
    responding_to_player_slot: int
    def __init__(
        self,
        ping_data: _Optional[_Union[PingCommonData, _Mapping]] = ...,
        responding_to_ping_message_id: _Optional[int] = ...,
        responding_to_player_slot: _Optional[int] = ...,
        lane_color: _Optional[
            _Union[_citadel_gcmessages_common_pb2.CMsgLaneColor, str]
        ] = ...,
    ) -> None: ...

class CCitadelUserMsg_RecentDamageSummary(_message.Message):
    __slots__ = [
        "damage_records",
        "end_time",
        "lost_gold",
        "modifier_records",
        "player_slot",
        "start_time",
        "total_damage",
    ]

    class DamageRecord(_message.Message):
        __slots__ = [
            "ability_id",
            "attacker_class",
            "damage",
            "damage_absorbed",
            "damage_type",
            "hero_id",
            "hits",
            "is_killing_blow",
            "victim_hero_id",
        ]
        ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
        ATTACKER_CLASS_FIELD_NUMBER: _ClassVar[int]
        DAMAGE_ABSORBED_FIELD_NUMBER: _ClassVar[int]
        DAMAGE_FIELD_NUMBER: _ClassVar[int]
        DAMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        HERO_ID_FIELD_NUMBER: _ClassVar[int]
        HITS_FIELD_NUMBER: _ClassVar[int]
        IS_KILLING_BLOW_FIELD_NUMBER: _ClassVar[int]
        VICTIM_HERO_ID_FIELD_NUMBER: _ClassVar[int]
        ability_id: int
        attacker_class: int
        damage: int
        damage_absorbed: int
        damage_type: int
        hero_id: int
        hits: int
        is_killing_blow: bool
        victim_hero_id: int
        def __init__(
            self,
            damage: _Optional[int] = ...,
            hits: _Optional[int] = ...,
            damage_type: _Optional[int] = ...,
            hero_id: _Optional[int] = ...,
            ability_id: _Optional[int] = ...,
            attacker_class: _Optional[int] = ...,
            damage_absorbed: _Optional[int] = ...,
            is_killing_blow: bool = ...,
            victim_hero_id: _Optional[int] = ...,
        ) -> None: ...

    class ModifierRecord(_message.Message):
        __slots__ = [
            "ability_id",
            "debuff",
            "end_time",
            "entindex_caster",
            "modifier_type_id",
            "start_time",
        ]
        ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
        DEBUFF_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        ENTINDEX_CASTER_FIELD_NUMBER: _ClassVar[int]
        MODIFIER_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        ability_id: int
        debuff: bool
        end_time: float
        entindex_caster: int
        modifier_type_id: int
        start_time: float
        def __init__(
            self,
            ability_id: _Optional[int] = ...,
            modifier_type_id: _Optional[int] = ...,
            entindex_caster: _Optional[int] = ...,
            start_time: _Optional[float] = ...,
            end_time: _Optional[float] = ...,
            debuff: bool = ...,
        ) -> None: ...

    DAMAGE_RECORDS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    LOST_GOLD_FIELD_NUMBER: _ClassVar[int]
    MODIFIER_RECORDS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DAMAGE_FIELD_NUMBER: _ClassVar[int]
    damage_records: _containers.RepeatedCompositeFieldContainer[
        CCitadelUserMsg_RecentDamageSummary.DamageRecord
    ]
    end_time: float
    lost_gold: int
    modifier_records: _containers.RepeatedCompositeFieldContainer[
        CCitadelUserMsg_RecentDamageSummary.ModifierRecord
    ]
    player_slot: int
    start_time: float
    total_damage: int
    def __init__(
        self,
        player_slot: _Optional[int] = ...,
        damage_records: _Optional[
            _Iterable[
                _Union[CCitadelUserMsg_RecentDamageSummary.DamageRecord, _Mapping]
            ]
        ] = ...,
        start_time: _Optional[float] = ...,
        end_time: _Optional[float] = ...,
        total_damage: _Optional[int] = ...,
        lost_gold: _Optional[int] = ...,
        modifier_records: _Optional[
            _Iterable[
                _Union[CCitadelUserMsg_RecentDamageSummary.ModifierRecord, _Mapping]
            ]
        ] = ...,
    ) -> None: ...

class CCitadelUserMsg_RejuvStatus(_message.Message):
    __slots__ = ["event_type", "killing_team", "player_pawn", "user_team"]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    KILLING_TEAM_FIELD_NUMBER: _ClassVar[int]
    PLAYER_PAWN_FIELD_NUMBER: _ClassVar[int]
    USER_TEAM_FIELD_NUMBER: _ClassVar[int]
    event_type: int
    killing_team: int
    player_pawn: int
    user_team: int
    def __init__(
        self,
        killing_team: _Optional[int] = ...,
        player_pawn: _Optional[int] = ...,
        user_team: _Optional[int] = ...,
        event_type: _Optional[int] = ...,
    ) -> None: ...

class CCitadelUserMsg_ReturnIdol(_message.Message):
    __slots__ = ["location_enabled", "location_index", "return_location"]
    LOCATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LOCATION_INDEX_FIELD_NUMBER: _ClassVar[int]
    RETURN_LOCATION_FIELD_NUMBER: _ClassVar[int]
    location_enabled: bool
    location_index: int
    return_location: _networkbasetypes_pb2.CMsgVector
    def __init__(
        self,
        location_index: _Optional[int] = ...,
        return_location: _Optional[
            _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
        ] = ...,
        location_enabled: bool = ...,
    ) -> None: ...

class CCitadelUserMsg_SetClientCameraAngles(_message.Message):
    __slots__ = ["camera_angles", "player_slot"]
    CAMERA_ANGLES_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
    camera_angles: _networkbasetypes_pb2.CMsgQAngle
    player_slot: int
    def __init__(
        self,
        player_slot: _Optional[int] = ...,
        camera_angles: _Optional[
            _Union[_networkbasetypes_pb2.CMsgQAngle, _Mapping]
        ] = ...,
    ) -> None: ...

class CCitadelUserMsg_SpectatorTeamChanged(_message.Message):
    __slots__ = ["teamnumber"]
    TEAMNUMBER_FIELD_NUMBER: _ClassVar[int]
    teamnumber: int
    def __init__(self, teamnumber: _Optional[int] = ...) -> None: ...

class CCitadelUserMsg_StaminaDrained(_message.Message):
    __slots__ = ["entindex_victim", "stamina_drained"]
    ENTINDEX_VICTIM_FIELD_NUMBER: _ClassVar[int]
    STAMINA_DRAINED_FIELD_NUMBER: _ClassVar[int]
    entindex_victim: int
    stamina_drained: int
    def __init__(
        self,
        entindex_victim: _Optional[int] = ...,
        stamina_drained: _Optional[int] = ...,
    ) -> None: ...

class CCitadelUserMsg_TeamMsg(_message.Message):
    __slots__ = ["event_type", "lane_color", "player_controller", "team_number"]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    LANE_COLOR_FIELD_NUMBER: _ClassVar[int]
    PLAYER_CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    TEAM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    event_type: int
    lane_color: int
    player_controller: int
    team_number: int
    def __init__(
        self,
        event_type: _Optional[int] = ...,
        team_number: _Optional[int] = ...,
        lane_color: _Optional[int] = ...,
        player_controller: _Optional[int] = ...,
    ) -> None: ...

class CCitadelUserMsg_TeamRewards(_message.Message):
    __slots__ = ["gold", "winner", "xp"]
    GOLD_FIELD_NUMBER: _ClassVar[int]
    WINNER_FIELD_NUMBER: _ClassVar[int]
    XP_FIELD_NUMBER: _ClassVar[int]
    gold: int
    winner: bool
    xp: int
    def __init__(
        self, xp: _Optional[int] = ..., gold: _Optional[int] = ..., winner: bool = ...
    ) -> None: ...

class CCitadelUserMsg_TriggerDamageFlash(_message.Message):
    __slots__ = [
        "entindex_flash_attacker",
        "entindex_flash_hitgroup",
        "entindex_flash_victim",
        "flash_flags",
        "flash_position",
        "flash_type",
        "flash_value",
    ]
    ENTINDEX_FLASH_ATTACKER_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_FLASH_HITGROUP_FIELD_NUMBER: _ClassVar[int]
    ENTINDEX_FLASH_VICTIM_FIELD_NUMBER: _ClassVar[int]
    FLASH_FLAGS_FIELD_NUMBER: _ClassVar[int]
    FLASH_POSITION_FIELD_NUMBER: _ClassVar[int]
    FLASH_TYPE_FIELD_NUMBER: _ClassVar[int]
    FLASH_VALUE_FIELD_NUMBER: _ClassVar[int]
    entindex_flash_attacker: int
    entindex_flash_hitgroup: int
    entindex_flash_victim: int
    flash_flags: int
    flash_position: _networkbasetypes_pb2.CMsgVector
    flash_type: int
    flash_value: int
    def __init__(
        self,
        entindex_flash_victim: _Optional[int] = ...,
        entindex_flash_attacker: _Optional[int] = ...,
        entindex_flash_hitgroup: _Optional[int] = ...,
        flash_value: _Optional[int] = ...,
        flash_type: _Optional[int] = ...,
        flash_flags: _Optional[int] = ...,
        flash_position: _Optional[
            _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
        ] = ...,
    ) -> None: ...

class CUserMessageEmpty(_message.Message):
    __slots__ = ["empty"]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    empty: int
    def __init__(self, empty: _Optional[int] = ...) -> None: ...

class PingCommonData(_message.Message):
    __slots__ = [
        "cooldown_time",
        "entity_index",
        "ping_location",
        "ping_message_id",
        "response_chosen",
        "sender_player_slot",
        "speech_concept",
    ]
    COOLDOWN_TIME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_INDEX_FIELD_NUMBER: _ClassVar[int]
    PING_LOCATION_FIELD_NUMBER: _ClassVar[int]
    PING_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_CHOSEN_FIELD_NUMBER: _ClassVar[int]
    SENDER_PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
    SPEECH_CONCEPT_FIELD_NUMBER: _ClassVar[int]
    cooldown_time: float
    entity_index: int
    ping_location: _networkbasetypes_pb2.CMsgVector
    ping_message_id: int
    response_chosen: str
    sender_player_slot: int
    speech_concept: int
    def __init__(
        self,
        ping_message_id: _Optional[int] = ...,
        ping_location: _Optional[
            _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
        ] = ...,
        entity_index: _Optional[int] = ...,
        sender_player_slot: _Optional[int] = ...,
        speech_concept: _Optional[int] = ...,
        response_chosen: _Optional[str] = ...,
        cooldown_time: _Optional[float] = ...,
    ) -> None: ...

class CitadelUserMessageIds(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class CitadelEntityMessageIds(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ChatMsgPingMarkerInfo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class CameraOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class CameraParam(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class CameraParamMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class CameraAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ECitadelChatMessage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class PostProcessingGameStates(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
