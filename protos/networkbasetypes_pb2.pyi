from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

import network_connection_pb2 as _network_connection_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor
SIGNONSTATE_CHALLENGE: SignonState_t
SIGNONSTATE_CHANGELEVEL: SignonState_t
SIGNONSTATE_CONNECTED: SignonState_t
SIGNONSTATE_FULL: SignonState_t
SIGNONSTATE_NEW: SignonState_t
SIGNONSTATE_NONE: SignonState_t
SIGNONSTATE_PRESPAWN: SignonState_t
SIGNONSTATE_SPAWN: SignonState_t
SPAWN_GROUP_BLOCK_UNTIL_LOADED: SpawnGroupFlags_t
SPAWN_GROUP_CREATE_CLIENT_ONLY_ENTITIES: SpawnGroupFlags_t
SPAWN_GROUP_CREATE_NEW_SCENE_WORLD: SpawnGroupFlags_t
SPAWN_GROUP_DONT_SPAWN_ENTITIES: SpawnGroupFlags_t
SPAWN_GROUP_IS_INITIAL_SPAWN_GROUP: SpawnGroupFlags_t
SPAWN_GROUP_LOAD_ENTITIES_FROM_SAVE: SpawnGroupFlags_t
SPAWN_GROUP_LOAD_STREAMING_DATA: SpawnGroupFlags_t
SPAWN_GROUP_SYNCHRONOUS_SPAWN: SpawnGroupFlags_t
net_DebugOverlay: NET_Messages
net_Disconnect_Legacy: NET_Messages
net_NOP: NET_Messages
net_SetConVar: NET_Messages
net_SignonState: NET_Messages
net_SpawnGroup_Load: NET_Messages
net_SpawnGroup_LoadCompleted: NET_Messages
net_SpawnGroup_ManifestUpdate: NET_Messages
net_SpawnGroup_SetCreationTick: NET_Messages
net_SpawnGroup_Unload: NET_Messages
net_SplitScreenUser: NET_Messages
net_StringCmd: NET_Messages
net_Tick: NET_Messages

class CEntityMsg(_message.Message):
    __slots__ = ["target_entity"]
    TARGET_ENTITY_FIELD_NUMBER: _ClassVar[int]
    target_entity: int
    def __init__(self, target_entity: _Optional[int] = ...) -> None: ...

class CMsgPlayerInfo(_message.Message):
    __slots__ = ["fakeplayer", "ishltv", "name", "steamid", "userid", "xuid"]
    FAKEPLAYER_FIELD_NUMBER: _ClassVar[int]
    ISHLTV_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    XUID_FIELD_NUMBER: _ClassVar[int]
    fakeplayer: bool
    ishltv: bool
    name: str
    steamid: int
    userid: int
    xuid: int
    def __init__(
        self,
        name: _Optional[str] = ...,
        xuid: _Optional[int] = ...,
        userid: _Optional[int] = ...,
        steamid: _Optional[int] = ...,
        fakeplayer: bool = ...,
        ishltv: bool = ...,
    ) -> None: ...

class CMsgQAngle(_message.Message):
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

class CMsgQuaternion(_message.Message):
    __slots__ = ["w", "x", "y", "z"]
    W_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    w: float
    x: float
    y: float
    z: float
    def __init__(
        self,
        x: _Optional[float] = ...,
        y: _Optional[float] = ...,
        z: _Optional[float] = ...,
        w: _Optional[float] = ...,
    ) -> None: ...

class CMsgRGBA(_message.Message):
    __slots__ = ["a", "b", "g", "r"]
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    G_FIELD_NUMBER: _ClassVar[int]
    R_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: int
    g: int
    r: int
    def __init__(
        self,
        r: _Optional[int] = ...,
        g: _Optional[int] = ...,
        b: _Optional[int] = ...,
        a: _Optional[int] = ...,
    ) -> None: ...

class CMsgTransform(_message.Message):
    __slots__ = ["orientation", "position", "scale"]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    orientation: CMsgQuaternion
    position: CMsgVector
    scale: float
    def __init__(
        self,
        position: _Optional[_Union[CMsgVector, _Mapping]] = ...,
        scale: _Optional[float] = ...,
        orientation: _Optional[_Union[CMsgQuaternion, _Mapping]] = ...,
    ) -> None: ...

class CMsgVector(_message.Message):
    __slots__ = ["w", "x", "y", "z"]
    W_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    w: float
    x: float
    y: float
    z: float
    def __init__(
        self,
        x: _Optional[float] = ...,
        y: _Optional[float] = ...,
        z: _Optional[float] = ...,
        w: _Optional[float] = ...,
    ) -> None: ...

class CMsgVector2D(_message.Message):
    __slots__ = ["x", "y"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(
        self, x: _Optional[float] = ..., y: _Optional[float] = ...
    ) -> None: ...

class CMsg_CVars(_message.Message):
    __slots__ = ["cvars"]

    class CVar(_message.Message):
        __slots__ = ["name", "value"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(
            self, name: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    CVARS_FIELD_NUMBER: _ClassVar[int]
    cvars: _containers.RepeatedCompositeFieldContainer[CMsg_CVars.CVar]
    def __init__(
        self, cvars: _Optional[_Iterable[_Union[CMsg_CVars.CVar, _Mapping]]] = ...
    ) -> None: ...

class CNETMsg_DebugOverlay(_message.Message):
    __slots__ = [
        "bools",
        "colors",
        "dimensions",
        "etype",
        "strings",
        "times",
        "uint64s",
        "vectors",
    ]
    BOOLS_FIELD_NUMBER: _ClassVar[int]
    COLORS_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    ETYPE_FIELD_NUMBER: _ClassVar[int]
    STRINGS_FIELD_NUMBER: _ClassVar[int]
    TIMES_FIELD_NUMBER: _ClassVar[int]
    UINT64S_FIELD_NUMBER: _ClassVar[int]
    VECTORS_FIELD_NUMBER: _ClassVar[int]
    bools: _containers.RepeatedScalarFieldContainer[bool]
    colors: _containers.RepeatedCompositeFieldContainer[CMsgRGBA]
    dimensions: _containers.RepeatedScalarFieldContainer[float]
    etype: int
    strings: _containers.RepeatedScalarFieldContainer[str]
    times: _containers.RepeatedScalarFieldContainer[float]
    uint64s: _containers.RepeatedScalarFieldContainer[int]
    vectors: _containers.RepeatedCompositeFieldContainer[CMsgVector]
    def __init__(
        self,
        etype: _Optional[int] = ...,
        vectors: _Optional[_Iterable[_Union[CMsgVector, _Mapping]]] = ...,
        colors: _Optional[_Iterable[_Union[CMsgRGBA, _Mapping]]] = ...,
        dimensions: _Optional[_Iterable[float]] = ...,
        times: _Optional[_Iterable[float]] = ...,
        bools: _Optional[_Iterable[bool]] = ...,
        uint64s: _Optional[_Iterable[int]] = ...,
        strings: _Optional[_Iterable[str]] = ...,
    ) -> None: ...

class CNETMsg_NOP(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CNETMsg_SetConVar(_message.Message):
    __slots__ = ["convars"]
    CONVARS_FIELD_NUMBER: _ClassVar[int]
    convars: CMsg_CVars
    def __init__(
        self, convars: _Optional[_Union[CMsg_CVars, _Mapping]] = ...
    ) -> None: ...

class CNETMsg_SignonState(_message.Message):
    __slots__ = [
        "addons",
        "map_name",
        "num_server_players",
        "players_networkids",
        "signon_state",
        "spawn_count",
    ]
    ADDONS_FIELD_NUMBER: _ClassVar[int]
    MAP_NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_SERVER_PLAYERS_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_NETWORKIDS_FIELD_NUMBER: _ClassVar[int]
    SIGNON_STATE_FIELD_NUMBER: _ClassVar[int]
    SPAWN_COUNT_FIELD_NUMBER: _ClassVar[int]
    addons: str
    map_name: str
    num_server_players: int
    players_networkids: _containers.RepeatedScalarFieldContainer[str]
    signon_state: SignonState_t
    spawn_count: int
    def __init__(
        self,
        signon_state: _Optional[_Union[SignonState_t, str]] = ...,
        spawn_count: _Optional[int] = ...,
        num_server_players: _Optional[int] = ...,
        players_networkids: _Optional[_Iterable[str]] = ...,
        map_name: _Optional[str] = ...,
        addons: _Optional[str] = ...,
    ) -> None: ...

class CNETMsg_SpawnGroup_Load(_message.Message):
    __slots__ = [
        "creationsequence",
        "entityfiltername",
        "entitylumpname",
        "flags",
        "leveltransition",
        "localnamefixup",
        "manifestincomplete",
        "manifestloadpriority",
        "parentnamefixup",
        "savegamefilename",
        "spawngrouphandle",
        "spawngroupmanifest",
        "spawngroupownerhandle",
        "spawngroupparenthandle",
        "tickcount",
        "world_offset_angle",
        "world_offset_pos",
        "worldgroupid",
        "worldgroupname",
        "worldname",
    ]
    CREATIONSEQUENCE_FIELD_NUMBER: _ClassVar[int]
    ENTITYFILTERNAME_FIELD_NUMBER: _ClassVar[int]
    ENTITYLUMPNAME_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    LEVELTRANSITION_FIELD_NUMBER: _ClassVar[int]
    LOCALNAMEFIXUP_FIELD_NUMBER: _ClassVar[int]
    MANIFESTINCOMPLETE_FIELD_NUMBER: _ClassVar[int]
    MANIFESTLOADPRIORITY_FIELD_NUMBER: _ClassVar[int]
    PARENTNAMEFIXUP_FIELD_NUMBER: _ClassVar[int]
    SAVEGAMEFILENAME_FIELD_NUMBER: _ClassVar[int]
    SPAWNGROUPHANDLE_FIELD_NUMBER: _ClassVar[int]
    SPAWNGROUPMANIFEST_FIELD_NUMBER: _ClassVar[int]
    SPAWNGROUPOWNERHANDLE_FIELD_NUMBER: _ClassVar[int]
    SPAWNGROUPPARENTHANDLE_FIELD_NUMBER: _ClassVar[int]
    TICKCOUNT_FIELD_NUMBER: _ClassVar[int]
    WORLDGROUPID_FIELD_NUMBER: _ClassVar[int]
    WORLDGROUPNAME_FIELD_NUMBER: _ClassVar[int]
    WORLDNAME_FIELD_NUMBER: _ClassVar[int]
    WORLD_OFFSET_ANGLE_FIELD_NUMBER: _ClassVar[int]
    WORLD_OFFSET_POS_FIELD_NUMBER: _ClassVar[int]
    creationsequence: int
    entityfiltername: str
    entitylumpname: str
    flags: int
    leveltransition: bool
    localnamefixup: str
    manifestincomplete: bool
    manifestloadpriority: int
    parentnamefixup: str
    savegamefilename: str
    spawngrouphandle: int
    spawngroupmanifest: bytes
    spawngroupownerhandle: int
    spawngroupparenthandle: int
    tickcount: int
    world_offset_angle: CMsgQAngle
    world_offset_pos: CMsgVector
    worldgroupid: int
    worldgroupname: str
    worldname: str
    def __init__(
        self,
        worldname: _Optional[str] = ...,
        entitylumpname: _Optional[str] = ...,
        entityfiltername: _Optional[str] = ...,
        spawngrouphandle: _Optional[int] = ...,
        spawngroupownerhandle: _Optional[int] = ...,
        world_offset_pos: _Optional[_Union[CMsgVector, _Mapping]] = ...,
        world_offset_angle: _Optional[_Union[CMsgQAngle, _Mapping]] = ...,
        spawngroupmanifest: _Optional[bytes] = ...,
        flags: _Optional[int] = ...,
        tickcount: _Optional[int] = ...,
        manifestincomplete: bool = ...,
        localnamefixup: _Optional[str] = ...,
        parentnamefixup: _Optional[str] = ...,
        manifestloadpriority: _Optional[int] = ...,
        worldgroupid: _Optional[int] = ...,
        creationsequence: _Optional[int] = ...,
        savegamefilename: _Optional[str] = ...,
        spawngroupparenthandle: _Optional[int] = ...,
        leveltransition: bool = ...,
        worldgroupname: _Optional[str] = ...,
    ) -> None: ...

class CNETMsg_SpawnGroup_LoadCompleted(_message.Message):
    __slots__ = ["spawngrouphandle"]
    SPAWNGROUPHANDLE_FIELD_NUMBER: _ClassVar[int]
    spawngrouphandle: int
    def __init__(self, spawngrouphandle: _Optional[int] = ...) -> None: ...

class CNETMsg_SpawnGroup_ManifestUpdate(_message.Message):
    __slots__ = ["manifestincomplete", "spawngrouphandle", "spawngroupmanifest"]
    MANIFESTINCOMPLETE_FIELD_NUMBER: _ClassVar[int]
    SPAWNGROUPHANDLE_FIELD_NUMBER: _ClassVar[int]
    SPAWNGROUPMANIFEST_FIELD_NUMBER: _ClassVar[int]
    manifestincomplete: bool
    spawngrouphandle: int
    spawngroupmanifest: bytes
    def __init__(
        self,
        spawngrouphandle: _Optional[int] = ...,
        spawngroupmanifest: _Optional[bytes] = ...,
        manifestincomplete: bool = ...,
    ) -> None: ...

class CNETMsg_SpawnGroup_SetCreationTick(_message.Message):
    __slots__ = ["creationsequence", "spawngrouphandle", "tickcount"]
    CREATIONSEQUENCE_FIELD_NUMBER: _ClassVar[int]
    SPAWNGROUPHANDLE_FIELD_NUMBER: _ClassVar[int]
    TICKCOUNT_FIELD_NUMBER: _ClassVar[int]
    creationsequence: int
    spawngrouphandle: int
    tickcount: int
    def __init__(
        self,
        spawngrouphandle: _Optional[int] = ...,
        tickcount: _Optional[int] = ...,
        creationsequence: _Optional[int] = ...,
    ) -> None: ...

class CNETMsg_SpawnGroup_Unload(_message.Message):
    __slots__ = ["flags", "spawngrouphandle", "tickcount"]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    SPAWNGROUPHANDLE_FIELD_NUMBER: _ClassVar[int]
    TICKCOUNT_FIELD_NUMBER: _ClassVar[int]
    flags: int
    spawngrouphandle: int
    tickcount: int
    def __init__(
        self,
        spawngrouphandle: _Optional[int] = ...,
        flags: _Optional[int] = ...,
        tickcount: _Optional[int] = ...,
    ) -> None: ...

class CNETMsg_SplitScreenUser(_message.Message):
    __slots__ = ["slot"]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    slot: int
    def __init__(self, slot: _Optional[int] = ...) -> None: ...

class CNETMsg_StringCmd(_message.Message):
    __slots__ = ["command", "prediction_sync"]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_SYNC_FIELD_NUMBER: _ClassVar[int]
    command: str
    prediction_sync: int
    def __init__(
        self, command: _Optional[str] = ..., prediction_sync: _Optional[int] = ...
    ) -> None: ...

class CNETMsg_Tick(_message.Message):
    __slots__ = [
        "expected_long_tick",
        "expected_long_tick_reason",
        "hltv_replay_flags",
        "host_computationtime",
        "host_computationtime_std_deviation",
        "host_framestarttime_std_deviation",
        "host_frametime",
        "host_frametime_std_deviation",
        "host_loss",
        "host_unfiltered_frametime",
        "jitter",
        "tick",
    ]
    EXPECTED_LONG_TICK_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_LONG_TICK_REASON_FIELD_NUMBER: _ClassVar[int]
    HLTV_REPLAY_FLAGS_FIELD_NUMBER: _ClassVar[int]
    HOST_COMPUTATIONTIME_FIELD_NUMBER: _ClassVar[int]
    HOST_COMPUTATIONTIME_STD_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    HOST_FRAMESTARTTIME_STD_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    HOST_FRAMETIME_FIELD_NUMBER: _ClassVar[int]
    HOST_FRAMETIME_STD_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    HOST_LOSS_FIELD_NUMBER: _ClassVar[int]
    HOST_UNFILTERED_FRAMETIME_FIELD_NUMBER: _ClassVar[int]
    JITTER_FIELD_NUMBER: _ClassVar[int]
    TICK_FIELD_NUMBER: _ClassVar[int]
    expected_long_tick: int
    expected_long_tick_reason: str
    hltv_replay_flags: int
    host_computationtime: int
    host_computationtime_std_deviation: int
    host_framestarttime_std_deviation: int
    host_frametime: int
    host_frametime_std_deviation: int
    host_loss: int
    host_unfiltered_frametime: int
    jitter: int
    tick: int
    def __init__(
        self,
        tick: _Optional[int] = ...,
        host_frametime: _Optional[int] = ...,
        host_frametime_std_deviation: _Optional[int] = ...,
        host_computationtime: _Optional[int] = ...,
        host_computationtime_std_deviation: _Optional[int] = ...,
        host_framestarttime_std_deviation: _Optional[int] = ...,
        host_loss: _Optional[int] = ...,
        host_unfiltered_frametime: _Optional[int] = ...,
        hltv_replay_flags: _Optional[int] = ...,
        expected_long_tick: _Optional[int] = ...,
        expected_long_tick_reason: _Optional[str] = ...,
        jitter: _Optional[int] = ...,
    ) -> None: ...

class CSVCMsgList_GameEvents(_message.Message):
    __slots__ = ["events"]

    class event_t(_message.Message):
        __slots__ = ["event", "tick"]
        EVENT_FIELD_NUMBER: _ClassVar[int]
        TICK_FIELD_NUMBER: _ClassVar[int]
        event: CSVCMsg_GameEvent
        tick: int
        def __init__(
            self,
            tick: _Optional[int] = ...,
            event: _Optional[_Union[CSVCMsg_GameEvent, _Mapping]] = ...,
        ) -> None: ...

    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[CSVCMsgList_GameEvents.event_t]
    def __init__(
        self,
        events: _Optional[
            _Iterable[_Union[CSVCMsgList_GameEvents.event_t, _Mapping]]
        ] = ...,
    ) -> None: ...

class CSVCMsg_GameEvent(_message.Message):
    __slots__ = ["event_name", "eventid", "keys"]

    class key_t(_message.Message):
        __slots__ = [
            "type",
            "val_bool",
            "val_byte",
            "val_float",
            "val_long",
            "val_short",
            "val_string",
            "val_uint64",
        ]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VAL_BOOL_FIELD_NUMBER: _ClassVar[int]
        VAL_BYTE_FIELD_NUMBER: _ClassVar[int]
        VAL_FLOAT_FIELD_NUMBER: _ClassVar[int]
        VAL_LONG_FIELD_NUMBER: _ClassVar[int]
        VAL_SHORT_FIELD_NUMBER: _ClassVar[int]
        VAL_STRING_FIELD_NUMBER: _ClassVar[int]
        VAL_UINT64_FIELD_NUMBER: _ClassVar[int]
        type: int
        val_bool: bool
        val_byte: int
        val_float: float
        val_long: int
        val_short: int
        val_string: str
        val_uint64: int
        def __init__(
            self,
            type: _Optional[int] = ...,
            val_string: _Optional[str] = ...,
            val_float: _Optional[float] = ...,
            val_long: _Optional[int] = ...,
            val_short: _Optional[int] = ...,
            val_byte: _Optional[int] = ...,
            val_bool: bool = ...,
            val_uint64: _Optional[int] = ...,
        ) -> None: ...

    EVENTID_FIELD_NUMBER: _ClassVar[int]
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    eventid: int
    keys: _containers.RepeatedCompositeFieldContainer[CSVCMsg_GameEvent.key_t]
    def __init__(
        self,
        event_name: _Optional[str] = ...,
        eventid: _Optional[int] = ...,
        keys: _Optional[_Iterable[_Union[CSVCMsg_GameEvent.key_t, _Mapping]]] = ...,
    ) -> None: ...

class CSVCMsg_GameSessionConfiguration(_message.Message):
    __slots__ = [
        "data",
        "gamemode",
        "hostname",
        "is_background_map",
        "is_headless",
        "is_loadsavegame",
        "is_localonly",
        "is_multiplayer",
        "is_transition",
        "landmarkname",
        "max_client_limit",
        "max_clients",
        "min_client_limit",
        "no_steam_server",
        "previouslevel",
        "s1_mapname",
        "savegamename",
        "server_ip_address",
        "tick_interval",
    ]
    DATA_FIELD_NUMBER: _ClassVar[int]
    GAMEMODE_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    IS_BACKGROUND_MAP_FIELD_NUMBER: _ClassVar[int]
    IS_HEADLESS_FIELD_NUMBER: _ClassVar[int]
    IS_LOADSAVEGAME_FIELD_NUMBER: _ClassVar[int]
    IS_LOCALONLY_FIELD_NUMBER: _ClassVar[int]
    IS_MULTIPLAYER_FIELD_NUMBER: _ClassVar[int]
    IS_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    LANDMARKNAME_FIELD_NUMBER: _ClassVar[int]
    MAX_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    MAX_CLIENT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MIN_CLIENT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    NO_STEAM_SERVER_FIELD_NUMBER: _ClassVar[int]
    PREVIOUSLEVEL_FIELD_NUMBER: _ClassVar[int]
    S1_MAPNAME_FIELD_NUMBER: _ClassVar[int]
    SAVEGAMENAME_FIELD_NUMBER: _ClassVar[int]
    SERVER_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TICK_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    gamemode: str
    hostname: str
    is_background_map: bool
    is_headless: bool
    is_loadsavegame: bool
    is_localonly: bool
    is_multiplayer: bool
    is_transition: bool
    landmarkname: str
    max_client_limit: int
    max_clients: int
    min_client_limit: int
    no_steam_server: bool
    previouslevel: str
    s1_mapname: str
    savegamename: str
    server_ip_address: str
    tick_interval: int
    def __init__(
        self,
        is_multiplayer: bool = ...,
        is_loadsavegame: bool = ...,
        is_background_map: bool = ...,
        is_headless: bool = ...,
        min_client_limit: _Optional[int] = ...,
        max_client_limit: _Optional[int] = ...,
        max_clients: _Optional[int] = ...,
        tick_interval: _Optional[int] = ...,
        hostname: _Optional[str] = ...,
        savegamename: _Optional[str] = ...,
        s1_mapname: _Optional[str] = ...,
        gamemode: _Optional[str] = ...,
        server_ip_address: _Optional[str] = ...,
        data: _Optional[bytes] = ...,
        is_localonly: bool = ...,
        no_steam_server: bool = ...,
        is_transition: bool = ...,
        previouslevel: _Optional[str] = ...,
        landmarkname: _Optional[str] = ...,
    ) -> None: ...

class SignonState_t(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class NET_Messages(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SpawnGroupFlags_t(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
