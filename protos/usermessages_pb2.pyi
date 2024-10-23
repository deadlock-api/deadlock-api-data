from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

import networkbasetypes_pb2 as _networkbasetypes_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message

DESCRIPTOR: _descriptor.FileDescriptor
EM_DoSpark: EBaseEntityMessages
EM_FixAngle: EBaseEntityMessages
EM_PlayJingle: EBaseEntityMessages
EM_PropagateForce: EBaseEntityMessages
EM_RemoveAllDecals: EBaseEntityMessages
EM_ScreenOverlay: EBaseEntityMessages
GAME_PARTICLE_MANAGER_EVENT_ADD_MODELLIST_OVERRIDE_ELEMENT: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_CAN_FREEZE: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_CHANGE_CONTROL_POINT_ATTACHMENT: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_CLEAR_MODELLIST_OVERRIDE: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_CREATE: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_CREATE_PHYSICS_SIM: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_DESTROY: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_DESTROY_INVOLVING: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_DESTROY_NAMED: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_DESTROY_PHYSICS_SIM: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_FREEZE_INVOLVING: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_FREEZE_TRANSITION_OVERRIDE: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_FROZEN: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_LATENCY: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_RELEASE: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_SET_CONTROL_POINT_MODEL: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_SET_CONTROL_POINT_SNAPSHOT: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_SET_FOW_PROPERTIES: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_SET_MATERIAL_OVERRIDE: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_SET_NAMED_VALUE_CONTEXT: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_SET_SCENE_OBJECT_GENERIC_FLAG: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_SET_SCENE_OBJECT_TINT_AND_DESAT: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_SET_SHOULD_CHECK_FOW: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_SET_TEXT: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_SET_TEXTURE_ATTRIBUTE: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_SET_VDATA: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_SHOULD_DRAW: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_SKIP_TO_TIME: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_UPDATE: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_UPDATE_ENT: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_UPDATE_ENTITY_POSITION: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_UPDATE_FALLBACK: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_UPDATE_FORWARD: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_UPDATE_OFFSET: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_UPDATE_ORIENTATION: PARTICLE_MESSAGE
GAME_PARTICLE_MANAGER_EVENT_UPDATE_TRANSFORM: PARTICLE_MESSAGE
ROLL_CREDITS: eRollType
ROLL_LATE_JOIN_LOGO: eRollType
ROLL_NONE: eRollType
ROLL_OUTTRO: eRollType
ROLL_STATS: eRollType
UM_AchievementEvent: EBaseUserMessages
UM_AmmoDenied: EBaseUserMessages
UM_AnimGraphUpdate: EBaseUserMessages
UM_AudioParameter: EBaseUserMessages
UM_CameraTransition: EBaseUserMessages
UM_CloseCaption: EBaseUserMessages
UM_CloseCaptionDirect: EBaseUserMessages
UM_CloseCaptionPlaceholder: EBaseUserMessages
UM_ColoredText: EBaseUserMessages
UM_CommandQueueState: EBaseUserMessages
UM_CreditsMsg: EBaseUserMessages
UM_CurrentTimescale: EBaseUserMessages
UM_CustomGameEvent: EBaseUserMessages
UM_DesiredTimescale: EBaseUserMessages
UM_DiagnosticResponse: EBaseUserMessages
UM_DllStatusResponse: EBaseUserMessages
UM_ExtraUserData: EBaseUserMessages
UM_Fade: EBaseUserMessages
UM_GameTitle: EBaseUserMessages
UM_HapticsManagerEffect: EBaseUserMessages
UM_HapticsManagerPulse: EBaseUserMessages
UM_HudError: EBaseUserMessages
UM_HudMsg: EBaseUserMessages
UM_HudText: EBaseUserMessages
UM_InventoryResponse: EBaseUserMessages
UM_ItemPickup: EBaseUserMessages
UM_LagCompensationError: EBaseUserMessages
UM_MAX_BASE: EBaseUserMessages
UM_NotifyResponseFound: EBaseUserMessages
UM_ParticleManager: EBaseUserMessages
UM_PlayResponseConditional: EBaseUserMessages
UM_RequestDiagnostic: EBaseUserMessages
UM_RequestDllStatus: EBaseUserMessages
UM_RequestInventory: EBaseUserMessages
UM_RequestState: EBaseUserMessages
UM_RequestUtilAction: EBaseUserMessages
UM_ResetHUD: EBaseUserMessages
UM_Rumble: EBaseUserMessages
UM_SayText: EBaseUserMessages
UM_SayText2: EBaseUserMessages
UM_SayTextChannel: EBaseUserMessages
UM_ScreenTilt: EBaseUserMessages
UM_SendAudio: EBaseUserMessages
UM_ServerFrameTime: EBaseUserMessages
UM_Shake: EBaseUserMessages
UM_ShakeDir: EBaseUserMessages
UM_ShowMenu: EBaseUserMessages
UM_TextMsg: EBaseUserMessages
UM_UpdateCssClasses: EBaseUserMessages
UM_UtilActionResponse: EBaseUserMessages
UM_VoiceMask: EBaseUserMessages
UM_WaterShake: EBaseUserMessages
VR_HAND_HAPTIC_PULSE_LIGHT: EHapticPulseType
VR_HAND_HAPTIC_PULSE_MEDIUM: EHapticPulseType
VR_HAND_HAPTIC_PULSE_STRONG: EHapticPulseType

class CEntityMessageDoSpark(_message.Message):
    __slots__ = [
        "beams",
        "color",
        "duration",
        "entity_msg",
        "entityindex",
        "origin",
        "radius",
        "thick",
    ]
    BEAMS_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ENTITYINDEX_FIELD_NUMBER: _ClassVar[int]
    ENTITY_MSG_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    THICK_FIELD_NUMBER: _ClassVar[int]
    beams: int
    color: int
    duration: float
    entity_msg: _networkbasetypes_pb2.CEntityMsg
    entityindex: int
    origin: _networkbasetypes_pb2.CMsgVector
    radius: float
    thick: float
    def __init__(
        self,
        origin: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...,
        entityindex: _Optional[int] = ...,
        radius: _Optional[float] = ...,
        color: _Optional[int] = ...,
        beams: _Optional[int] = ...,
        thick: _Optional[float] = ...,
        duration: _Optional[float] = ...,
        entity_msg: _Optional[_Union[_networkbasetypes_pb2.CEntityMsg, _Mapping]] = ...,
    ) -> None: ...

class CEntityMessageFixAngle(_message.Message):
    __slots__ = ["angle", "entity_msg", "relative"]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_MSG_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_FIELD_NUMBER: _ClassVar[int]
    angle: _networkbasetypes_pb2.CMsgQAngle
    entity_msg: _networkbasetypes_pb2.CEntityMsg
    relative: bool
    def __init__(
        self,
        relative: bool = ...,
        angle: _Optional[_Union[_networkbasetypes_pb2.CMsgQAngle, _Mapping]] = ...,
        entity_msg: _Optional[_Union[_networkbasetypes_pb2.CEntityMsg, _Mapping]] = ...,
    ) -> None: ...

class CEntityMessagePlayJingle(_message.Message):
    __slots__ = ["entity_msg"]
    ENTITY_MSG_FIELD_NUMBER: _ClassVar[int]
    entity_msg: _networkbasetypes_pb2.CEntityMsg
    def __init__(
        self,
        entity_msg: _Optional[_Union[_networkbasetypes_pb2.CEntityMsg, _Mapping]] = ...,
    ) -> None: ...

class CEntityMessagePropagateForce(_message.Message):
    __slots__ = ["entity_msg", "impulse"]
    ENTITY_MSG_FIELD_NUMBER: _ClassVar[int]
    IMPULSE_FIELD_NUMBER: _ClassVar[int]
    entity_msg: _networkbasetypes_pb2.CEntityMsg
    impulse: _networkbasetypes_pb2.CMsgVector
    def __init__(
        self,
        impulse: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...,
        entity_msg: _Optional[_Union[_networkbasetypes_pb2.CEntityMsg, _Mapping]] = ...,
    ) -> None: ...

class CEntityMessageRemoveAllDecals(_message.Message):
    __slots__ = ["entity_msg", "remove_decals"]
    ENTITY_MSG_FIELD_NUMBER: _ClassVar[int]
    REMOVE_DECALS_FIELD_NUMBER: _ClassVar[int]
    entity_msg: _networkbasetypes_pb2.CEntityMsg
    remove_decals: bool
    def __init__(
        self,
        remove_decals: bool = ...,
        entity_msg: _Optional[_Union[_networkbasetypes_pb2.CEntityMsg, _Mapping]] = ...,
    ) -> None: ...

class CEntityMessageScreenOverlay(_message.Message):
    __slots__ = ["entity_msg", "start_effect"]
    ENTITY_MSG_FIELD_NUMBER: _ClassVar[int]
    START_EFFECT_FIELD_NUMBER: _ClassVar[int]
    entity_msg: _networkbasetypes_pb2.CEntityMsg
    start_effect: bool
    def __init__(
        self,
        start_effect: bool = ...,
        entity_msg: _Optional[_Union[_networkbasetypes_pb2.CEntityMsg, _Mapping]] = ...,
    ) -> None: ...

class CUserMessageAchievementEvent(_message.Message):
    __slots__ = ["achievement"]
    ACHIEVEMENT_FIELD_NUMBER: _ClassVar[int]
    achievement: int
    def __init__(self, achievement: _Optional[int] = ...) -> None: ...

class CUserMessageAmmoDenied(_message.Message):
    __slots__ = ["ammo_id"]
    AMMO_ID_FIELD_NUMBER: _ClassVar[int]
    ammo_id: int
    def __init__(self, ammo_id: _Optional[int] = ...) -> None: ...

class CUserMessageAnimStateGraphState(_message.Message):
    __slots__ = ["data", "entity_index"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ENTITY_INDEX_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    entity_index: int
    def __init__(
        self, entity_index: _Optional[int] = ..., data: _Optional[bytes] = ...
    ) -> None: ...

class CUserMessageAudioParameter(_message.Message):
    __slots__ = ["int_value", "name_hash_code", "parameter_type", "value"]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    NAME_HASH_CODE_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    int_value: int
    name_hash_code: int
    parameter_type: int
    value: float
    def __init__(
        self,
        parameter_type: _Optional[int] = ...,
        name_hash_code: _Optional[int] = ...,
        value: _Optional[float] = ...,
        int_value: _Optional[int] = ...,
    ) -> None: ...

class CUserMessageCameraTransition(_message.Message):
    __slots__ = ["camera_type", "duration", "params_data_driven"]

    class Transition_DataDriven(_message.Message):
        __slots__ = ["attach_ent_index", "duration", "filename"]
        ATTACH_ENT_INDEX_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        FILENAME_FIELD_NUMBER: _ClassVar[int]
        attach_ent_index: int
        duration: float
        filename: str
        def __init__(
            self,
            filename: _Optional[str] = ...,
            attach_ent_index: _Optional[int] = ...,
            duration: _Optional[float] = ...,
        ) -> None: ...

    CAMERA_TYPE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    PARAMS_DATA_DRIVEN_FIELD_NUMBER: _ClassVar[int]
    camera_type: int
    duration: float
    params_data_driven: CUserMessageCameraTransition.Transition_DataDriven
    def __init__(
        self,
        camera_type: _Optional[int] = ...,
        duration: _Optional[float] = ...,
        params_data_driven: _Optional[
            _Union[CUserMessageCameraTransition.Transition_DataDriven, _Mapping]
        ] = ...,
    ) -> None: ...

class CUserMessageCloseCaption(_message.Message):
    __slots__ = ["duration", "ent_index", "from_player", "hash"]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    FROM_PLAYER_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    duration: float
    ent_index: int
    from_player: bool
    hash: int
    def __init__(
        self,
        hash: _Optional[int] = ...,
        duration: _Optional[float] = ...,
        from_player: bool = ...,
        ent_index: _Optional[int] = ...,
    ) -> None: ...

class CUserMessageCloseCaptionDirect(_message.Message):
    __slots__ = ["duration", "ent_index", "from_player", "hash"]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    FROM_PLAYER_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    duration: float
    ent_index: int
    from_player: bool
    hash: int
    def __init__(
        self,
        hash: _Optional[int] = ...,
        duration: _Optional[float] = ...,
        from_player: bool = ...,
        ent_index: _Optional[int] = ...,
    ) -> None: ...

class CUserMessageCloseCaptionPlaceholder(_message.Message):
    __slots__ = ["duration", "ent_index", "from_player", "string"]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    FROM_PLAYER_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    duration: float
    ent_index: int
    from_player: bool
    string: str
    def __init__(
        self,
        string: _Optional[str] = ...,
        duration: _Optional[float] = ...,
        from_player: bool = ...,
        ent_index: _Optional[int] = ...,
    ) -> None: ...

class CUserMessageColoredText(_message.Message):
    __slots__ = [
        "color",
        "context_player_slot",
        "context_team_id",
        "context_value",
        "reset",
        "text",
    ]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_VALUE_FIELD_NUMBER: _ClassVar[int]
    RESET_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    color: int
    context_player_slot: int
    context_team_id: int
    context_value: int
    reset: bool
    text: str
    def __init__(
        self,
        color: _Optional[int] = ...,
        text: _Optional[str] = ...,
        reset: bool = ...,
        context_player_slot: _Optional[int] = ...,
        context_value: _Optional[int] = ...,
        context_team_id: _Optional[int] = ...,
    ) -> None: ...

class CUserMessageCreditsMsg(_message.Message):
    __slots__ = ["logo_length", "rolltype"]
    LOGO_LENGTH_FIELD_NUMBER: _ClassVar[int]
    ROLLTYPE_FIELD_NUMBER: _ClassVar[int]
    logo_length: float
    rolltype: eRollType
    def __init__(
        self,
        rolltype: _Optional[_Union[eRollType, str]] = ...,
        logo_length: _Optional[float] = ...,
    ) -> None: ...

class CUserMessageCurrentTimescale(_message.Message):
    __slots__ = ["current"]
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    current: float
    def __init__(self, current: _Optional[float] = ...) -> None: ...

class CUserMessageDesiredTimescale(_message.Message):
    __slots__ = ["acceleration", "blenddeltamultiplier", "desired", "minblendrate"]
    ACCELERATION_FIELD_NUMBER: _ClassVar[int]
    BLENDDELTAMULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    DESIRED_FIELD_NUMBER: _ClassVar[int]
    MINBLENDRATE_FIELD_NUMBER: _ClassVar[int]
    acceleration: float
    blenddeltamultiplier: float
    desired: float
    minblendrate: float
    def __init__(
        self,
        desired: _Optional[float] = ...,
        acceleration: _Optional[float] = ...,
        minblendrate: _Optional[float] = ...,
        blenddeltamultiplier: _Optional[float] = ...,
    ) -> None: ...

class CUserMessageFade(_message.Message):
    __slots__ = ["color", "duration", "flags", "hold_time"]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    HOLD_TIME_FIELD_NUMBER: _ClassVar[int]
    color: int
    duration: int
    flags: int
    hold_time: int
    def __init__(
        self,
        duration: _Optional[int] = ...,
        hold_time: _Optional[int] = ...,
        flags: _Optional[int] = ...,
        color: _Optional[int] = ...,
    ) -> None: ...

class CUserMessageGameTitle(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CUserMessageHapticsManagerEffect(_message.Message):
    __slots__ = ["effect_name_hash_code", "effect_scale", "hand_id"]
    EFFECT_NAME_HASH_CODE_FIELD_NUMBER: _ClassVar[int]
    EFFECT_SCALE_FIELD_NUMBER: _ClassVar[int]
    HAND_ID_FIELD_NUMBER: _ClassVar[int]
    effect_name_hash_code: int
    effect_scale: float
    hand_id: int
    def __init__(
        self,
        hand_id: _Optional[int] = ...,
        effect_name_hash_code: _Optional[int] = ...,
        effect_scale: _Optional[float] = ...,
    ) -> None: ...

class CUserMessageHapticsManagerPulse(_message.Message):
    __slots__ = ["effect_amplitude", "effect_duration", "effect_frequency", "hand_id"]
    EFFECT_AMPLITUDE_FIELD_NUMBER: _ClassVar[int]
    EFFECT_DURATION_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    HAND_ID_FIELD_NUMBER: _ClassVar[int]
    effect_amplitude: float
    effect_duration: float
    effect_frequency: float
    hand_id: int
    def __init__(
        self,
        hand_id: _Optional[int] = ...,
        effect_amplitude: _Optional[float] = ...,
        effect_frequency: _Optional[float] = ...,
        effect_duration: _Optional[float] = ...,
    ) -> None: ...

class CUserMessageHudMsg(_message.Message):
    __slots__ = ["channel", "color1", "color2", "effect", "message", "x", "y"]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    COLOR1_FIELD_NUMBER: _ClassVar[int]
    COLOR2_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    channel: int
    color1: int
    color2: int
    effect: int
    message: str
    x: float
    y: float
    def __init__(
        self,
        channel: _Optional[int] = ...,
        x: _Optional[float] = ...,
        y: _Optional[float] = ...,
        color1: _Optional[int] = ...,
        color2: _Optional[int] = ...,
        effect: _Optional[int] = ...,
        message: _Optional[str] = ...,
    ) -> None: ...

class CUserMessageHudText(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class CUserMessageItemPickup(_message.Message):
    __slots__ = ["itemname"]
    ITEMNAME_FIELD_NUMBER: _ClassVar[int]
    itemname: str
    def __init__(self, itemname: _Optional[str] = ...) -> None: ...

class CUserMessageLagCompensationError(_message.Message):
    __slots__ = ["distance"]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    distance: float
    def __init__(self, distance: _Optional[float] = ...) -> None: ...

class CUserMessageRequestDiagnostic(_message.Message):
    __slots__ = ["diagnostics"]

    class Diagnostic(_message.Message):
        __slots__ = [
            "alias",
            "base",
            "context",
            "detail",
            "extent",
            "index",
            "length",
            "name",
            "offset",
            "param",
            "range",
            "type",
            "vardetail",
        ]
        ALIAS_FIELD_NUMBER: _ClassVar[int]
        BASE_FIELD_NUMBER: _ClassVar[int]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        DETAIL_FIELD_NUMBER: _ClassVar[int]
        EXTENT_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        PARAM_FIELD_NUMBER: _ClassVar[int]
        RANGE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VARDETAIL_FIELD_NUMBER: _ClassVar[int]
        alias: str
        base: int
        context: int
        detail: int
        extent: int
        index: int
        length: int
        name: str
        offset: int
        param: int
        range: int
        type: int
        vardetail: bytes
        def __init__(
            self,
            index: _Optional[int] = ...,
            offset: _Optional[int] = ...,
            param: _Optional[int] = ...,
            length: _Optional[int] = ...,
            type: _Optional[int] = ...,
            base: _Optional[int] = ...,
            range: _Optional[int] = ...,
            extent: _Optional[int] = ...,
            detail: _Optional[int] = ...,
            name: _Optional[str] = ...,
            alias: _Optional[str] = ...,
            vardetail: _Optional[bytes] = ...,
            context: _Optional[int] = ...,
        ) -> None: ...

    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    diagnostics: _containers.RepeatedCompositeFieldContainer[
        CUserMessageRequestDiagnostic.Diagnostic
    ]
    def __init__(
        self,
        diagnostics: _Optional[
            _Iterable[_Union[CUserMessageRequestDiagnostic.Diagnostic, _Mapping]]
        ] = ...,
    ) -> None: ...

class CUserMessageRequestDllStatus(_message.Message):
    __slots__ = ["dll_action", "full_report"]
    DLL_ACTION_FIELD_NUMBER: _ClassVar[int]
    FULL_REPORT_FIELD_NUMBER: _ClassVar[int]
    dll_action: str
    full_report: bool
    def __init__(
        self, dll_action: _Optional[str] = ..., full_report: bool = ...
    ) -> None: ...

class CUserMessageRequestInventory(_message.Message):
    __slots__ = ["inventory", "offset", "options"]
    INVENTORY_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    inventory: int
    offset: int
    options: int
    def __init__(
        self,
        inventory: _Optional[int] = ...,
        offset: _Optional[int] = ...,
        options: _Optional[int] = ...,
    ) -> None: ...

class CUserMessageRequestState(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CUserMessageRequestUtilAction(_message.Message):
    __slots__ = ["util1", "util2", "util3", "util4", "util5"]
    UTIL1_FIELD_NUMBER: _ClassVar[int]
    UTIL2_FIELD_NUMBER: _ClassVar[int]
    UTIL3_FIELD_NUMBER: _ClassVar[int]
    UTIL4_FIELD_NUMBER: _ClassVar[int]
    UTIL5_FIELD_NUMBER: _ClassVar[int]
    util1: int
    util2: int
    util3: int
    util4: int
    util5: int
    def __init__(
        self,
        util1: _Optional[int] = ...,
        util2: _Optional[int] = ...,
        util3: _Optional[int] = ...,
        util4: _Optional[int] = ...,
        util5: _Optional[int] = ...,
    ) -> None: ...

class CUserMessageResetHUD(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CUserMessageRumble(_message.Message):
    __slots__ = ["data", "flags", "index"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    data: int
    flags: int
    index: int
    def __init__(
        self,
        index: _Optional[int] = ...,
        data: _Optional[int] = ...,
        flags: _Optional[int] = ...,
    ) -> None: ...

class CUserMessageSayText(_message.Message):
    __slots__ = ["chat", "playerindex", "text"]
    CHAT_FIELD_NUMBER: _ClassVar[int]
    PLAYERINDEX_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    chat: bool
    playerindex: int
    text: str
    def __init__(
        self,
        playerindex: _Optional[int] = ...,
        text: _Optional[str] = ...,
        chat: bool = ...,
    ) -> None: ...

class CUserMessageSayText2(_message.Message):
    __slots__ = [
        "chat",
        "entityindex",
        "messagename",
        "param1",
        "param2",
        "param3",
        "param4",
    ]
    CHAT_FIELD_NUMBER: _ClassVar[int]
    ENTITYINDEX_FIELD_NUMBER: _ClassVar[int]
    MESSAGENAME_FIELD_NUMBER: _ClassVar[int]
    PARAM1_FIELD_NUMBER: _ClassVar[int]
    PARAM2_FIELD_NUMBER: _ClassVar[int]
    PARAM3_FIELD_NUMBER: _ClassVar[int]
    PARAM4_FIELD_NUMBER: _ClassVar[int]
    chat: bool
    entityindex: int
    messagename: str
    param1: str
    param2: str
    param3: str
    param4: str
    def __init__(
        self,
        entityindex: _Optional[int] = ...,
        chat: bool = ...,
        messagename: _Optional[str] = ...,
        param1: _Optional[str] = ...,
        param2: _Optional[str] = ...,
        param3: _Optional[str] = ...,
        param4: _Optional[str] = ...,
    ) -> None: ...

class CUserMessageSayTextChannel(_message.Message):
    __slots__ = ["channel", "player", "text"]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    channel: int
    player: int
    text: str
    def __init__(
        self,
        player: _Optional[int] = ...,
        channel: _Optional[int] = ...,
        text: _Optional[str] = ...,
    ) -> None: ...

class CUserMessageScreenTilt(_message.Message):
    __slots__ = ["angle", "command", "duration", "ease_in_out", "time"]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    EASE_IN_OUT_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    angle: _networkbasetypes_pb2.CMsgVector
    command: int
    duration: float
    ease_in_out: bool
    time: float
    def __init__(
        self,
        command: _Optional[int] = ...,
        ease_in_out: bool = ...,
        angle: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...,
        duration: _Optional[float] = ...,
        time: _Optional[float] = ...,
    ) -> None: ...

class CUserMessageSendAudio(_message.Message):
    __slots__ = ["soundname", "stop"]
    SOUNDNAME_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    soundname: str
    stop: bool
    def __init__(self, soundname: _Optional[str] = ..., stop: bool = ...) -> None: ...

class CUserMessageServerFrameTime(_message.Message):
    __slots__ = ["frame_time"]
    FRAME_TIME_FIELD_NUMBER: _ClassVar[int]
    frame_time: float
    def __init__(self, frame_time: _Optional[float] = ...) -> None: ...

class CUserMessageShake(_message.Message):
    __slots__ = ["amplitude", "command", "duration", "frequency"]
    AMPLITUDE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    amplitude: float
    command: int
    duration: float
    frequency: float
    def __init__(
        self,
        command: _Optional[int] = ...,
        amplitude: _Optional[float] = ...,
        frequency: _Optional[float] = ...,
        duration: _Optional[float] = ...,
    ) -> None: ...

class CUserMessageShakeDir(_message.Message):
    __slots__ = ["direction", "shake"]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    SHAKE_FIELD_NUMBER: _ClassVar[int]
    direction: _networkbasetypes_pb2.CMsgVector
    shake: CUserMessageShake
    def __init__(
        self,
        shake: _Optional[_Union[CUserMessageShake, _Mapping]] = ...,
        direction: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...,
    ) -> None: ...

class CUserMessageShowMenu(_message.Message):
    __slots__ = ["displaytime", "menustring", "needmore", "validslots"]
    DISPLAYTIME_FIELD_NUMBER: _ClassVar[int]
    MENUSTRING_FIELD_NUMBER: _ClassVar[int]
    NEEDMORE_FIELD_NUMBER: _ClassVar[int]
    VALIDSLOTS_FIELD_NUMBER: _ClassVar[int]
    displaytime: int
    menustring: str
    needmore: bool
    validslots: int
    def __init__(
        self,
        validslots: _Optional[int] = ...,
        displaytime: _Optional[int] = ...,
        needmore: bool = ...,
        menustring: _Optional[str] = ...,
    ) -> None: ...

class CUserMessageTextMsg(_message.Message):
    __slots__ = ["dest", "param"]
    DEST_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    dest: int
    param: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self, dest: _Optional[int] = ..., param: _Optional[_Iterable[str]] = ...
    ) -> None: ...

class CUserMessageUpdateCssClasses(_message.Message):
    __slots__ = ["css_classes", "is_add", "target_world_panel"]
    CSS_CLASSES_FIELD_NUMBER: _ClassVar[int]
    IS_ADD_FIELD_NUMBER: _ClassVar[int]
    TARGET_WORLD_PANEL_FIELD_NUMBER: _ClassVar[int]
    css_classes: str
    is_add: bool
    target_world_panel: int
    def __init__(
        self,
        target_world_panel: _Optional[int] = ...,
        css_classes: _Optional[str] = ...,
        is_add: bool = ...,
    ) -> None: ...

class CUserMessageVoiceMask(_message.Message):
    __slots__ = ["ban_masks", "gamerules_masks", "mod_enable"]
    BAN_MASKS_FIELD_NUMBER: _ClassVar[int]
    GAMERULES_MASKS_FIELD_NUMBER: _ClassVar[int]
    MOD_ENABLE_FIELD_NUMBER: _ClassVar[int]
    ban_masks: _containers.RepeatedScalarFieldContainer[int]
    gamerules_masks: _containers.RepeatedScalarFieldContainer[int]
    mod_enable: bool
    def __init__(
        self,
        gamerules_masks: _Optional[_Iterable[int]] = ...,
        ban_masks: _Optional[_Iterable[int]] = ...,
        mod_enable: bool = ...,
    ) -> None: ...

class CUserMessageWaterShake(_message.Message):
    __slots__ = ["amplitude", "command", "duration", "frequency"]
    AMPLITUDE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    amplitude: float
    command: int
    duration: float
    frequency: float
    def __init__(
        self,
        command: _Optional[int] = ...,
        amplitude: _Optional[float] = ...,
        frequency: _Optional[float] = ...,
        duration: _Optional[float] = ...,
    ) -> None: ...

class CUserMessage_Diagnostic_Response(_message.Message):
    __slots__ = [
        "build_version",
        "diagnostics",
        "instance",
        "osversion",
        "platform",
        "start_time",
    ]

    class Diagnostic(_message.Message):
        __slots__ = [
            "alias",
            "augment",
            "backup",
            "base",
            "context",
            "control",
            "detail",
            "index",
            "length",
            "name",
            "offset",
            "param",
            "placebo",
            "range",
            "type",
        ]
        ALIAS_FIELD_NUMBER: _ClassVar[int]
        AUGMENT_FIELD_NUMBER: _ClassVar[int]
        BACKUP_FIELD_NUMBER: _ClassVar[int]
        BASE_FIELD_NUMBER: _ClassVar[int]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        CONTROL_FIELD_NUMBER: _ClassVar[int]
        DETAIL_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        PARAM_FIELD_NUMBER: _ClassVar[int]
        PLACEBO_FIELD_NUMBER: _ClassVar[int]
        RANGE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        alias: str
        augment: int
        backup: bytes
        base: int
        context: int
        control: int
        detail: bytes
        index: int
        length: int
        name: str
        offset: int
        param: int
        placebo: int
        range: int
        type: int
        def __init__(
            self,
            index: _Optional[int] = ...,
            offset: _Optional[int] = ...,
            param: _Optional[int] = ...,
            length: _Optional[int] = ...,
            detail: _Optional[bytes] = ...,
            base: _Optional[int] = ...,
            range: _Optional[int] = ...,
            type: _Optional[int] = ...,
            name: _Optional[str] = ...,
            alias: _Optional[str] = ...,
            backup: _Optional[bytes] = ...,
            context: _Optional[int] = ...,
            control: _Optional[int] = ...,
            augment: _Optional[int] = ...,
            placebo: _Optional[int] = ...,
        ) -> None: ...

    BUILD_VERSION_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    OSVERSION_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    build_version: int
    diagnostics: _containers.RepeatedCompositeFieldContainer[
        CUserMessage_Diagnostic_Response.Diagnostic
    ]
    instance: int
    osversion: int
    platform: int
    start_time: int
    def __init__(
        self,
        diagnostics: _Optional[
            _Iterable[_Union[CUserMessage_Diagnostic_Response.Diagnostic, _Mapping]]
        ] = ...,
        build_version: _Optional[int] = ...,
        instance: _Optional[int] = ...,
        start_time: _Optional[int] = ...,
        osversion: _Optional[int] = ...,
        platform: _Optional[int] = ...,
    ) -> None: ...

class CUserMessage_DllStatus(_message.Message):
    __slots__ = [
        "client_time",
        "command_line",
        "diagnostics",
        "file_report",
        "modules",
        "osversion",
        "process_id",
        "total_files",
    ]

    class CModule(_message.Message):
        __slots__ = ["base_addr", "name", "size", "timestamp"]
        BASE_ADDR_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        base_addr: int
        name: str
        size: int
        timestamp: int
        def __init__(
            self,
            base_addr: _Optional[int] = ...,
            name: _Optional[str] = ...,
            size: _Optional[int] = ...,
            timestamp: _Optional[int] = ...,
        ) -> None: ...

    class CVDiagnostic(_message.Message):
        __slots__ = ["extended", "id", "string_value", "value"]
        EXTENDED_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        extended: int
        id: int
        string_value: str
        value: int
        def __init__(
            self,
            id: _Optional[int] = ...,
            extended: _Optional[int] = ...,
            value: _Optional[int] = ...,
            string_value: _Optional[str] = ...,
        ) -> None: ...

    CLIENT_TIME_FIELD_NUMBER: _ClassVar[int]
    COMMAND_LINE_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    FILE_REPORT_FIELD_NUMBER: _ClassVar[int]
    MODULES_FIELD_NUMBER: _ClassVar[int]
    OSVERSION_FIELD_NUMBER: _ClassVar[int]
    PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FILES_FIELD_NUMBER: _ClassVar[int]
    client_time: int
    command_line: str
    diagnostics: _containers.RepeatedCompositeFieldContainer[
        CUserMessage_DllStatus.CVDiagnostic
    ]
    file_report: str
    modules: _containers.RepeatedCompositeFieldContainer[CUserMessage_DllStatus.CModule]
    osversion: int
    process_id: int
    total_files: int
    def __init__(
        self,
        file_report: _Optional[str] = ...,
        command_line: _Optional[str] = ...,
        total_files: _Optional[int] = ...,
        process_id: _Optional[int] = ...,
        osversion: _Optional[int] = ...,
        client_time: _Optional[int] = ...,
        diagnostics: _Optional[
            _Iterable[_Union[CUserMessage_DllStatus.CVDiagnostic, _Mapping]]
        ] = ...,
        modules: _Optional[
            _Iterable[_Union[CUserMessage_DllStatus.CModule, _Mapping]]
        ] = ...,
    ) -> None: ...

class CUserMessage_ExtraUserData(_message.Message):
    __slots__ = ["detail1", "detail2", "item", "value1", "value2"]
    DETAIL1_FIELD_NUMBER: _ClassVar[int]
    DETAIL2_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    VALUE1_FIELD_NUMBER: _ClassVar[int]
    VALUE2_FIELD_NUMBER: _ClassVar[int]
    detail1: _containers.RepeatedScalarFieldContainer[bytes]
    detail2: _containers.RepeatedScalarFieldContainer[bytes]
    item: int
    value1: int
    value2: int
    def __init__(
        self,
        item: _Optional[int] = ...,
        value1: _Optional[int] = ...,
        value2: _Optional[int] = ...,
        detail1: _Optional[_Iterable[bytes]] = ...,
        detail2: _Optional[_Iterable[bytes]] = ...,
    ) -> None: ...

class CUserMessage_Inventory_Response(_message.Message):
    __slots__ = [
        "build_version",
        "client_timestamp",
        "crc",
        "instance",
        "inv_type",
        "inventories",
        "inventories2",
        "inventories3",
        "item_count",
        "osversion",
        "perf_time",
        "platform",
        "start_time",
    ]

    class InventoryDetail(_message.Message):
        __slots__ = [
            "base",
            "base_detail",
            "base_hash",
            "base_name",
            "base_time",
            "first",
            "index",
            "name",
            "offset",
            "primary",
        ]
        BASE_DETAIL_FIELD_NUMBER: _ClassVar[int]
        BASE_FIELD_NUMBER: _ClassVar[int]
        BASE_HASH_FIELD_NUMBER: _ClassVar[int]
        BASE_NAME_FIELD_NUMBER: _ClassVar[int]
        BASE_TIME_FIELD_NUMBER: _ClassVar[int]
        FIRST_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_FIELD_NUMBER: _ClassVar[int]
        base: int
        base_detail: int
        base_hash: int
        base_name: str
        base_time: int
        first: int
        index: int
        name: str
        offset: int
        primary: int
        def __init__(
            self,
            index: _Optional[int] = ...,
            primary: _Optional[int] = ...,
            offset: _Optional[int] = ...,
            first: _Optional[int] = ...,
            base: _Optional[int] = ...,
            name: _Optional[str] = ...,
            base_name: _Optional[str] = ...,
            base_detail: _Optional[int] = ...,
            base_time: _Optional[int] = ...,
            base_hash: _Optional[int] = ...,
        ) -> None: ...

    BUILD_VERSION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CRC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    INVENTORIES2_FIELD_NUMBER: _ClassVar[int]
    INVENTORIES3_FIELD_NUMBER: _ClassVar[int]
    INVENTORIES_FIELD_NUMBER: _ClassVar[int]
    INV_TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    OSVERSION_FIELD_NUMBER: _ClassVar[int]
    PERF_TIME_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    build_version: int
    client_timestamp: int
    crc: int
    instance: int
    inv_type: int
    inventories: _containers.RepeatedCompositeFieldContainer[
        CUserMessage_Inventory_Response.InventoryDetail
    ]
    inventories2: _containers.RepeatedCompositeFieldContainer[
        CUserMessage_Inventory_Response.InventoryDetail
    ]
    inventories3: _containers.RepeatedCompositeFieldContainer[
        CUserMessage_Inventory_Response.InventoryDetail
    ]
    item_count: int
    osversion: int
    perf_time: int
    platform: int
    start_time: int
    def __init__(
        self,
        crc: _Optional[int] = ...,
        item_count: _Optional[int] = ...,
        osversion: _Optional[int] = ...,
        perf_time: _Optional[int] = ...,
        client_timestamp: _Optional[int] = ...,
        platform: _Optional[int] = ...,
        inventories: _Optional[
            _Iterable[_Union[CUserMessage_Inventory_Response.InventoryDetail, _Mapping]]
        ] = ...,
        inventories2: _Optional[
            _Iterable[_Union[CUserMessage_Inventory_Response.InventoryDetail, _Mapping]]
        ] = ...,
        inventories3: _Optional[
            _Iterable[_Union[CUserMessage_Inventory_Response.InventoryDetail, _Mapping]]
        ] = ...,
        inv_type: _Optional[int] = ...,
        build_version: _Optional[int] = ...,
        instance: _Optional[int] = ...,
        start_time: _Optional[int] = ...,
    ) -> None: ...

class CUserMessage_NotifyResponseFound(_message.Message):
    __slots__ = [
        "criteria",
        "ent_index",
        "float_criteria_names",
        "float_criteria_values",
        "int_criteria_names",
        "int_criteria_values",
        "response_concept",
        "response_value",
        "rule_name",
        "speak_result",
        "symbol_criteria_names",
        "symbol_criteria_values",
    ]

    class Criteria(_message.Message):
        __slots__ = ["name_symbol", "value"]
        NAME_SYMBOL_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name_symbol: int
        value: str
        def __init__(
            self, name_symbol: _Optional[int] = ..., value: _Optional[str] = ...
        ) -> None: ...

    CRITERIA_FIELD_NUMBER: _ClassVar[int]
    ENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    FLOAT_CRITERIA_NAMES_FIELD_NUMBER: _ClassVar[int]
    FLOAT_CRITERIA_VALUES_FIELD_NUMBER: _ClassVar[int]
    INT_CRITERIA_NAMES_FIELD_NUMBER: _ClassVar[int]
    INT_CRITERIA_VALUES_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_CONCEPT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_VALUE_FIELD_NUMBER: _ClassVar[int]
    RULE_NAME_FIELD_NUMBER: _ClassVar[int]
    SPEAK_RESULT_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_CRITERIA_NAMES_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_CRITERIA_VALUES_FIELD_NUMBER: _ClassVar[int]
    criteria: _containers.RepeatedCompositeFieldContainer[
        CUserMessage_NotifyResponseFound.Criteria
    ]
    ent_index: int
    float_criteria_names: _containers.RepeatedScalarFieldContainer[int]
    float_criteria_values: _containers.RepeatedScalarFieldContainer[float]
    int_criteria_names: _containers.RepeatedScalarFieldContainer[int]
    int_criteria_values: _containers.RepeatedScalarFieldContainer[int]
    response_concept: str
    response_value: str
    rule_name: str
    speak_result: int
    symbol_criteria_names: _containers.RepeatedScalarFieldContainer[int]
    symbol_criteria_values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(
        self,
        ent_index: _Optional[int] = ...,
        rule_name: _Optional[str] = ...,
        response_value: _Optional[str] = ...,
        response_concept: _Optional[str] = ...,
        criteria: _Optional[
            _Iterable[_Union[CUserMessage_NotifyResponseFound.Criteria, _Mapping]]
        ] = ...,
        int_criteria_names: _Optional[_Iterable[int]] = ...,
        int_criteria_values: _Optional[_Iterable[int]] = ...,
        float_criteria_names: _Optional[_Iterable[int]] = ...,
        float_criteria_values: _Optional[_Iterable[float]] = ...,
        symbol_criteria_names: _Optional[_Iterable[int]] = ...,
        symbol_criteria_values: _Optional[_Iterable[int]] = ...,
        speak_result: _Optional[int] = ...,
    ) -> None: ...

class CUserMessage_PlayResponseConditional(_message.Message):
    __slots__ = [
        "ent_index",
        "ent_origin",
        "mix_priority",
        "player_slots",
        "pre_delay",
        "response",
    ]
    ENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    ENT_ORIGIN_FIELD_NUMBER: _ClassVar[int]
    MIX_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SLOTS_FIELD_NUMBER: _ClassVar[int]
    PRE_DELAY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ent_index: int
    ent_origin: _networkbasetypes_pb2.CMsgVector
    mix_priority: int
    player_slots: _containers.RepeatedScalarFieldContainer[int]
    pre_delay: float
    response: str
    def __init__(
        self,
        ent_index: _Optional[int] = ...,
        player_slots: _Optional[_Iterable[int]] = ...,
        response: _Optional[str] = ...,
        ent_origin: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...,
        pre_delay: _Optional[float] = ...,
        mix_priority: _Optional[int] = ...,
    ) -> None: ...

class CUserMessage_UtilMsg_Response(_message.Message):
    __slots__ = [
        "client_timestamp",
        "crc",
        "crc2",
        "crc_part",
        "crc_part2",
        "item_count",
        "item_count2",
        "itemdetails",
        "itemgroup",
        "platform",
        "total_count",
        "total_count2",
    ]

    class ItemDetail(_message.Message):
        __slots__ = ["crc", "hash", "index", "name"]
        CRC_FIELD_NUMBER: _ClassVar[int]
        HASH_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        crc: int
        hash: int
        index: int
        name: str
        def __init__(
            self,
            index: _Optional[int] = ...,
            hash: _Optional[int] = ...,
            crc: _Optional[int] = ...,
            name: _Optional[str] = ...,
        ) -> None: ...

    CLIENT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CRC2_FIELD_NUMBER: _ClassVar[int]
    CRC_FIELD_NUMBER: _ClassVar[int]
    CRC_PART2_FIELD_NUMBER: _ClassVar[int]
    CRC_PART_FIELD_NUMBER: _ClassVar[int]
    ITEMDETAILS_FIELD_NUMBER: _ClassVar[int]
    ITEMGROUP_FIELD_NUMBER: _ClassVar[int]
    ITEM_COUNT2_FIELD_NUMBER: _ClassVar[int]
    ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT2_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    client_timestamp: int
    crc: int
    crc2: int
    crc_part: _containers.RepeatedScalarFieldContainer[int]
    crc_part2: _containers.RepeatedScalarFieldContainer[int]
    item_count: int
    item_count2: int
    itemdetails: _containers.RepeatedCompositeFieldContainer[
        CUserMessage_UtilMsg_Response.ItemDetail
    ]
    itemgroup: int
    platform: int
    total_count: int
    total_count2: int
    def __init__(
        self,
        crc: _Optional[int] = ...,
        item_count: _Optional[int] = ...,
        crc2: _Optional[int] = ...,
        item_count2: _Optional[int] = ...,
        crc_part: _Optional[_Iterable[int]] = ...,
        crc_part2: _Optional[_Iterable[int]] = ...,
        client_timestamp: _Optional[int] = ...,
        platform: _Optional[int] = ...,
        itemdetails: _Optional[
            _Iterable[_Union[CUserMessage_UtilMsg_Response.ItemDetail, _Mapping]]
        ] = ...,
        itemgroup: _Optional[int] = ...,
        total_count: _Optional[int] = ...,
        total_count2: _Optional[int] = ...,
    ) -> None: ...

class CUserMsg_CustomGameEvent(_message.Message):
    __slots__ = ["data", "event_name"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    event_name: str
    def __init__(
        self, event_name: _Optional[str] = ..., data: _Optional[bytes] = ...
    ) -> None: ...

class CUserMsg_HudError(_message.Message):
    __slots__ = ["order_id"]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: int
    def __init__(self, order_id: _Optional[int] = ...) -> None: ...

class CUserMsg_ParticleManager(_message.Message):
    __slots__ = [
        "add_modellist_override_element",
        "change_control_point_attachment",
        "clear_modellist_override",
        "create_particle",
        "create_physics_sim",
        "destroy_particle",
        "destroy_particle_involving",
        "destroy_particle_named",
        "destroy_physics_sim",
        "freeze_particle_involving",
        "index",
        "particle_can_freeze",
        "particle_freeze_transition_override",
        "particle_skip_to_time",
        "release_particle_index",
        "set_control_point_model",
        "set_control_point_snapshot",
        "set_material_override",
        "set_named_value_context",
        "set_particle_fow_properties",
        "set_particle_should_check_fow",
        "set_particle_text",
        "set_scene_object_generic_flag",
        "set_scene_object_tint_and_desat",
        "set_texture_attribute",
        "set_vdata",
        "type",
        "update_entity_position",
        "update_particle",
        "update_particle_ent",
        "update_particle_fallback",
        "update_particle_fwd",
        "update_particle_offset",
        "update_particle_orient",
        "update_particle_set_frozen",
        "update_particle_should_draw",
        "update_particle_transform",
    ]

    class AddModellistOverrideElement(_message.Message):
        __slots__ = ["groupid", "model_name", "spawn_probability"]
        GROUPID_FIELD_NUMBER: _ClassVar[int]
        MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
        SPAWN_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
        groupid: int
        model_name: str
        spawn_probability: float
        def __init__(
            self,
            model_name: _Optional[str] = ...,
            spawn_probability: _Optional[float] = ...,
            groupid: _Optional[int] = ...,
        ) -> None: ...

    class ChangeControlPointAttachment(_message.Message):
        __slots__ = ["attachment_new", "attachment_old", "entity_handle"]
        ATTACHMENT_NEW_FIELD_NUMBER: _ClassVar[int]
        ATTACHMENT_OLD_FIELD_NUMBER: _ClassVar[int]
        ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
        attachment_new: int
        attachment_old: int
        entity_handle: int
        def __init__(
            self,
            attachment_old: _Optional[int] = ...,
            attachment_new: _Optional[int] = ...,
            entity_handle: _Optional[int] = ...,
        ) -> None: ...

    class ClearModellistOverride(_message.Message):
        __slots__ = ["groupid"]
        GROUPID_FIELD_NUMBER: _ClassVar[int]
        groupid: int
        def __init__(self, groupid: _Optional[int] = ...) -> None: ...

    class CreateParticle(_message.Message):
        __slots__ = [
            "aggregation_position",
            "apply_voice_ban_rules",
            "attach_type",
            "cluster",
            "control_point_configuration",
            "endcap_time",
            "entity_handle",
            "entity_handle_for_modifiers",
            "particle_name_index",
            "team_behavior",
        ]
        AGGREGATION_POSITION_FIELD_NUMBER: _ClassVar[int]
        APPLY_VOICE_BAN_RULES_FIELD_NUMBER: _ClassVar[int]
        ATTACH_TYPE_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_FIELD_NUMBER: _ClassVar[int]
        CONTROL_POINT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
        ENDCAP_TIME_FIELD_NUMBER: _ClassVar[int]
        ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
        ENTITY_HANDLE_FOR_MODIFIERS_FIELD_NUMBER: _ClassVar[int]
        PARTICLE_NAME_INDEX_FIELD_NUMBER: _ClassVar[int]
        TEAM_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        aggregation_position: _networkbasetypes_pb2.CMsgVector
        apply_voice_ban_rules: bool
        attach_type: int
        cluster: bool
        control_point_configuration: str
        endcap_time: float
        entity_handle: int
        entity_handle_for_modifiers: int
        particle_name_index: int
        team_behavior: int
        def __init__(
            self,
            particle_name_index: _Optional[int] = ...,
            attach_type: _Optional[int] = ...,
            entity_handle: _Optional[int] = ...,
            entity_handle_for_modifiers: _Optional[int] = ...,
            apply_voice_ban_rules: bool = ...,
            team_behavior: _Optional[int] = ...,
            control_point_configuration: _Optional[str] = ...,
            cluster: bool = ...,
            endcap_time: _Optional[float] = ...,
            aggregation_position: _Optional[
                _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
            ] = ...,
        ) -> None: ...

    class CreatePhysicsSim(_message.Message):
        __slots__ = [
            "max_particle_count",
            "prop_group_name",
            "use_high_quality_simulation",
        ]
        MAX_PARTICLE_COUNT_FIELD_NUMBER: _ClassVar[int]
        PROP_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        USE_HIGH_QUALITY_SIMULATION_FIELD_NUMBER: _ClassVar[int]
        max_particle_count: int
        prop_group_name: str
        use_high_quality_simulation: bool
        def __init__(
            self,
            prop_group_name: _Optional[str] = ...,
            use_high_quality_simulation: bool = ...,
            max_particle_count: _Optional[int] = ...,
        ) -> None: ...

    class DestroyParticle(_message.Message):
        __slots__ = ["destroy_immediately"]
        DESTROY_IMMEDIATELY_FIELD_NUMBER: _ClassVar[int]
        destroy_immediately: bool
        def __init__(self, destroy_immediately: bool = ...) -> None: ...

    class DestroyParticleInvolving(_message.Message):
        __slots__ = ["destroy_immediately", "entity_handle"]
        DESTROY_IMMEDIATELY_FIELD_NUMBER: _ClassVar[int]
        ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
        destroy_immediately: bool
        entity_handle: int
        def __init__(
            self, destroy_immediately: bool = ..., entity_handle: _Optional[int] = ...
        ) -> None: ...

    class DestroyParticleNamed(_message.Message):
        __slots__ = [
            "destroy_immediately",
            "entity_handle",
            "particle_name_index",
            "play_endcap",
        ]
        DESTROY_IMMEDIATELY_FIELD_NUMBER: _ClassVar[int]
        ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
        PARTICLE_NAME_INDEX_FIELD_NUMBER: _ClassVar[int]
        PLAY_ENDCAP_FIELD_NUMBER: _ClassVar[int]
        destroy_immediately: bool
        entity_handle: int
        particle_name_index: int
        play_endcap: bool
        def __init__(
            self,
            particle_name_index: _Optional[int] = ...,
            entity_handle: _Optional[int] = ...,
            destroy_immediately: bool = ...,
            play_endcap: bool = ...,
        ) -> None: ...

    class DestroyPhysicsSim(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...

    class FreezeParticleInvolving(_message.Message):
        __slots__ = ["entity_handle", "set_frozen", "transition_duration"]
        ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
        SET_FROZEN_FIELD_NUMBER: _ClassVar[int]
        TRANSITION_DURATION_FIELD_NUMBER: _ClassVar[int]
        entity_handle: int
        set_frozen: bool
        transition_duration: float
        def __init__(
            self,
            set_frozen: bool = ...,
            transition_duration: _Optional[float] = ...,
            entity_handle: _Optional[int] = ...,
        ) -> None: ...

    class ParticleCanFreeze(_message.Message):
        __slots__ = ["can_freeze"]
        CAN_FREEZE_FIELD_NUMBER: _ClassVar[int]
        can_freeze: bool
        def __init__(self, can_freeze: bool = ...) -> None: ...

    class ParticleFreezeTransitionOverride(_message.Message):
        __slots__ = ["freeze_transition_override"]
        FREEZE_TRANSITION_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
        freeze_transition_override: float
        def __init__(
            self, freeze_transition_override: _Optional[float] = ...
        ) -> None: ...

    class ParticleSkipToTime(_message.Message):
        __slots__ = ["skip_to_time"]
        SKIP_TO_TIME_FIELD_NUMBER: _ClassVar[int]
        skip_to_time: float
        def __init__(self, skip_to_time: _Optional[float] = ...) -> None: ...

    class ReleaseParticleIndex(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...

    class SetControlPointModel(_message.Message):
        __slots__ = ["control_point", "model_name"]
        CONTROL_POINT_FIELD_NUMBER: _ClassVar[int]
        MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
        control_point: int
        model_name: str
        def __init__(
            self, control_point: _Optional[int] = ..., model_name: _Optional[str] = ...
        ) -> None: ...

    class SetControlPointSnapshot(_message.Message):
        __slots__ = ["control_point", "snapshot_name"]
        CONTROL_POINT_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
        control_point: int
        snapshot_name: str
        def __init__(
            self,
            control_point: _Optional[int] = ...,
            snapshot_name: _Optional[str] = ...,
        ) -> None: ...

    class SetMaterialOverride(_message.Message):
        __slots__ = ["include_children", "material_name"]
        INCLUDE_CHILDREN_FIELD_NUMBER: _ClassVar[int]
        MATERIAL_NAME_FIELD_NUMBER: _ClassVar[int]
        include_children: bool
        material_name: str
        def __init__(
            self, material_name: _Optional[str] = ..., include_children: bool = ...
        ) -> None: ...

    class SetParticleFoWProperties(_message.Message):
        __slots__ = ["fow_control_point", "fow_control_point2", "fow_radius"]
        FOW_CONTROL_POINT2_FIELD_NUMBER: _ClassVar[int]
        FOW_CONTROL_POINT_FIELD_NUMBER: _ClassVar[int]
        FOW_RADIUS_FIELD_NUMBER: _ClassVar[int]
        fow_control_point: int
        fow_control_point2: int
        fow_radius: float
        def __init__(
            self,
            fow_control_point: _Optional[int] = ...,
            fow_control_point2: _Optional[int] = ...,
            fow_radius: _Optional[float] = ...,
        ) -> None: ...

    class SetParticleNamedValueContext(_message.Message):
        __slots__ = [
            "ehandle_values",
            "float_values",
            "transform_values",
            "vector_values",
        ]

        class EHandleContext(_message.Message):
            __slots__ = ["ent_index", "value_name_hash"]
            ENT_INDEX_FIELD_NUMBER: _ClassVar[int]
            VALUE_NAME_HASH_FIELD_NUMBER: _ClassVar[int]
            ent_index: int
            value_name_hash: int
            def __init__(
                self,
                value_name_hash: _Optional[int] = ...,
                ent_index: _Optional[int] = ...,
            ) -> None: ...

        class FloatContextValue(_message.Message):
            __slots__ = ["value", "value_name_hash"]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            VALUE_NAME_HASH_FIELD_NUMBER: _ClassVar[int]
            value: float
            value_name_hash: int
            def __init__(
                self,
                value_name_hash: _Optional[int] = ...,
                value: _Optional[float] = ...,
            ) -> None: ...

        class TransformContextValue(_message.Message):
            __slots__ = ["angles", "translation", "value_name_hash"]
            ANGLES_FIELD_NUMBER: _ClassVar[int]
            TRANSLATION_FIELD_NUMBER: _ClassVar[int]
            VALUE_NAME_HASH_FIELD_NUMBER: _ClassVar[int]
            angles: _networkbasetypes_pb2.CMsgQAngle
            translation: _networkbasetypes_pb2.CMsgVector
            value_name_hash: int
            def __init__(
                self,
                value_name_hash: _Optional[int] = ...,
                angles: _Optional[
                    _Union[_networkbasetypes_pb2.CMsgQAngle, _Mapping]
                ] = ...,
                translation: _Optional[
                    _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
                ] = ...,
            ) -> None: ...

        class VectorContextValue(_message.Message):
            __slots__ = ["value", "value_name_hash"]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            VALUE_NAME_HASH_FIELD_NUMBER: _ClassVar[int]
            value: _networkbasetypes_pb2.CMsgVector
            value_name_hash: int
            def __init__(
                self,
                value_name_hash: _Optional[int] = ...,
                value: _Optional[
                    _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
                ] = ...,
            ) -> None: ...

        EHANDLE_VALUES_FIELD_NUMBER: _ClassVar[int]
        FLOAT_VALUES_FIELD_NUMBER: _ClassVar[int]
        TRANSFORM_VALUES_FIELD_NUMBER: _ClassVar[int]
        VECTOR_VALUES_FIELD_NUMBER: _ClassVar[int]
        ehandle_values: _containers.RepeatedCompositeFieldContainer[
            CUserMsg_ParticleManager.SetParticleNamedValueContext.EHandleContext
        ]
        float_values: _containers.RepeatedCompositeFieldContainer[
            CUserMsg_ParticleManager.SetParticleNamedValueContext.FloatContextValue
        ]
        transform_values: _containers.RepeatedCompositeFieldContainer[
            CUserMsg_ParticleManager.SetParticleNamedValueContext.TransformContextValue
        ]
        vector_values: _containers.RepeatedCompositeFieldContainer[
            CUserMsg_ParticleManager.SetParticleNamedValueContext.VectorContextValue
        ]
        def __init__(
            self,
            float_values: _Optional[
                _Iterable[
                    _Union[
                        CUserMsg_ParticleManager.SetParticleNamedValueContext.FloatContextValue,
                        _Mapping,
                    ]
                ]
            ] = ...,
            vector_values: _Optional[
                _Iterable[
                    _Union[
                        CUserMsg_ParticleManager.SetParticleNamedValueContext.VectorContextValue,
                        _Mapping,
                    ]
                ]
            ] = ...,
            transform_values: _Optional[
                _Iterable[
                    _Union[
                        CUserMsg_ParticleManager.SetParticleNamedValueContext.TransformContextValue,
                        _Mapping,
                    ]
                ]
            ] = ...,
            ehandle_values: _Optional[
                _Iterable[
                    _Union[
                        CUserMsg_ParticleManager.SetParticleNamedValueContext.EHandleContext,
                        _Mapping,
                    ]
                ]
            ] = ...,
        ) -> None: ...

    class SetParticleShouldCheckFoW(_message.Message):
        __slots__ = ["check_fow"]
        CHECK_FOW_FIELD_NUMBER: _ClassVar[int]
        check_fow: bool
        def __init__(self, check_fow: bool = ...) -> None: ...

    class SetParticleText(_message.Message):
        __slots__ = ["text"]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        text: str
        def __init__(self, text: _Optional[str] = ...) -> None: ...

    class SetSceneObjectGenericFlag(_message.Message):
        __slots__ = ["flag_value"]
        FLAG_VALUE_FIELD_NUMBER: _ClassVar[int]
        flag_value: bool
        def __init__(self, flag_value: bool = ...) -> None: ...

    class SetSceneObjectTintAndDesat(_message.Message):
        __slots__ = ["desat", "tint"]
        DESAT_FIELD_NUMBER: _ClassVar[int]
        TINT_FIELD_NUMBER: _ClassVar[int]
        desat: float
        tint: int
        def __init__(
            self, tint: _Optional[int] = ..., desat: _Optional[float] = ...
        ) -> None: ...

    class SetTextureAttribute(_message.Message):
        __slots__ = ["attribute_name", "texture_name"]
        ATTRIBUTE_NAME_FIELD_NUMBER: _ClassVar[int]
        TEXTURE_NAME_FIELD_NUMBER: _ClassVar[int]
        attribute_name: str
        texture_name: str
        def __init__(
            self,
            attribute_name: _Optional[str] = ...,
            texture_name: _Optional[str] = ...,
        ) -> None: ...

    class SetVData(_message.Message):
        __slots__ = ["vdata_name"]
        VDATA_NAME_FIELD_NUMBER: _ClassVar[int]
        vdata_name: str
        def __init__(self, vdata_name: _Optional[str] = ...) -> None: ...

    class UpdateEntityPosition(_message.Message):
        __slots__ = ["entity_handle", "position"]
        ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
        POSITION_FIELD_NUMBER: _ClassVar[int]
        entity_handle: int
        position: _networkbasetypes_pb2.CMsgVector
        def __init__(
            self,
            entity_handle: _Optional[int] = ...,
            position: _Optional[
                _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
            ] = ...,
        ) -> None: ...

    class UpdateParticleEnt(_message.Message):
        __slots__ = [
            "attach_type",
            "attachment",
            "control_point",
            "entity_handle",
            "fallback_position",
            "include_wearables",
            "offset_angles",
            "offset_position",
        ]
        ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
        ATTACH_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONTROL_POINT_FIELD_NUMBER: _ClassVar[int]
        ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
        FALLBACK_POSITION_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_WEARABLES_FIELD_NUMBER: _ClassVar[int]
        OFFSET_ANGLES_FIELD_NUMBER: _ClassVar[int]
        OFFSET_POSITION_FIELD_NUMBER: _ClassVar[int]
        attach_type: int
        attachment: int
        control_point: int
        entity_handle: int
        fallback_position: _networkbasetypes_pb2.CMsgVector
        include_wearables: bool
        offset_angles: _networkbasetypes_pb2.CMsgQAngle
        offset_position: _networkbasetypes_pb2.CMsgVector
        def __init__(
            self,
            control_point: _Optional[int] = ...,
            entity_handle: _Optional[int] = ...,
            attach_type: _Optional[int] = ...,
            attachment: _Optional[int] = ...,
            fallback_position: _Optional[
                _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
            ] = ...,
            include_wearables: bool = ...,
            offset_position: _Optional[
                _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
            ] = ...,
            offset_angles: _Optional[
                _Union[_networkbasetypes_pb2.CMsgQAngle, _Mapping]
            ] = ...,
        ) -> None: ...

    class UpdateParticleFallback(_message.Message):
        __slots__ = ["control_point", "position"]
        CONTROL_POINT_FIELD_NUMBER: _ClassVar[int]
        POSITION_FIELD_NUMBER: _ClassVar[int]
        control_point: int
        position: _networkbasetypes_pb2.CMsgVector
        def __init__(
            self,
            control_point: _Optional[int] = ...,
            position: _Optional[
                _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
            ] = ...,
        ) -> None: ...

    class UpdateParticleFwd_OBSOLETE(_message.Message):
        __slots__ = ["control_point", "forward"]
        CONTROL_POINT_FIELD_NUMBER: _ClassVar[int]
        FORWARD_FIELD_NUMBER: _ClassVar[int]
        control_point: int
        forward: _networkbasetypes_pb2.CMsgVector
        def __init__(
            self,
            control_point: _Optional[int] = ...,
            forward: _Optional[
                _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
            ] = ...,
        ) -> None: ...

    class UpdateParticleOffset(_message.Message):
        __slots__ = ["angle_offset", "control_point", "origin_offset"]
        ANGLE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        CONTROL_POINT_FIELD_NUMBER: _ClassVar[int]
        ORIGIN_OFFSET_FIELD_NUMBER: _ClassVar[int]
        angle_offset: _networkbasetypes_pb2.CMsgQAngle
        control_point: int
        origin_offset: _networkbasetypes_pb2.CMsgVector
        def __init__(
            self,
            control_point: _Optional[int] = ...,
            origin_offset: _Optional[
                _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
            ] = ...,
            angle_offset: _Optional[
                _Union[_networkbasetypes_pb2.CMsgQAngle, _Mapping]
            ] = ...,
        ) -> None: ...

    class UpdateParticleOrient_OBSOLETE(_message.Message):
        __slots__ = ["control_point", "deprecated_right", "forward", "left", "up"]
        CONTROL_POINT_FIELD_NUMBER: _ClassVar[int]
        DEPRECATED_RIGHT_FIELD_NUMBER: _ClassVar[int]
        FORWARD_FIELD_NUMBER: _ClassVar[int]
        LEFT_FIELD_NUMBER: _ClassVar[int]
        UP_FIELD_NUMBER: _ClassVar[int]
        control_point: int
        deprecated_right: _networkbasetypes_pb2.CMsgVector
        forward: _networkbasetypes_pb2.CMsgVector
        left: _networkbasetypes_pb2.CMsgVector
        up: _networkbasetypes_pb2.CMsgVector
        def __init__(
            self,
            control_point: _Optional[int] = ...,
            forward: _Optional[
                _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
            ] = ...,
            deprecated_right: _Optional[
                _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
            ] = ...,
            up: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...,
            left: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...,
        ) -> None: ...

    class UpdateParticleSetFrozen(_message.Message):
        __slots__ = ["set_frozen", "transition_duration"]
        SET_FROZEN_FIELD_NUMBER: _ClassVar[int]
        TRANSITION_DURATION_FIELD_NUMBER: _ClassVar[int]
        set_frozen: bool
        transition_duration: float
        def __init__(
            self, set_frozen: bool = ..., transition_duration: _Optional[float] = ...
        ) -> None: ...

    class UpdateParticleShouldDraw(_message.Message):
        __slots__ = ["should_draw"]
        SHOULD_DRAW_FIELD_NUMBER: _ClassVar[int]
        should_draw: bool
        def __init__(self, should_draw: bool = ...) -> None: ...

    class UpdateParticleTransform(_message.Message):
        __slots__ = [
            "control_point",
            "interpolation_interval",
            "orientation",
            "position",
        ]
        CONTROL_POINT_FIELD_NUMBER: _ClassVar[int]
        INTERPOLATION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        ORIENTATION_FIELD_NUMBER: _ClassVar[int]
        POSITION_FIELD_NUMBER: _ClassVar[int]
        control_point: int
        interpolation_interval: float
        orientation: _networkbasetypes_pb2.CMsgQuaternion
        position: _networkbasetypes_pb2.CMsgVector
        def __init__(
            self,
            control_point: _Optional[int] = ...,
            position: _Optional[
                _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
            ] = ...,
            orientation: _Optional[
                _Union[_networkbasetypes_pb2.CMsgQuaternion, _Mapping]
            ] = ...,
            interpolation_interval: _Optional[float] = ...,
        ) -> None: ...

    class UpdateParticle_OBSOLETE(_message.Message):
        __slots__ = ["control_point", "position"]
        CONTROL_POINT_FIELD_NUMBER: _ClassVar[int]
        POSITION_FIELD_NUMBER: _ClassVar[int]
        control_point: int
        position: _networkbasetypes_pb2.CMsgVector
        def __init__(
            self,
            control_point: _Optional[int] = ...,
            position: _Optional[
                _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
            ] = ...,
        ) -> None: ...

    ADD_MODELLIST_OVERRIDE_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    CHANGE_CONTROL_POINT_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    CLEAR_MODELLIST_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    CREATE_PARTICLE_FIELD_NUMBER: _ClassVar[int]
    CREATE_PHYSICS_SIM_FIELD_NUMBER: _ClassVar[int]
    DESTROY_PARTICLE_FIELD_NUMBER: _ClassVar[int]
    DESTROY_PARTICLE_INVOLVING_FIELD_NUMBER: _ClassVar[int]
    DESTROY_PARTICLE_NAMED_FIELD_NUMBER: _ClassVar[int]
    DESTROY_PHYSICS_SIM_FIELD_NUMBER: _ClassVar[int]
    Extensions: _python_message._ExtensionDict
    FREEZE_PARTICLE_INVOLVING_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    PARTICLE_CAN_FREEZE_FIELD_NUMBER: _ClassVar[int]
    PARTICLE_FREEZE_TRANSITION_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    PARTICLE_SKIP_TO_TIME_FIELD_NUMBER: _ClassVar[int]
    RELEASE_PARTICLE_INDEX_FIELD_NUMBER: _ClassVar[int]
    SET_CONTROL_POINT_MODEL_FIELD_NUMBER: _ClassVar[int]
    SET_CONTROL_POINT_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    SET_MATERIAL_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    SET_NAMED_VALUE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SET_PARTICLE_FOW_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    SET_PARTICLE_SHOULD_CHECK_FOW_FIELD_NUMBER: _ClassVar[int]
    SET_PARTICLE_TEXT_FIELD_NUMBER: _ClassVar[int]
    SET_SCENE_OBJECT_GENERIC_FLAG_FIELD_NUMBER: _ClassVar[int]
    SET_SCENE_OBJECT_TINT_AND_DESAT_FIELD_NUMBER: _ClassVar[int]
    SET_TEXTURE_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    SET_VDATA_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ENTITY_POSITION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PARTICLE_ENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PARTICLE_FALLBACK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PARTICLE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PARTICLE_FWD_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PARTICLE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PARTICLE_ORIENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PARTICLE_SET_FROZEN_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PARTICLE_SHOULD_DRAW_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PARTICLE_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    add_modellist_override_element: CUserMsg_ParticleManager.AddModellistOverrideElement
    change_control_point_attachment: (
        CUserMsg_ParticleManager.ChangeControlPointAttachment
    )
    clear_modellist_override: CUserMsg_ParticleManager.ClearModellistOverride
    create_particle: CUserMsg_ParticleManager.CreateParticle
    create_physics_sim: CUserMsg_ParticleManager.CreatePhysicsSim
    destroy_particle: CUserMsg_ParticleManager.DestroyParticle
    destroy_particle_involving: CUserMsg_ParticleManager.DestroyParticleInvolving
    destroy_particle_named: CUserMsg_ParticleManager.DestroyParticleNamed
    destroy_physics_sim: CUserMsg_ParticleManager.DestroyPhysicsSim
    freeze_particle_involving: CUserMsg_ParticleManager.FreezeParticleInvolving
    index: int
    particle_can_freeze: CUserMsg_ParticleManager.ParticleCanFreeze
    particle_freeze_transition_override: (
        CUserMsg_ParticleManager.ParticleFreezeTransitionOverride
    )
    particle_skip_to_time: CUserMsg_ParticleManager.ParticleSkipToTime
    release_particle_index: CUserMsg_ParticleManager.ReleaseParticleIndex
    set_control_point_model: CUserMsg_ParticleManager.SetControlPointModel
    set_control_point_snapshot: CUserMsg_ParticleManager.SetControlPointSnapshot
    set_material_override: CUserMsg_ParticleManager.SetMaterialOverride
    set_named_value_context: CUserMsg_ParticleManager.SetParticleNamedValueContext
    set_particle_fow_properties: CUserMsg_ParticleManager.SetParticleFoWProperties
    set_particle_should_check_fow: CUserMsg_ParticleManager.SetParticleShouldCheckFoW
    set_particle_text: CUserMsg_ParticleManager.SetParticleText
    set_scene_object_generic_flag: CUserMsg_ParticleManager.SetSceneObjectGenericFlag
    set_scene_object_tint_and_desat: CUserMsg_ParticleManager.SetSceneObjectTintAndDesat
    set_texture_attribute: CUserMsg_ParticleManager.SetTextureAttribute
    set_vdata: CUserMsg_ParticleManager.SetVData
    type: PARTICLE_MESSAGE
    update_entity_position: CUserMsg_ParticleManager.UpdateEntityPosition
    update_particle: CUserMsg_ParticleManager.UpdateParticle_OBSOLETE
    update_particle_ent: CUserMsg_ParticleManager.UpdateParticleEnt
    update_particle_fallback: CUserMsg_ParticleManager.UpdateParticleFallback
    update_particle_fwd: CUserMsg_ParticleManager.UpdateParticleFwd_OBSOLETE
    update_particle_offset: CUserMsg_ParticleManager.UpdateParticleOffset
    update_particle_orient: CUserMsg_ParticleManager.UpdateParticleOrient_OBSOLETE
    update_particle_set_frozen: CUserMsg_ParticleManager.UpdateParticleSetFrozen
    update_particle_should_draw: CUserMsg_ParticleManager.UpdateParticleShouldDraw
    update_particle_transform: CUserMsg_ParticleManager.UpdateParticleTransform
    def __init__(
        self,
        type: _Optional[_Union[PARTICLE_MESSAGE, str]] = ...,
        index: _Optional[int] = ...,
        release_particle_index: _Optional[
            _Union[CUserMsg_ParticleManager.ReleaseParticleIndex, _Mapping]
        ] = ...,
        create_particle: _Optional[
            _Union[CUserMsg_ParticleManager.CreateParticle, _Mapping]
        ] = ...,
        destroy_particle: _Optional[
            _Union[CUserMsg_ParticleManager.DestroyParticle, _Mapping]
        ] = ...,
        destroy_particle_involving: _Optional[
            _Union[CUserMsg_ParticleManager.DestroyParticleInvolving, _Mapping]
        ] = ...,
        update_particle: _Optional[
            _Union[CUserMsg_ParticleManager.UpdateParticle_OBSOLETE, _Mapping]
        ] = ...,
        update_particle_fwd: _Optional[
            _Union[CUserMsg_ParticleManager.UpdateParticleFwd_OBSOLETE, _Mapping]
        ] = ...,
        update_particle_orient: _Optional[
            _Union[CUserMsg_ParticleManager.UpdateParticleOrient_OBSOLETE, _Mapping]
        ] = ...,
        update_particle_fallback: _Optional[
            _Union[CUserMsg_ParticleManager.UpdateParticleFallback, _Mapping]
        ] = ...,
        update_particle_offset: _Optional[
            _Union[CUserMsg_ParticleManager.UpdateParticleOffset, _Mapping]
        ] = ...,
        update_particle_ent: _Optional[
            _Union[CUserMsg_ParticleManager.UpdateParticleEnt, _Mapping]
        ] = ...,
        update_particle_should_draw: _Optional[
            _Union[CUserMsg_ParticleManager.UpdateParticleShouldDraw, _Mapping]
        ] = ...,
        update_particle_set_frozen: _Optional[
            _Union[CUserMsg_ParticleManager.UpdateParticleSetFrozen, _Mapping]
        ] = ...,
        change_control_point_attachment: _Optional[
            _Union[CUserMsg_ParticleManager.ChangeControlPointAttachment, _Mapping]
        ] = ...,
        update_entity_position: _Optional[
            _Union[CUserMsg_ParticleManager.UpdateEntityPosition, _Mapping]
        ] = ...,
        set_particle_fow_properties: _Optional[
            _Union[CUserMsg_ParticleManager.SetParticleFoWProperties, _Mapping]
        ] = ...,
        set_particle_text: _Optional[
            _Union[CUserMsg_ParticleManager.SetParticleText, _Mapping]
        ] = ...,
        set_particle_should_check_fow: _Optional[
            _Union[CUserMsg_ParticleManager.SetParticleShouldCheckFoW, _Mapping]
        ] = ...,
        set_control_point_model: _Optional[
            _Union[CUserMsg_ParticleManager.SetControlPointModel, _Mapping]
        ] = ...,
        set_control_point_snapshot: _Optional[
            _Union[CUserMsg_ParticleManager.SetControlPointSnapshot, _Mapping]
        ] = ...,
        set_texture_attribute: _Optional[
            _Union[CUserMsg_ParticleManager.SetTextureAttribute, _Mapping]
        ] = ...,
        set_scene_object_generic_flag: _Optional[
            _Union[CUserMsg_ParticleManager.SetSceneObjectGenericFlag, _Mapping]
        ] = ...,
        set_scene_object_tint_and_desat: _Optional[
            _Union[CUserMsg_ParticleManager.SetSceneObjectTintAndDesat, _Mapping]
        ] = ...,
        destroy_particle_named: _Optional[
            _Union[CUserMsg_ParticleManager.DestroyParticleNamed, _Mapping]
        ] = ...,
        particle_skip_to_time: _Optional[
            _Union[CUserMsg_ParticleManager.ParticleSkipToTime, _Mapping]
        ] = ...,
        particle_can_freeze: _Optional[
            _Union[CUserMsg_ParticleManager.ParticleCanFreeze, _Mapping]
        ] = ...,
        set_named_value_context: _Optional[
            _Union[CUserMsg_ParticleManager.SetParticleNamedValueContext, _Mapping]
        ] = ...,
        update_particle_transform: _Optional[
            _Union[CUserMsg_ParticleManager.UpdateParticleTransform, _Mapping]
        ] = ...,
        particle_freeze_transition_override: _Optional[
            _Union[CUserMsg_ParticleManager.ParticleFreezeTransitionOverride, _Mapping]
        ] = ...,
        freeze_particle_involving: _Optional[
            _Union[CUserMsg_ParticleManager.FreezeParticleInvolving, _Mapping]
        ] = ...,
        add_modellist_override_element: _Optional[
            _Union[CUserMsg_ParticleManager.AddModellistOverrideElement, _Mapping]
        ] = ...,
        clear_modellist_override: _Optional[
            _Union[CUserMsg_ParticleManager.ClearModellistOverride, _Mapping]
        ] = ...,
        create_physics_sim: _Optional[
            _Union[CUserMsg_ParticleManager.CreatePhysicsSim, _Mapping]
        ] = ...,
        destroy_physics_sim: _Optional[
            _Union[CUserMsg_ParticleManager.DestroyPhysicsSim, _Mapping]
        ] = ...,
        set_vdata: _Optional[_Union[CUserMsg_ParticleManager.SetVData, _Mapping]] = ...,
        set_material_override: _Optional[
            _Union[CUserMsg_ParticleManager.SetMaterialOverride, _Mapping]
        ] = ...,
    ) -> None: ...

class EBaseUserMessages(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EBaseEntityMessages(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class eRollType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class PARTICLE_MESSAGE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EHapticPulseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
