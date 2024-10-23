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

DESCRIPTOR: _descriptor.FileDescriptor
DIALOG_ASKCONNECT: DIALOG_TYPE
DIALOG_ENTRY: DIALOG_TYPE
DIALOG_MENU: DIALOG_TYPE
DIALOG_MSG: DIALOG_TYPE
DIALOG_TEXT: DIALOG_TYPE
MSG_SPLITSCREEN_ADDUSER: ESplitScreenMessageType
MSG_SPLITSCREEN_REMOVEUSER: ESplitScreenMessageType
PFT_SOUND: PrefetchType
REPLAY_EVENT_CANCEL: ReplayEventType_t
REPLAY_EVENT_DEATH: ReplayEventType_t
REPLAY_EVENT_GENERIC: ReplayEventType_t
REPLAY_EVENT_STUCK_NEED_FULL_UPDATE: ReplayEventType_t
REPLAY_EVENT_VICTORY: ReplayEventType_t
RP_PAUSE: RequestPause_t
RP_TOGGLEPAUSE: RequestPause_t
RP_UNPAUSE: RequestPause_t
VOICEDATA_FORMAT_ENGINE: VoiceDataFormat_t
VOICEDATA_FORMAT_OPUS: VoiceDataFormat_t
VOICEDATA_FORMAT_STEAM: VoiceDataFormat_t
bi_GameEvent: Bidirectional_Messages
bi_RebroadcastGameEvent: Bidirectional_Messages
bi_RebroadcastSource: Bidirectional_Messages
bi_RelayInfo: Bidirectional_Messages_LowFrequency
bi_RelayPacket: Bidirectional_Messages_LowFrequency
clc_BaselineAck: CLC_Messages
clc_ClientInfo: CLC_Messages
clc_CmdKeyValues: CLC_Messages
clc_Diagnostic: CLC_Messages
clc_FileCRCCheck: CLC_Messages
clc_HltvReplay: CLC_Messages
clc_LoadingProgress: CLC_Messages
clc_Move: CLC_Messages
clc_RconServerDetails: CLC_Messages
clc_RequestPause: CLC_Messages
clc_RespondCvarValue: CLC_Messages
clc_ServerStatus: CLC_Messages
clc_SplitPlayerConnect: CLC_Messages
clc_SplitPlayerDisconnect: CLC_Messages
clc_VoiceData: CLC_Messages
eQueryCvarValueStatus_CvarNotFound: EQueryCvarValueStatus
eQueryCvarValueStatus_CvarProtected: EQueryCvarValueStatus
eQueryCvarValueStatus_NotACvar: EQueryCvarValueStatus
eQueryCvarValueStatus_ValueIntact: EQueryCvarValueStatus
svc_BSPDecal: SVC_Messages
svc_Broadcast_Command: SVC_Messages
svc_ClassInfo: SVC_Messages
svc_ClearAllStringTables: SVC_Messages
svc_CmdKeyValues: SVC_Messages
svc_CreateStringTable: SVC_Messages
svc_FlattenedSerializer: SVC_Messages
svc_FullFrameSplit: SVC_Messages
svc_GetCvarValue: SVC_Messages
svc_HLTVStatus: SVC_Messages
svc_HltvFixupOperatorStatus: SVC_Messages
svc_Menu: SVC_Messages
svc_PacketEntities: SVC_Messages
svc_PacketReliable: SVC_Messages
svc_PeerList: SVC_Messages
svc_Prefetch: SVC_Messages
svc_Print: SVC_Messages
svc_RconServerDetails: SVC_Messages
svc_ServerInfo: SVC_Messages
svc_ServerSteamID: SVC_Messages
svc_SetPause: SVC_Messages
svc_SetView: SVC_Messages
svc_Sounds: SVC_Messages
svc_SplitScreen: SVC_Messages
svc_StopSound: SVC_Messages
svc_UpdateStringTable: SVC_Messages
svc_UserCmds: SVC_Messages
svc_UserMessage: SVC_Messages
svc_VoiceData: SVC_Messages
svc_VoiceInit: SVC_Messages
svc_dummy: SVC_Messages_LowFrequency

class CBidirMsg_RebroadcastGameEvent(_message.Message):
    __slots__ = ["buftype", "clientbitcount", "posttoserver", "receivingclients"]
    BUFTYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENTBITCOUNT_FIELD_NUMBER: _ClassVar[int]
    POSTTOSERVER_FIELD_NUMBER: _ClassVar[int]
    RECEIVINGCLIENTS_FIELD_NUMBER: _ClassVar[int]
    buftype: int
    clientbitcount: int
    posttoserver: bool
    receivingclients: int
    def __init__(
        self,
        posttoserver: bool = ...,
        buftype: _Optional[int] = ...,
        clientbitcount: _Optional[int] = ...,
        receivingclients: _Optional[int] = ...,
    ) -> None: ...

class CBidirMsg_RebroadcastSource(_message.Message):
    __slots__ = ["eventsource"]
    EVENTSOURCE_FIELD_NUMBER: _ClassVar[int]
    eventsource: int
    def __init__(self, eventsource: _Optional[int] = ...) -> None: ...

class CCLCMsg_BaselineAck(_message.Message):
    __slots__ = ["baseline_nr", "baseline_tick"]
    BASELINE_NR_FIELD_NUMBER: _ClassVar[int]
    BASELINE_TICK_FIELD_NUMBER: _ClassVar[int]
    baseline_nr: int
    baseline_tick: int
    def __init__(
        self, baseline_tick: _Optional[int] = ..., baseline_nr: _Optional[int] = ...
    ) -> None: ...

class CCLCMsg_ClientInfo(_message.Message):
    __slots__ = [
        "friends_id",
        "friends_name",
        "is_hltv",
        "send_table_crc",
        "server_count",
    ]
    FRIENDS_ID_FIELD_NUMBER: _ClassVar[int]
    FRIENDS_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_HLTV_FIELD_NUMBER: _ClassVar[int]
    SEND_TABLE_CRC_FIELD_NUMBER: _ClassVar[int]
    SERVER_COUNT_FIELD_NUMBER: _ClassVar[int]
    friends_id: int
    friends_name: str
    is_hltv: bool
    send_table_crc: int
    server_count: int
    def __init__(
        self,
        send_table_crc: _Optional[int] = ...,
        server_count: _Optional[int] = ...,
        is_hltv: bool = ...,
        friends_id: _Optional[int] = ...,
        friends_name: _Optional[str] = ...,
    ) -> None: ...

class CCLCMsg_CmdKeyValues(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class CCLCMsg_Diagnostic(_message.Message):
    __slots__ = ["system_specs", "vprof_report"]
    SYSTEM_SPECS_FIELD_NUMBER: _ClassVar[int]
    VPROF_REPORT_FIELD_NUMBER: _ClassVar[int]
    system_specs: CMsgSource2SystemSpecs
    vprof_report: CMsgSource2VProfLiteReport
    def __init__(
        self,
        system_specs: _Optional[_Union[CMsgSource2SystemSpecs, _Mapping]] = ...,
        vprof_report: _Optional[_Union[CMsgSource2VProfLiteReport, _Mapping]] = ...,
    ) -> None: ...

class CCLCMsg_FileCRCCheck(_message.Message):
    __slots__ = ["code_filename", "code_path", "crc", "filename", "path"]
    CODE_FILENAME_FIELD_NUMBER: _ClassVar[int]
    CODE_PATH_FIELD_NUMBER: _ClassVar[int]
    CRC_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    code_filename: int
    code_path: int
    crc: int
    filename: str
    path: str
    def __init__(
        self,
        code_path: _Optional[int] = ...,
        path: _Optional[str] = ...,
        code_filename: _Optional[int] = ...,
        filename: _Optional[str] = ...,
        crc: _Optional[int] = ...,
    ) -> None: ...

class CCLCMsg_HltvFixupOperatorTick(_message.Message):
    __slots__ = [
        "cameraman_scoreboard",
        "eye_angles",
        "observer_mode",
        "observer_target",
        "origin",
        "props_data",
        "tick",
        "view_offset",
    ]
    CAMERAMAN_SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
    EYE_ANGLES_FIELD_NUMBER: _ClassVar[int]
    OBSERVER_MODE_FIELD_NUMBER: _ClassVar[int]
    OBSERVER_TARGET_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PROPS_DATA_FIELD_NUMBER: _ClassVar[int]
    TICK_FIELD_NUMBER: _ClassVar[int]
    VIEW_OFFSET_FIELD_NUMBER: _ClassVar[int]
    cameraman_scoreboard: bool
    eye_angles: _networkbasetypes_pb2.CMsgQAngle
    observer_mode: int
    observer_target: int
    origin: _networkbasetypes_pb2.CMsgVector
    props_data: bytes
    tick: int
    view_offset: _networkbasetypes_pb2.CMsgVector
    def __init__(
        self,
        tick: _Optional[int] = ...,
        props_data: _Optional[bytes] = ...,
        origin: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...,
        eye_angles: _Optional[_Union[_networkbasetypes_pb2.CMsgQAngle, _Mapping]] = ...,
        observer_mode: _Optional[int] = ...,
        cameraman_scoreboard: bool = ...,
        observer_target: _Optional[int] = ...,
        view_offset: _Optional[
            _Union[_networkbasetypes_pb2.CMsgVector, _Mapping]
        ] = ...,
    ) -> None: ...

class CCLCMsg_HltvReplay(_message.Message):
    __slots__ = [
        "event_time",
        "primary_target",
        "request",
        "slowdown_length",
        "slowdown_rate",
    ]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_TARGET_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    SLOWDOWN_LENGTH_FIELD_NUMBER: _ClassVar[int]
    SLOWDOWN_RATE_FIELD_NUMBER: _ClassVar[int]
    event_time: float
    primary_target: int
    request: int
    slowdown_length: float
    slowdown_rate: float
    def __init__(
        self,
        request: _Optional[int] = ...,
        slowdown_length: _Optional[float] = ...,
        slowdown_rate: _Optional[float] = ...,
        primary_target: _Optional[int] = ...,
        event_time: _Optional[float] = ...,
    ) -> None: ...

class CCLCMsg_ListenEvents(_message.Message):
    __slots__ = ["event_mask"]
    EVENT_MASK_FIELD_NUMBER: _ClassVar[int]
    event_mask: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, event_mask: _Optional[_Iterable[int]] = ...) -> None: ...

class CCLCMsg_LoadingProgress(_message.Message):
    __slots__ = ["progress"]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    progress: int
    def __init__(self, progress: _Optional[int] = ...) -> None: ...

class CCLCMsg_Move(_message.Message):
    __slots__ = ["data", "last_command_number"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    LAST_COMMAND_NUMBER_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    last_command_number: int
    def __init__(
        self, data: _Optional[bytes] = ..., last_command_number: _Optional[int] = ...
    ) -> None: ...

class CCLCMsg_RconServerDetails(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: bytes
    def __init__(self, token: _Optional[bytes] = ...) -> None: ...

class CCLCMsg_RequestPause(_message.Message):
    __slots__ = ["pause_group", "pause_type"]
    PAUSE_GROUP_FIELD_NUMBER: _ClassVar[int]
    PAUSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    pause_group: int
    pause_type: RequestPause_t
    def __init__(
        self,
        pause_type: _Optional[_Union[RequestPause_t, str]] = ...,
        pause_group: _Optional[int] = ...,
    ) -> None: ...

class CCLCMsg_RespondCvarValue(_message.Message):
    __slots__ = ["cookie", "name", "status_code", "value"]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    cookie: int
    name: str
    status_code: int
    value: str
    def __init__(
        self,
        cookie: _Optional[int] = ...,
        status_code: _Optional[int] = ...,
        name: _Optional[str] = ...,
        value: _Optional[str] = ...,
    ) -> None: ...

class CCLCMsg_ServerStatus(_message.Message):
    __slots__ = ["simplified"]
    SIMPLIFIED_FIELD_NUMBER: _ClassVar[int]
    simplified: bool
    def __init__(self, simplified: bool = ...) -> None: ...

class CCLCMsg_SplitPlayerConnect(_message.Message):
    __slots__ = ["playername"]
    PLAYERNAME_FIELD_NUMBER: _ClassVar[int]
    playername: str
    def __init__(self, playername: _Optional[str] = ...) -> None: ...

class CCLCMsg_SplitPlayerDisconnect(_message.Message):
    __slots__ = ["slot"]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    slot: int
    def __init__(self, slot: _Optional[int] = ...) -> None: ...

class CCLCMsg_VoiceData(_message.Message):
    __slots__ = ["audio", "tick", "xuid"]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    TICK_FIELD_NUMBER: _ClassVar[int]
    XUID_FIELD_NUMBER: _ClassVar[int]
    audio: CMsgVoiceAudio
    tick: int
    xuid: int
    def __init__(
        self,
        audio: _Optional[_Union[CMsgVoiceAudio, _Mapping]] = ...,
        xuid: _Optional[int] = ...,
        tick: _Optional[int] = ...,
    ) -> None: ...

class CMsgIPCAddress(_message.Message):
    __slots__ = ["computer_guid", "process_id"]
    COMPUTER_GUID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
    computer_guid: int
    process_id: int
    def __init__(
        self, computer_guid: _Optional[int] = ..., process_id: _Optional[int] = ...
    ) -> None: ...

class CMsgServerNetworkStats(_message.Message):
    __slots__ = [
        "avg_data_in",
        "avg_data_out",
        "avg_engine_latency_out",
        "avg_loss_in",
        "avg_loss_out",
        "avg_packets_in",
        "avg_packets_out",
        "avg_ping_ms",
        "cpu_usage",
        "dedicated",
        "fps",
        "memory_free_mb",
        "memory_used_mb",
        "num_bots",
        "num_clients",
        "num_spectators",
        "num_tv_relays",
        "players",
        "ports",
        "spawn_count",
        "total_data_in",
        "total_data_out",
        "total_packets_in",
        "total_packets_out",
        "uptime",
    ]

    class Player(_message.Message):
        __slots__ = [
            "engine_latency_ms",
            "is_bot",
            "loss_in",
            "loss_out",
            "packet_loss_pct",
            "ping_avg_ms",
            "remote_addr",
            "steamid",
        ]
        ENGINE_LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
        IS_BOT_FIELD_NUMBER: _ClassVar[int]
        LOSS_IN_FIELD_NUMBER: _ClassVar[int]
        LOSS_OUT_FIELD_NUMBER: _ClassVar[int]
        PACKET_LOSS_PCT_FIELD_NUMBER: _ClassVar[int]
        PING_AVG_MS_FIELD_NUMBER: _ClassVar[int]
        REMOTE_ADDR_FIELD_NUMBER: _ClassVar[int]
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        engine_latency_ms: int
        is_bot: bool
        loss_in: float
        loss_out: float
        packet_loss_pct: float
        ping_avg_ms: int
        remote_addr: str
        steamid: int
        def __init__(
            self,
            steamid: _Optional[int] = ...,
            remote_addr: _Optional[str] = ...,
            ping_avg_ms: _Optional[int] = ...,
            packet_loss_pct: _Optional[float] = ...,
            is_bot: bool = ...,
            loss_in: _Optional[float] = ...,
            loss_out: _Optional[float] = ...,
            engine_latency_ms: _Optional[int] = ...,
        ) -> None: ...

    class Port(_message.Message):
        __slots__ = ["name", "port"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        name: str
        port: int
        def __init__(
            self, port: _Optional[int] = ..., name: _Optional[str] = ...
        ) -> None: ...

    AVG_DATA_IN_FIELD_NUMBER: _ClassVar[int]
    AVG_DATA_OUT_FIELD_NUMBER: _ClassVar[int]
    AVG_ENGINE_LATENCY_OUT_FIELD_NUMBER: _ClassVar[int]
    AVG_LOSS_IN_FIELD_NUMBER: _ClassVar[int]
    AVG_LOSS_OUT_FIELD_NUMBER: _ClassVar[int]
    AVG_PACKETS_IN_FIELD_NUMBER: _ClassVar[int]
    AVG_PACKETS_OUT_FIELD_NUMBER: _ClassVar[int]
    AVG_PING_MS_FIELD_NUMBER: _ClassVar[int]
    CPU_USAGE_FIELD_NUMBER: _ClassVar[int]
    DEDICATED_FIELD_NUMBER: _ClassVar[int]
    FPS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FREE_MB_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USED_MB_FIELD_NUMBER: _ClassVar[int]
    NUM_BOTS_FIELD_NUMBER: _ClassVar[int]
    NUM_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    NUM_SPECTATORS_FIELD_NUMBER: _ClassVar[int]
    NUM_TV_RELAYS_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    SPAWN_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DATA_IN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DATA_OUT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PACKETS_IN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PACKETS_OUT_FIELD_NUMBER: _ClassVar[int]
    UPTIME_FIELD_NUMBER: _ClassVar[int]
    avg_data_in: float
    avg_data_out: float
    avg_engine_latency_out: float
    avg_loss_in: float
    avg_loss_out: float
    avg_packets_in: float
    avg_packets_out: float
    avg_ping_ms: float
    cpu_usage: int
    dedicated: bool
    fps: float
    memory_free_mb: int
    memory_used_mb: int
    num_bots: int
    num_clients: int
    num_spectators: int
    num_tv_relays: int
    players: _containers.RepeatedCompositeFieldContainer[CMsgServerNetworkStats.Player]
    ports: _containers.RepeatedCompositeFieldContainer[CMsgServerNetworkStats.Port]
    spawn_count: int
    total_data_in: int
    total_data_out: int
    total_packets_in: int
    total_packets_out: int
    uptime: int
    def __init__(
        self,
        dedicated: bool = ...,
        cpu_usage: _Optional[int] = ...,
        memory_used_mb: _Optional[int] = ...,
        memory_free_mb: _Optional[int] = ...,
        uptime: _Optional[int] = ...,
        spawn_count: _Optional[int] = ...,
        num_clients: _Optional[int] = ...,
        num_bots: _Optional[int] = ...,
        num_spectators: _Optional[int] = ...,
        num_tv_relays: _Optional[int] = ...,
        fps: _Optional[float] = ...,
        ports: _Optional[
            _Iterable[_Union[CMsgServerNetworkStats.Port, _Mapping]]
        ] = ...,
        avg_ping_ms: _Optional[float] = ...,
        avg_engine_latency_out: _Optional[float] = ...,
        avg_packets_out: _Optional[float] = ...,
        avg_packets_in: _Optional[float] = ...,
        avg_loss_out: _Optional[float] = ...,
        avg_loss_in: _Optional[float] = ...,
        avg_data_out: _Optional[float] = ...,
        avg_data_in: _Optional[float] = ...,
        total_data_in: _Optional[int] = ...,
        total_packets_in: _Optional[int] = ...,
        total_data_out: _Optional[int] = ...,
        total_packets_out: _Optional[int] = ...,
        players: _Optional[
            _Iterable[_Union[CMsgServerNetworkStats.Player, _Mapping]]
        ] = ...,
    ) -> None: ...

class CMsgServerPeer(_message.Message):
    __slots__ = [
        "ipc",
        "is_listenserver_host",
        "player_slot",
        "steamid",
        "they_hear_you",
        "you_hear_them",
    ]
    IPC_FIELD_NUMBER: _ClassVar[int]
    IS_LISTENSERVER_HOST_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    THEY_HEAR_YOU_FIELD_NUMBER: _ClassVar[int]
    YOU_HEAR_THEM_FIELD_NUMBER: _ClassVar[int]
    ipc: CMsgIPCAddress
    is_listenserver_host: bool
    player_slot: int
    steamid: int
    they_hear_you: bool
    you_hear_them: bool
    def __init__(
        self,
        player_slot: _Optional[int] = ...,
        steamid: _Optional[int] = ...,
        ipc: _Optional[_Union[CMsgIPCAddress, _Mapping]] = ...,
        they_hear_you: bool = ...,
        you_hear_them: bool = ...,
        is_listenserver_host: bool = ...,
    ) -> None: ...

class CMsgServerUserCmd(_message.Message):
    __slots__ = [
        "client_tick",
        "cmd_number",
        "data",
        "player_slot",
        "server_tick_executed",
    ]
    CLIENT_TICK_FIELD_NUMBER: _ClassVar[int]
    CMD_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
    SERVER_TICK_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    client_tick: int
    cmd_number: int
    data: bytes
    player_slot: int
    server_tick_executed: int
    def __init__(
        self,
        data: _Optional[bytes] = ...,
        cmd_number: _Optional[int] = ...,
        player_slot: _Optional[int] = ...,
        server_tick_executed: _Optional[int] = ...,
        client_tick: _Optional[int] = ...,
    ) -> None: ...

class CMsgSource2SystemSpecs(_message.Message):
    __slots__ = [
        "cpu_brand",
        "cpu_id",
        "cpu_model",
        "cpu_num_physical",
        "gpu_driver_name",
        "gpu_driver_version_high",
        "gpu_driver_version_low",
        "gpu_dx_support_level",
        "gpu_rendersystem_dll_name",
        "gpu_texture_memory_size_mb",
        "gpu_vendor_id",
        "ram_physical_total_mb",
    ]
    CPU_BRAND_FIELD_NUMBER: _ClassVar[int]
    CPU_ID_FIELD_NUMBER: _ClassVar[int]
    CPU_MODEL_FIELD_NUMBER: _ClassVar[int]
    CPU_NUM_PHYSICAL_FIELD_NUMBER: _ClassVar[int]
    GPU_DRIVER_NAME_FIELD_NUMBER: _ClassVar[int]
    GPU_DRIVER_VERSION_HIGH_FIELD_NUMBER: _ClassVar[int]
    GPU_DRIVER_VERSION_LOW_FIELD_NUMBER: _ClassVar[int]
    GPU_DX_SUPPORT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    GPU_RENDERSYSTEM_DLL_NAME_FIELD_NUMBER: _ClassVar[int]
    GPU_TEXTURE_MEMORY_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    GPU_VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    RAM_PHYSICAL_TOTAL_MB_FIELD_NUMBER: _ClassVar[int]
    cpu_brand: str
    cpu_id: str
    cpu_model: int
    cpu_num_physical: int
    gpu_driver_name: str
    gpu_driver_version_high: int
    gpu_driver_version_low: int
    gpu_dx_support_level: int
    gpu_rendersystem_dll_name: str
    gpu_texture_memory_size_mb: int
    gpu_vendor_id: int
    ram_physical_total_mb: int
    def __init__(
        self,
        cpu_id: _Optional[str] = ...,
        cpu_brand: _Optional[str] = ...,
        cpu_model: _Optional[int] = ...,
        cpu_num_physical: _Optional[int] = ...,
        ram_physical_total_mb: _Optional[int] = ...,
        gpu_rendersystem_dll_name: _Optional[str] = ...,
        gpu_vendor_id: _Optional[int] = ...,
        gpu_driver_name: _Optional[str] = ...,
        gpu_driver_version_high: _Optional[int] = ...,
        gpu_driver_version_low: _Optional[int] = ...,
        gpu_dx_support_level: _Optional[int] = ...,
        gpu_texture_memory_size_mb: _Optional[int] = ...,
    ) -> None: ...

class CMsgSource2VProfLiteReport(_message.Message):
    __slots__ = ["discarded_frames", "items", "total"]
    DISCARDED_FRAMES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    discarded_frames: int
    items: _containers.RepeatedCompositeFieldContainer[CMsgSource2VProfLiteReportItem]
    total: CMsgSource2VProfLiteReportItem
    def __init__(
        self,
        total: _Optional[_Union[CMsgSource2VProfLiteReportItem, _Mapping]] = ...,
        items: _Optional[
            _Iterable[_Union[CMsgSource2VProfLiteReportItem, _Mapping]]
        ] = ...,
        discarded_frames: _Optional[int] = ...,
    ) -> None: ...

class CMsgSource2VProfLiteReportItem(_message.Message):
    __slots__ = [
        "active_samples",
        "name",
        "usec_avg_active",
        "usec_avg_all",
        "usec_max",
        "usec_p50_active",
        "usec_p50_all",
        "usec_p99_active",
        "usec_p99_all",
    ]
    ACTIVE_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USEC_AVG_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    USEC_AVG_ALL_FIELD_NUMBER: _ClassVar[int]
    USEC_MAX_FIELD_NUMBER: _ClassVar[int]
    USEC_P50_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    USEC_P50_ALL_FIELD_NUMBER: _ClassVar[int]
    USEC_P99_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    USEC_P99_ALL_FIELD_NUMBER: _ClassVar[int]
    active_samples: int
    name: str
    usec_avg_active: int
    usec_avg_all: int
    usec_max: int
    usec_p50_active: int
    usec_p50_all: int
    usec_p99_active: int
    usec_p99_all: int
    def __init__(
        self,
        name: _Optional[str] = ...,
        active_samples: _Optional[int] = ...,
        usec_max: _Optional[int] = ...,
        usec_avg_active: _Optional[int] = ...,
        usec_p50_active: _Optional[int] = ...,
        usec_p99_active: _Optional[int] = ...,
        usec_avg_all: _Optional[int] = ...,
        usec_p50_all: _Optional[int] = ...,
        usec_p99_all: _Optional[int] = ...,
    ) -> None: ...

class CMsgVoiceAudio(_message.Message):
    __slots__ = [
        "format",
        "num_packets",
        "packet_offsets",
        "sample_rate",
        "section_number",
        "sequence_bytes",
        "uncompressed_sample_offset",
        "voice_data",
        "voice_level",
    ]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    NUM_PACKETS_FIELD_NUMBER: _ClassVar[int]
    PACKET_OFFSETS_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    SECTION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_BYTES_FIELD_NUMBER: _ClassVar[int]
    UNCOMPRESSED_SAMPLE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    VOICE_DATA_FIELD_NUMBER: _ClassVar[int]
    VOICE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    format: VoiceDataFormat_t
    num_packets: int
    packet_offsets: _containers.RepeatedScalarFieldContainer[int]
    sample_rate: int
    section_number: int
    sequence_bytes: int
    uncompressed_sample_offset: int
    voice_data: bytes
    voice_level: float
    def __init__(
        self,
        format: _Optional[_Union[VoiceDataFormat_t, str]] = ...,
        voice_data: _Optional[bytes] = ...,
        sequence_bytes: _Optional[int] = ...,
        section_number: _Optional[int] = ...,
        sample_rate: _Optional[int] = ...,
        uncompressed_sample_offset: _Optional[int] = ...,
        num_packets: _Optional[int] = ...,
        packet_offsets: _Optional[_Iterable[int]] = ...,
        voice_level: _Optional[float] = ...,
    ) -> None: ...

class CSVCMsg_BSPDecal(_message.Message):
    __slots__ = [
        "decal_texture_index",
        "entity_index",
        "low_priority",
        "model_index",
        "pos",
    ]
    DECAL_TEXTURE_INDEX_FIELD_NUMBER: _ClassVar[int]
    ENTITY_INDEX_FIELD_NUMBER: _ClassVar[int]
    LOW_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    MODEL_INDEX_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    decal_texture_index: int
    entity_index: int
    low_priority: bool
    model_index: int
    pos: _networkbasetypes_pb2.CMsgVector
    def __init__(
        self,
        pos: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...,
        decal_texture_index: _Optional[int] = ...,
        entity_index: _Optional[int] = ...,
        model_index: _Optional[int] = ...,
        low_priority: bool = ...,
    ) -> None: ...

class CSVCMsg_Broadcast_Command(_message.Message):
    __slots__ = ["cmd"]
    CMD_FIELD_NUMBER: _ClassVar[int]
    cmd: str
    def __init__(self, cmd: _Optional[str] = ...) -> None: ...

class CSVCMsg_ClassInfo(_message.Message):
    __slots__ = ["classes", "create_on_client"]

    class class_t(_message.Message):
        __slots__ = ["class_id", "class_name"]
        CLASS_ID_FIELD_NUMBER: _ClassVar[int]
        CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
        class_id: int
        class_name: str
        def __init__(
            self, class_id: _Optional[int] = ..., class_name: _Optional[str] = ...
        ) -> None: ...

    CLASSES_FIELD_NUMBER: _ClassVar[int]
    CREATE_ON_CLIENT_FIELD_NUMBER: _ClassVar[int]
    classes: _containers.RepeatedCompositeFieldContainer[CSVCMsg_ClassInfo.class_t]
    create_on_client: bool
    def __init__(
        self,
        create_on_client: bool = ...,
        classes: _Optional[
            _Iterable[_Union[CSVCMsg_ClassInfo.class_t, _Mapping]]
        ] = ...,
    ) -> None: ...

class CSVCMsg_ClearAllStringTables(_message.Message):
    __slots__ = ["create_tables_skipped", "mapname"]
    CREATE_TABLES_SKIPPED_FIELD_NUMBER: _ClassVar[int]
    MAPNAME_FIELD_NUMBER: _ClassVar[int]
    create_tables_skipped: bool
    mapname: str
    def __init__(
        self, mapname: _Optional[str] = ..., create_tables_skipped: bool = ...
    ) -> None: ...

class CSVCMsg_CmdKeyValues(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class CSVCMsg_CreateStringTable(_message.Message):
    __slots__ = [
        "data_compressed",
        "flags",
        "name",
        "num_entries",
        "string_data",
        "uncompressed_size",
        "user_data_fixed_size",
        "user_data_size",
        "user_data_size_bits",
        "using_varint_bitcounts",
    ]
    DATA_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    STRING_DATA_FIELD_NUMBER: _ClassVar[int]
    UNCOMPRESSED_SIZE_FIELD_NUMBER: _ClassVar[int]
    USER_DATA_FIXED_SIZE_FIELD_NUMBER: _ClassVar[int]
    USER_DATA_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    USER_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    USING_VARINT_BITCOUNTS_FIELD_NUMBER: _ClassVar[int]
    data_compressed: bool
    flags: int
    name: str
    num_entries: int
    string_data: bytes
    uncompressed_size: int
    user_data_fixed_size: bool
    user_data_size: int
    user_data_size_bits: int
    using_varint_bitcounts: bool
    def __init__(
        self,
        name: _Optional[str] = ...,
        num_entries: _Optional[int] = ...,
        user_data_fixed_size: bool = ...,
        user_data_size: _Optional[int] = ...,
        user_data_size_bits: _Optional[int] = ...,
        flags: _Optional[int] = ...,
        string_data: _Optional[bytes] = ...,
        uncompressed_size: _Optional[int] = ...,
        data_compressed: bool = ...,
        using_varint_bitcounts: bool = ...,
    ) -> None: ...

class CSVCMsg_CrosshairAngle(_message.Message):
    __slots__ = ["angle"]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    angle: _networkbasetypes_pb2.CMsgQAngle
    def __init__(
        self, angle: _Optional[_Union[_networkbasetypes_pb2.CMsgQAngle, _Mapping]] = ...
    ) -> None: ...

class CSVCMsg_FixAngle(_message.Message):
    __slots__ = ["angle", "relative"]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_FIELD_NUMBER: _ClassVar[int]
    angle: _networkbasetypes_pb2.CMsgQAngle
    relative: bool
    def __init__(
        self,
        relative: bool = ...,
        angle: _Optional[_Union[_networkbasetypes_pb2.CMsgQAngle, _Mapping]] = ...,
    ) -> None: ...

class CSVCMsg_FlattenedSerializer(_message.Message):
    __slots__ = ["fields", "serializers", "symbols"]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    SERIALIZERS_FIELD_NUMBER: _ClassVar[int]
    SYMBOLS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[ProtoFlattenedSerializerField_t]
    serializers: _containers.RepeatedCompositeFieldContainer[ProtoFlattenedSerializer_t]
    symbols: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        serializers: _Optional[
            _Iterable[_Union[ProtoFlattenedSerializer_t, _Mapping]]
        ] = ...,
        symbols: _Optional[_Iterable[str]] = ...,
        fields: _Optional[
            _Iterable[_Union[ProtoFlattenedSerializerField_t, _Mapping]]
        ] = ...,
    ) -> None: ...

class CSVCMsg_FullFrameSplit(_message.Message):
    __slots__ = ["data", "section", "tick", "total"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SECTION_FIELD_NUMBER: _ClassVar[int]
    TICK_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    section: int
    tick: int
    total: int
    def __init__(
        self,
        tick: _Optional[int] = ...,
        section: _Optional[int] = ...,
        total: _Optional[int] = ...,
        data: _Optional[bytes] = ...,
    ) -> None: ...

class CSVCMsg_GameEventList(_message.Message):
    __slots__ = ["descriptors"]

    class descriptor_t(_message.Message):
        __slots__ = ["eventid", "keys", "name"]
        EVENTID_FIELD_NUMBER: _ClassVar[int]
        KEYS_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        eventid: int
        keys: _containers.RepeatedCompositeFieldContainer[CSVCMsg_GameEventList.key_t]
        name: str
        def __init__(
            self,
            eventid: _Optional[int] = ...,
            name: _Optional[str] = ...,
            keys: _Optional[
                _Iterable[_Union[CSVCMsg_GameEventList.key_t, _Mapping]]
            ] = ...,
        ) -> None: ...

    class key_t(_message.Message):
        __slots__ = ["name", "type"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: int
        def __init__(
            self, type: _Optional[int] = ..., name: _Optional[str] = ...
        ) -> None: ...

    DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    descriptors: _containers.RepeatedCompositeFieldContainer[
        CSVCMsg_GameEventList.descriptor_t
    ]
    def __init__(
        self,
        descriptors: _Optional[
            _Iterable[_Union[CSVCMsg_GameEventList.descriptor_t, _Mapping]]
        ] = ...,
    ) -> None: ...

class CSVCMsg_GetCvarValue(_message.Message):
    __slots__ = ["cookie", "cvar_name"]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    CVAR_NAME_FIELD_NUMBER: _ClassVar[int]
    cookie: int
    cvar_name: str
    def __init__(
        self, cookie: _Optional[int] = ..., cvar_name: _Optional[str] = ...
    ) -> None: ...

class CSVCMsg_HLTVStatus(_message.Message):
    __slots__ = ["clients", "master", "proxies", "slots"]
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    MASTER_FIELD_NUMBER: _ClassVar[int]
    PROXIES_FIELD_NUMBER: _ClassVar[int]
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    clients: int
    master: str
    proxies: int
    slots: int
    def __init__(
        self,
        master: _Optional[str] = ...,
        clients: _Optional[int] = ...,
        slots: _Optional[int] = ...,
        proxies: _Optional[int] = ...,
    ) -> None: ...

class CSVCMsg_HltvFixupOperatorStatus(_message.Message):
    __slots__ = ["mode", "override_operator_name"]
    MODE_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_OPERATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    mode: int
    override_operator_name: str
    def __init__(
        self, mode: _Optional[int] = ..., override_operator_name: _Optional[str] = ...
    ) -> None: ...

class CSVCMsg_HltvReplay(_message.Message):
    __slots__ = [
        "delay",
        "primary_target",
        "reason",
        "replay_slowdown_begin",
        "replay_slowdown_end",
        "replay_slowdown_rate",
        "replay_start_at",
        "replay_stop_at",
    ]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_TARGET_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    REPLAY_SLOWDOWN_BEGIN_FIELD_NUMBER: _ClassVar[int]
    REPLAY_SLOWDOWN_END_FIELD_NUMBER: _ClassVar[int]
    REPLAY_SLOWDOWN_RATE_FIELD_NUMBER: _ClassVar[int]
    REPLAY_START_AT_FIELD_NUMBER: _ClassVar[int]
    REPLAY_STOP_AT_FIELD_NUMBER: _ClassVar[int]
    delay: int
    primary_target: int
    reason: int
    replay_slowdown_begin: int
    replay_slowdown_end: int
    replay_slowdown_rate: float
    replay_start_at: int
    replay_stop_at: int
    def __init__(
        self,
        delay: _Optional[int] = ...,
        primary_target: _Optional[int] = ...,
        replay_stop_at: _Optional[int] = ...,
        replay_start_at: _Optional[int] = ...,
        replay_slowdown_begin: _Optional[int] = ...,
        replay_slowdown_end: _Optional[int] = ...,
        replay_slowdown_rate: _Optional[float] = ...,
        reason: _Optional[int] = ...,
    ) -> None: ...

class CSVCMsg_Menu(_message.Message):
    __slots__ = ["dialog_type", "menu_key_values"]
    DIALOG_TYPE_FIELD_NUMBER: _ClassVar[int]
    MENU_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    dialog_type: int
    menu_key_values: bytes
    def __init__(
        self, dialog_type: _Optional[int] = ..., menu_key_values: _Optional[bytes] = ...
    ) -> None: ...

class CSVCMsg_PacketEntities(_message.Message):
    __slots__ = [
        "active_spawngroup_handle",
        "alternate_baselines",
        "baseline",
        "cmd_recv_status",
        "cq_discarded_command_ticks",
        "cq_starved_command_ticks",
        "delta_from",
        "dev_padding",
        "entity_data",
        "has_pvs_vis_bits",
        "last_cmd_number_executed",
        "last_cmd_number_recv_delta",
        "legacy_is_delta",
        "max_entries",
        "max_spawngroup_creationsequence",
        "non_transmitted_entities",
        "pending_full_frame",
        "serialized_entities",
        "server_tick",
        "update_baseline",
        "updated_entries",
    ]

    class alternate_baseline_t(_message.Message):
        __slots__ = ["baseline_index", "entity_index"]
        BASELINE_INDEX_FIELD_NUMBER: _ClassVar[int]
        ENTITY_INDEX_FIELD_NUMBER: _ClassVar[int]
        baseline_index: int
        entity_index: int
        def __init__(
            self,
            entity_index: _Optional[int] = ...,
            baseline_index: _Optional[int] = ...,
        ) -> None: ...

    class non_transmitted_entities_t(_message.Message):
        __slots__ = ["data", "header_count"]
        DATA_FIELD_NUMBER: _ClassVar[int]
        HEADER_COUNT_FIELD_NUMBER: _ClassVar[int]
        data: bytes
        header_count: int
        def __init__(
            self, header_count: _Optional[int] = ..., data: _Optional[bytes] = ...
        ) -> None: ...

    ACTIVE_SPAWNGROUP_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_BASELINES_FIELD_NUMBER: _ClassVar[int]
    BASELINE_FIELD_NUMBER: _ClassVar[int]
    CMD_RECV_STATUS_FIELD_NUMBER: _ClassVar[int]
    CQ_DISCARDED_COMMAND_TICKS_FIELD_NUMBER: _ClassVar[int]
    CQ_STARVED_COMMAND_TICKS_FIELD_NUMBER: _ClassVar[int]
    DELTA_FROM_FIELD_NUMBER: _ClassVar[int]
    DEV_PADDING_FIELD_NUMBER: _ClassVar[int]
    ENTITY_DATA_FIELD_NUMBER: _ClassVar[int]
    HAS_PVS_VIS_BITS_FIELD_NUMBER: _ClassVar[int]
    LAST_CMD_NUMBER_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    LAST_CMD_NUMBER_RECV_DELTA_FIELD_NUMBER: _ClassVar[int]
    LEGACY_IS_DELTA_FIELD_NUMBER: _ClassVar[int]
    MAX_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    MAX_SPAWNGROUP_CREATIONSEQUENCE_FIELD_NUMBER: _ClassVar[int]
    NON_TRANSMITTED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    PENDING_FULL_FRAME_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    SERVER_TICK_FIELD_NUMBER: _ClassVar[int]
    UPDATED_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    UPDATE_BASELINE_FIELD_NUMBER: _ClassVar[int]
    active_spawngroup_handle: int
    alternate_baselines: _containers.RepeatedCompositeFieldContainer[
        CSVCMsg_PacketEntities.alternate_baseline_t
    ]
    baseline: int
    cmd_recv_status: _containers.RepeatedScalarFieldContainer[int]
    cq_discarded_command_ticks: int
    cq_starved_command_ticks: int
    delta_from: int
    dev_padding: bytes
    entity_data: bytes
    has_pvs_vis_bits: int
    last_cmd_number_executed: int
    last_cmd_number_recv_delta: int
    legacy_is_delta: bool
    max_entries: int
    max_spawngroup_creationsequence: int
    non_transmitted_entities: CSVCMsg_PacketEntities.non_transmitted_entities_t
    pending_full_frame: bool
    serialized_entities: bytes
    server_tick: int
    update_baseline: bool
    updated_entries: int
    def __init__(
        self,
        max_entries: _Optional[int] = ...,
        updated_entries: _Optional[int] = ...,
        legacy_is_delta: bool = ...,
        update_baseline: bool = ...,
        baseline: _Optional[int] = ...,
        delta_from: _Optional[int] = ...,
        entity_data: _Optional[bytes] = ...,
        pending_full_frame: bool = ...,
        active_spawngroup_handle: _Optional[int] = ...,
        max_spawngroup_creationsequence: _Optional[int] = ...,
        last_cmd_number_executed: _Optional[int] = ...,
        last_cmd_number_recv_delta: _Optional[int] = ...,
        server_tick: _Optional[int] = ...,
        serialized_entities: _Optional[bytes] = ...,
        alternate_baselines: _Optional[
            _Iterable[_Union[CSVCMsg_PacketEntities.alternate_baseline_t, _Mapping]]
        ] = ...,
        has_pvs_vis_bits: _Optional[int] = ...,
        cmd_recv_status: _Optional[_Iterable[int]] = ...,
        non_transmitted_entities: _Optional[
            _Union[CSVCMsg_PacketEntities.non_transmitted_entities_t, _Mapping]
        ] = ...,
        cq_starved_command_ticks: _Optional[int] = ...,
        cq_discarded_command_ticks: _Optional[int] = ...,
        dev_padding: _Optional[bytes] = ...,
    ) -> None: ...

class CSVCMsg_PacketReliable(_message.Message):
    __slots__ = ["messagessize", "state", "tick"]
    MESSAGESSIZE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TICK_FIELD_NUMBER: _ClassVar[int]
    messagessize: int
    state: bool
    tick: int
    def __init__(
        self,
        tick: _Optional[int] = ...,
        messagessize: _Optional[int] = ...,
        state: bool = ...,
    ) -> None: ...

class CSVCMsg_PeerList(_message.Message):
    __slots__ = ["peer"]
    PEER_FIELD_NUMBER: _ClassVar[int]
    peer: _containers.RepeatedCompositeFieldContainer[CMsgServerPeer]
    def __init__(
        self, peer: _Optional[_Iterable[_Union[CMsgServerPeer, _Mapping]]] = ...
    ) -> None: ...

class CSVCMsg_Prefetch(_message.Message):
    __slots__ = ["resource_type", "sound_index"]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOUND_INDEX_FIELD_NUMBER: _ClassVar[int]
    resource_type: PrefetchType
    sound_index: int
    def __init__(
        self,
        sound_index: _Optional[int] = ...,
        resource_type: _Optional[_Union[PrefetchType, str]] = ...,
    ) -> None: ...

class CSVCMsg_Print(_message.Message):
    __slots__ = ["text"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class CSVCMsg_RconServerDetails(_message.Message):
    __slots__ = ["details", "token"]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    details: str
    token: bytes
    def __init__(
        self, token: _Optional[bytes] = ..., details: _Optional[str] = ...
    ) -> None: ...

class CSVCMsg_SendTable(_message.Message):
    __slots__ = ["is_end", "needs_decoder", "net_table_name", "props"]

    class sendprop_t(_message.Message):
        __slots__ = [
            "dt_name",
            "flags",
            "high_value",
            "low_value",
            "num_bits",
            "num_elements",
            "priority",
            "type",
            "var_name",
        ]
        DT_NAME_FIELD_NUMBER: _ClassVar[int]
        FLAGS_FIELD_NUMBER: _ClassVar[int]
        HIGH_VALUE_FIELD_NUMBER: _ClassVar[int]
        LOW_VALUE_FIELD_NUMBER: _ClassVar[int]
        NUM_BITS_FIELD_NUMBER: _ClassVar[int]
        NUM_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VAR_NAME_FIELD_NUMBER: _ClassVar[int]
        dt_name: str
        flags: int
        high_value: float
        low_value: float
        num_bits: int
        num_elements: int
        priority: int
        type: int
        var_name: str
        def __init__(
            self,
            type: _Optional[int] = ...,
            var_name: _Optional[str] = ...,
            flags: _Optional[int] = ...,
            priority: _Optional[int] = ...,
            dt_name: _Optional[str] = ...,
            num_elements: _Optional[int] = ...,
            low_value: _Optional[float] = ...,
            high_value: _Optional[float] = ...,
            num_bits: _Optional[int] = ...,
        ) -> None: ...

    IS_END_FIELD_NUMBER: _ClassVar[int]
    NEEDS_DECODER_FIELD_NUMBER: _ClassVar[int]
    NET_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PROPS_FIELD_NUMBER: _ClassVar[int]
    is_end: bool
    needs_decoder: bool
    net_table_name: str
    props: _containers.RepeatedCompositeFieldContainer[CSVCMsg_SendTable.sendprop_t]
    def __init__(
        self,
        is_end: bool = ...,
        net_table_name: _Optional[str] = ...,
        needs_decoder: bool = ...,
        props: _Optional[
            _Iterable[_Union[CSVCMsg_SendTable.sendprop_t, _Mapping]]
        ] = ...,
    ) -> None: ...

class CSVCMsg_ServerInfo(_message.Message):
    __slots__ = [
        "addon_name",
        "c_os",
        "game_dir",
        "game_session_config",
        "game_session_manifest",
        "host_name",
        "is_dedicated",
        "is_hltv",
        "map_name",
        "max_classes",
        "max_clients",
        "player_slot",
        "protocol",
        "server_count",
        "sky_name",
        "tick_interval",
    ]
    ADDON_NAME_FIELD_NUMBER: _ClassVar[int]
    C_OS_FIELD_NUMBER: _ClassVar[int]
    GAME_DIR_FIELD_NUMBER: _ClassVar[int]
    GAME_SESSION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GAME_SESSION_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_DEDICATED_FIELD_NUMBER: _ClassVar[int]
    IS_HLTV_FIELD_NUMBER: _ClassVar[int]
    MAP_NAME_FIELD_NUMBER: _ClassVar[int]
    MAX_CLASSES_FIELD_NUMBER: _ClassVar[int]
    MAX_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SLOT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    SERVER_COUNT_FIELD_NUMBER: _ClassVar[int]
    SKY_NAME_FIELD_NUMBER: _ClassVar[int]
    TICK_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    addon_name: str
    c_os: int
    game_dir: str
    game_session_config: _networkbasetypes_pb2.CSVCMsg_GameSessionConfiguration
    game_session_manifest: bytes
    host_name: str
    is_dedicated: bool
    is_hltv: bool
    map_name: str
    max_classes: int
    max_clients: int
    player_slot: int
    protocol: int
    server_count: int
    sky_name: str
    tick_interval: float
    def __init__(
        self,
        protocol: _Optional[int] = ...,
        server_count: _Optional[int] = ...,
        is_dedicated: bool = ...,
        is_hltv: bool = ...,
        c_os: _Optional[int] = ...,
        max_clients: _Optional[int] = ...,
        max_classes: _Optional[int] = ...,
        player_slot: _Optional[int] = ...,
        tick_interval: _Optional[float] = ...,
        game_dir: _Optional[str] = ...,
        map_name: _Optional[str] = ...,
        sky_name: _Optional[str] = ...,
        host_name: _Optional[str] = ...,
        addon_name: _Optional[str] = ...,
        game_session_config: _Optional[
            _Union[_networkbasetypes_pb2.CSVCMsg_GameSessionConfiguration, _Mapping]
        ] = ...,
        game_session_manifest: _Optional[bytes] = ...,
    ) -> None: ...

class CSVCMsg_ServerSteamID(_message.Message):
    __slots__ = ["steam_id"]
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    steam_id: int
    def __init__(self, steam_id: _Optional[int] = ...) -> None: ...

class CSVCMsg_SetPause(_message.Message):
    __slots__ = ["paused"]
    PAUSED_FIELD_NUMBER: _ClassVar[int]
    paused: bool
    def __init__(self, paused: bool = ...) -> None: ...

class CSVCMsg_SetView(_message.Message):
    __slots__ = ["entity_index", "slot"]
    ENTITY_INDEX_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    entity_index: int
    slot: int
    def __init__(
        self, entity_index: _Optional[int] = ..., slot: _Optional[int] = ...
    ) -> None: ...

class CSVCMsg_Sounds(_message.Message):
    __slots__ = ["reliable_sound", "sounds"]

    class sounddata_t(_message.Message):
        __slots__ = [
            "channel",
            "delay_value",
            "entity_index",
            "flags",
            "guid",
            "is_ambient",
            "is_sentence",
            "origin_x",
            "origin_y",
            "origin_z",
            "pitch",
            "random_seed",
            "sequence_number",
            "sound_level",
            "sound_num",
            "sound_num_handle",
            "sound_resource_id",
            "speaker_entity",
            "volume",
        ]
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        DELAY_VALUE_FIELD_NUMBER: _ClassVar[int]
        ENTITY_INDEX_FIELD_NUMBER: _ClassVar[int]
        FLAGS_FIELD_NUMBER: _ClassVar[int]
        GUID_FIELD_NUMBER: _ClassVar[int]
        IS_AMBIENT_FIELD_NUMBER: _ClassVar[int]
        IS_SENTENCE_FIELD_NUMBER: _ClassVar[int]
        ORIGIN_X_FIELD_NUMBER: _ClassVar[int]
        ORIGIN_Y_FIELD_NUMBER: _ClassVar[int]
        ORIGIN_Z_FIELD_NUMBER: _ClassVar[int]
        PITCH_FIELD_NUMBER: _ClassVar[int]
        RANDOM_SEED_FIELD_NUMBER: _ClassVar[int]
        SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        SOUND_LEVEL_FIELD_NUMBER: _ClassVar[int]
        SOUND_NUM_FIELD_NUMBER: _ClassVar[int]
        SOUND_NUM_HANDLE_FIELD_NUMBER: _ClassVar[int]
        SOUND_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        SPEAKER_ENTITY_FIELD_NUMBER: _ClassVar[int]
        VOLUME_FIELD_NUMBER: _ClassVar[int]
        channel: int
        delay_value: float
        entity_index: int
        flags: int
        guid: int
        is_ambient: bool
        is_sentence: bool
        origin_x: int
        origin_y: int
        origin_z: int
        pitch: int
        random_seed: int
        sequence_number: int
        sound_level: int
        sound_num: int
        sound_num_handle: int
        sound_resource_id: int
        speaker_entity: int
        volume: int
        def __init__(
            self,
            origin_x: _Optional[int] = ...,
            origin_y: _Optional[int] = ...,
            origin_z: _Optional[int] = ...,
            volume: _Optional[int] = ...,
            delay_value: _Optional[float] = ...,
            sequence_number: _Optional[int] = ...,
            entity_index: _Optional[int] = ...,
            channel: _Optional[int] = ...,
            pitch: _Optional[int] = ...,
            flags: _Optional[int] = ...,
            sound_num: _Optional[int] = ...,
            sound_num_handle: _Optional[int] = ...,
            speaker_entity: _Optional[int] = ...,
            random_seed: _Optional[int] = ...,
            sound_level: _Optional[int] = ...,
            is_sentence: bool = ...,
            is_ambient: bool = ...,
            guid: _Optional[int] = ...,
            sound_resource_id: _Optional[int] = ...,
        ) -> None: ...

    RELIABLE_SOUND_FIELD_NUMBER: _ClassVar[int]
    SOUNDS_FIELD_NUMBER: _ClassVar[int]
    reliable_sound: bool
    sounds: _containers.RepeatedCompositeFieldContainer[CSVCMsg_Sounds.sounddata_t]
    def __init__(
        self,
        reliable_sound: bool = ...,
        sounds: _Optional[
            _Iterable[_Union[CSVCMsg_Sounds.sounddata_t, _Mapping]]
        ] = ...,
    ) -> None: ...

class CSVCMsg_SplitScreen(_message.Message):
    __slots__ = ["player_index", "slot", "type"]
    PLAYER_INDEX_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    player_index: int
    slot: int
    type: ESplitScreenMessageType
    def __init__(
        self,
        type: _Optional[_Union[ESplitScreenMessageType, str]] = ...,
        slot: _Optional[int] = ...,
        player_index: _Optional[int] = ...,
    ) -> None: ...

class CSVCMsg_StopSound(_message.Message):
    __slots__ = ["guid"]
    GUID_FIELD_NUMBER: _ClassVar[int]
    guid: int
    def __init__(self, guid: _Optional[int] = ...) -> None: ...

class CSVCMsg_TempEntities(_message.Message):
    __slots__ = ["entity_data", "num_entries", "reliable"]
    ENTITY_DATA_FIELD_NUMBER: _ClassVar[int]
    NUM_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    RELIABLE_FIELD_NUMBER: _ClassVar[int]
    entity_data: bytes
    num_entries: int
    reliable: bool
    def __init__(
        self,
        reliable: bool = ...,
        num_entries: _Optional[int] = ...,
        entity_data: _Optional[bytes] = ...,
    ) -> None: ...

class CSVCMsg_UpdateStringTable(_message.Message):
    __slots__ = ["num_changed_entries", "string_data", "table_id"]
    NUM_CHANGED_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    STRING_DATA_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    num_changed_entries: int
    string_data: bytes
    table_id: int
    def __init__(
        self,
        table_id: _Optional[int] = ...,
        num_changed_entries: _Optional[int] = ...,
        string_data: _Optional[bytes] = ...,
    ) -> None: ...

class CSVCMsg_UserCommands(_message.Message):
    __slots__ = ["commands"]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    commands: _containers.RepeatedCompositeFieldContainer[CMsgServerUserCmd]
    def __init__(
        self, commands: _Optional[_Iterable[_Union[CMsgServerUserCmd, _Mapping]]] = ...
    ) -> None: ...

class CSVCMsg_UserMessage(_message.Message):
    __slots__ = ["msg_data", "msg_type", "passthrough"]
    MSG_DATA_FIELD_NUMBER: _ClassVar[int]
    MSG_TYPE_FIELD_NUMBER: _ClassVar[int]
    PASSTHROUGH_FIELD_NUMBER: _ClassVar[int]
    msg_data: bytes
    msg_type: int
    passthrough: int
    def __init__(
        self,
        msg_type: _Optional[int] = ...,
        msg_data: _Optional[bytes] = ...,
        passthrough: _Optional[int] = ...,
    ) -> None: ...

class CSVCMsg_VoiceData(_message.Message):
    __slots__ = [
        "audible_mask",
        "audio",
        "client",
        "passthrough",
        "proximity",
        "tick",
        "xuid",
    ]
    AUDIBLE_MASK_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    PASSTHROUGH_FIELD_NUMBER: _ClassVar[int]
    PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    TICK_FIELD_NUMBER: _ClassVar[int]
    XUID_FIELD_NUMBER: _ClassVar[int]
    audible_mask: int
    audio: CMsgVoiceAudio
    client: int
    passthrough: int
    proximity: bool
    tick: int
    xuid: int
    def __init__(
        self,
        audio: _Optional[_Union[CMsgVoiceAudio, _Mapping]] = ...,
        client: _Optional[int] = ...,
        proximity: bool = ...,
        xuid: _Optional[int] = ...,
        audible_mask: _Optional[int] = ...,
        tick: _Optional[int] = ...,
        passthrough: _Optional[int] = ...,
    ) -> None: ...

class CSVCMsg_VoiceInit(_message.Message):
    __slots__ = ["codec", "quality", "version"]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    codec: str
    quality: int
    version: int
    def __init__(
        self,
        quality: _Optional[int] = ...,
        codec: _Optional[str] = ...,
        version: _Optional[int] = ...,
    ) -> None: ...

class CSource2Metrics_MatchPerfSummary_Notification(_message.Message):
    __slots__ = [
        "appid",
        "clients",
        "game_mode",
        "map",
        "server_build_id",
        "server_profile",
    ]

    class Client(_message.Message):
        __slots__ = ["build_id", "profile", "steamid", "system_specs"]
        BUILD_ID_FIELD_NUMBER: _ClassVar[int]
        PROFILE_FIELD_NUMBER: _ClassVar[int]
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        SYSTEM_SPECS_FIELD_NUMBER: _ClassVar[int]
        build_id: int
        profile: CMsgSource2VProfLiteReport
        steamid: int
        system_specs: CMsgSource2SystemSpecs
        def __init__(
            self,
            system_specs: _Optional[_Union[CMsgSource2SystemSpecs, _Mapping]] = ...,
            profile: _Optional[_Union[CMsgSource2VProfLiteReport, _Mapping]] = ...,
            build_id: _Optional[int] = ...,
            steamid: _Optional[int] = ...,
        ) -> None: ...

    APPID_FIELD_NUMBER: _ClassVar[int]
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    GAME_MODE_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    SERVER_BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_PROFILE_FIELD_NUMBER: _ClassVar[int]
    appid: int
    clients: _containers.RepeatedCompositeFieldContainer[
        CSource2Metrics_MatchPerfSummary_Notification.Client
    ]
    game_mode: str
    map: str
    server_build_id: int
    server_profile: CMsgSource2VProfLiteReport
    def __init__(
        self,
        appid: _Optional[int] = ...,
        game_mode: _Optional[str] = ...,
        server_build_id: _Optional[int] = ...,
        server_profile: _Optional[_Union[CMsgSource2VProfLiteReport, _Mapping]] = ...,
        clients: _Optional[
            _Iterable[
                _Union[CSource2Metrics_MatchPerfSummary_Notification.Client, _Mapping]
            ]
        ] = ...,
        map: _Optional[str] = ...,
    ) -> None: ...

class ProtoFlattenedSerializerField_t(_message.Message):
    __slots__ = [
        "bit_count",
        "encode_flags",
        "field_serializer_name_sym",
        "field_serializer_version",
        "high_value",
        "low_value",
        "polymorphic_types",
        "send_node_sym",
        "var_encoder_sym",
        "var_name_sym",
        "var_serializer_sym",
        "var_type_sym",
    ]

    class polymorphic_field_t(_message.Message):
        __slots__ = [
            "polymorphic_field_serializer_name_sym",
            "polymorphic_field_serializer_version",
        ]
        POLYMORPHIC_FIELD_SERIALIZER_NAME_SYM_FIELD_NUMBER: _ClassVar[int]
        POLYMORPHIC_FIELD_SERIALIZER_VERSION_FIELD_NUMBER: _ClassVar[int]
        polymorphic_field_serializer_name_sym: int
        polymorphic_field_serializer_version: int
        def __init__(
            self,
            polymorphic_field_serializer_name_sym: _Optional[int] = ...,
            polymorphic_field_serializer_version: _Optional[int] = ...,
        ) -> None: ...

    BIT_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENCODE_FLAGS_FIELD_NUMBER: _ClassVar[int]
    FIELD_SERIALIZER_NAME_SYM_FIELD_NUMBER: _ClassVar[int]
    FIELD_SERIALIZER_VERSION_FIELD_NUMBER: _ClassVar[int]
    HIGH_VALUE_FIELD_NUMBER: _ClassVar[int]
    LOW_VALUE_FIELD_NUMBER: _ClassVar[int]
    POLYMORPHIC_TYPES_FIELD_NUMBER: _ClassVar[int]
    SEND_NODE_SYM_FIELD_NUMBER: _ClassVar[int]
    VAR_ENCODER_SYM_FIELD_NUMBER: _ClassVar[int]
    VAR_NAME_SYM_FIELD_NUMBER: _ClassVar[int]
    VAR_SERIALIZER_SYM_FIELD_NUMBER: _ClassVar[int]
    VAR_TYPE_SYM_FIELD_NUMBER: _ClassVar[int]
    bit_count: int
    encode_flags: int
    field_serializer_name_sym: int
    field_serializer_version: int
    high_value: float
    low_value: float
    polymorphic_types: _containers.RepeatedCompositeFieldContainer[
        ProtoFlattenedSerializerField_t.polymorphic_field_t
    ]
    send_node_sym: int
    var_encoder_sym: int
    var_name_sym: int
    var_serializer_sym: int
    var_type_sym: int
    def __init__(
        self,
        var_type_sym: _Optional[int] = ...,
        var_name_sym: _Optional[int] = ...,
        bit_count: _Optional[int] = ...,
        low_value: _Optional[float] = ...,
        high_value: _Optional[float] = ...,
        encode_flags: _Optional[int] = ...,
        field_serializer_name_sym: _Optional[int] = ...,
        field_serializer_version: _Optional[int] = ...,
        send_node_sym: _Optional[int] = ...,
        var_encoder_sym: _Optional[int] = ...,
        polymorphic_types: _Optional[
            _Iterable[
                _Union[ProtoFlattenedSerializerField_t.polymorphic_field_t, _Mapping]
            ]
        ] = ...,
        var_serializer_sym: _Optional[int] = ...,
    ) -> None: ...

class ProtoFlattenedSerializer_t(_message.Message):
    __slots__ = ["fields_index", "serializer_name_sym", "serializer_version"]
    FIELDS_INDEX_FIELD_NUMBER: _ClassVar[int]
    SERIALIZER_NAME_SYM_FIELD_NUMBER: _ClassVar[int]
    SERIALIZER_VERSION_FIELD_NUMBER: _ClassVar[int]
    fields_index: _containers.RepeatedScalarFieldContainer[int]
    serializer_name_sym: int
    serializer_version: int
    def __init__(
        self,
        serializer_name_sym: _Optional[int] = ...,
        serializer_version: _Optional[int] = ...,
        fields_index: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class CLC_Messages(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SVC_Messages(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class VoiceDataFormat_t(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class RequestPause_t(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class PrefetchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ESplitScreenMessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EQueryCvarValueStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class DIALOG_TYPE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SVC_Messages_LowFrequency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Bidirectional_Messages(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Bidirectional_Messages_LowFrequency(
    int, metaclass=_enum_type_wrapper.EnumTypeWrapper
):
    __slots__ = []

class ReplayEventType_t(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
