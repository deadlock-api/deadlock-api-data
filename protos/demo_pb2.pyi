from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DEM_AnimationData: EDemoCommands
DEM_AnimationHeader: EDemoCommands
DEM_ClassInfo: EDemoCommands
DEM_ConsoleCmd: EDemoCommands
DEM_CustomData: EDemoCommands
DEM_CustomDataCallbacks: EDemoCommands
DEM_Error: EDemoCommands
DEM_FileHeader: EDemoCommands
DEM_FileInfo: EDemoCommands
DEM_FullPacket: EDemoCommands
DEM_IsCompressed: EDemoCommands
DEM_Max: EDemoCommands
DEM_Packet: EDemoCommands
DEM_SaveGame: EDemoCommands
DEM_SendTables: EDemoCommands
DEM_SignonPacket: EDemoCommands
DEM_SpawnGroups: EDemoCommands
DEM_Stop: EDemoCommands
DEM_StringTables: EDemoCommands
DEM_SyncTick: EDemoCommands
DEM_UserCmd: EDemoCommands
DESCRIPTOR: _descriptor.FileDescriptor

class CDemoAnimationData(_message.Message):
    __slots__ = ["data", "data_checksum", "end_tick", "entity_id", "start_tick"]
    DATA_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    END_TICK_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    START_TICK_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    data_checksum: int
    end_tick: int
    entity_id: int
    start_tick: int
    def __init__(
        self,
        entity_id: _Optional[int] = ...,
        start_tick: _Optional[int] = ...,
        end_tick: _Optional[int] = ...,
        data: _Optional[bytes] = ...,
        data_checksum: _Optional[int] = ...,
    ) -> None: ...

class CDemoAnimationHeader(_message.Message):
    __slots__ = ["data", "entity_id", "tick"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    TICK_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    entity_id: int
    tick: int
    def __init__(
        self,
        entity_id: _Optional[int] = ...,
        tick: _Optional[int] = ...,
        data: _Optional[bytes] = ...,
    ) -> None: ...

class CDemoClassInfo(_message.Message):
    __slots__ = ["classes"]

    class class_t(_message.Message):
        __slots__ = ["class_id", "network_name", "table_name"]
        CLASS_ID_FIELD_NUMBER: _ClassVar[int]
        NETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
        TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
        class_id: int
        network_name: str
        table_name: str
        def __init__(
            self,
            class_id: _Optional[int] = ...,
            network_name: _Optional[str] = ...,
            table_name: _Optional[str] = ...,
        ) -> None: ...

    CLASSES_FIELD_NUMBER: _ClassVar[int]
    classes: _containers.RepeatedCompositeFieldContainer[CDemoClassInfo.class_t]
    def __init__(
        self,
        classes: _Optional[_Iterable[_Union[CDemoClassInfo.class_t, _Mapping]]] = ...,
    ) -> None: ...

class CDemoConsoleCmd(_message.Message):
    __slots__ = ["cmdstring"]
    CMDSTRING_FIELD_NUMBER: _ClassVar[int]
    cmdstring: str
    def __init__(self, cmdstring: _Optional[str] = ...) -> None: ...

class CDemoCustomData(_message.Message):
    __slots__ = ["callback_index", "data"]
    CALLBACK_INDEX_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    callback_index: int
    data: bytes
    def __init__(
        self, callback_index: _Optional[int] = ..., data: _Optional[bytes] = ...
    ) -> None: ...

class CDemoCustomDataCallbacks(_message.Message):
    __slots__ = ["save_id"]
    SAVE_ID_FIELD_NUMBER: _ClassVar[int]
    save_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, save_id: _Optional[_Iterable[str]] = ...) -> None: ...

class CDemoFileHeader(_message.Message):
    __slots__ = [
        "addons",
        "allow_clientside_entities",
        "allow_clientside_particles",
        "build_num",
        "client_name",
        "demo_file_stamp",
        "demo_version_guid",
        "demo_version_name",
        "fullpackets_version",
        "game",
        "game_directory",
        "map_name",
        "network_protocol",
        "server_name",
        "server_start_tick",
    ]
    ADDONS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CLIENTSIDE_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CLIENTSIDE_PARTICLES_FIELD_NUMBER: _ClassVar[int]
    BUILD_NUM_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    DEMO_FILE_STAMP_FIELD_NUMBER: _ClassVar[int]
    DEMO_VERSION_GUID_FIELD_NUMBER: _ClassVar[int]
    DEMO_VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    FULLPACKETS_VERSION_FIELD_NUMBER: _ClassVar[int]
    GAME_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    GAME_FIELD_NUMBER: _ClassVar[int]
    MAP_NAME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVER_START_TICK_FIELD_NUMBER: _ClassVar[int]
    addons: str
    allow_clientside_entities: bool
    allow_clientside_particles: bool
    build_num: int
    client_name: str
    demo_file_stamp: str
    demo_version_guid: str
    demo_version_name: str
    fullpackets_version: int
    game: str
    game_directory: str
    map_name: str
    network_protocol: int
    server_name: str
    server_start_tick: int
    def __init__(
        self,
        demo_file_stamp: _Optional[str] = ...,
        network_protocol: _Optional[int] = ...,
        server_name: _Optional[str] = ...,
        client_name: _Optional[str] = ...,
        map_name: _Optional[str] = ...,
        game_directory: _Optional[str] = ...,
        fullpackets_version: _Optional[int] = ...,
        allow_clientside_entities: bool = ...,
        allow_clientside_particles: bool = ...,
        addons: _Optional[str] = ...,
        demo_version_name: _Optional[str] = ...,
        demo_version_guid: _Optional[str] = ...,
        build_num: _Optional[int] = ...,
        game: _Optional[str] = ...,
        server_start_tick: _Optional[int] = ...,
    ) -> None: ...

class CDemoFileInfo(_message.Message):
    __slots__ = ["game_info", "playback_frames", "playback_ticks", "playback_time"]
    GAME_INFO_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_FRAMES_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_TICKS_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_TIME_FIELD_NUMBER: _ClassVar[int]
    game_info: CGameInfo
    playback_frames: int
    playback_ticks: int
    playback_time: float
    def __init__(
        self,
        playback_time: _Optional[float] = ...,
        playback_ticks: _Optional[int] = ...,
        playback_frames: _Optional[int] = ...,
        game_info: _Optional[_Union[CGameInfo, _Mapping]] = ...,
    ) -> None: ...

class CDemoFullPacket(_message.Message):
    __slots__ = ["packet", "string_table"]
    PACKET_FIELD_NUMBER: _ClassVar[int]
    STRING_TABLE_FIELD_NUMBER: _ClassVar[int]
    packet: CDemoPacket
    string_table: CDemoStringTables
    def __init__(
        self,
        string_table: _Optional[_Union[CDemoStringTables, _Mapping]] = ...,
        packet: _Optional[_Union[CDemoPacket, _Mapping]] = ...,
    ) -> None: ...

class CDemoPacket(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class CDemoSaveGame(_message.Message):
    __slots__ = ["data", "signature", "steam_id", "version"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    signature: int
    steam_id: int
    version: int
    def __init__(
        self,
        data: _Optional[bytes] = ...,
        steam_id: _Optional[int] = ...,
        signature: _Optional[int] = ...,
        version: _Optional[int] = ...,
    ) -> None: ...

class CDemoSendTables(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class CDemoSpawnGroups(_message.Message):
    __slots__ = ["msgs"]
    MSGS_FIELD_NUMBER: _ClassVar[int]
    msgs: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, msgs: _Optional[_Iterable[bytes]] = ...) -> None: ...

class CDemoStop(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CDemoStringTables(_message.Message):
    __slots__ = ["tables"]

    class items_t(_message.Message):
        __slots__ = ["data", "str"]
        DATA_FIELD_NUMBER: _ClassVar[int]
        STR_FIELD_NUMBER: _ClassVar[int]
        data: bytes
        str: str
        def __init__(
            self, str: _Optional[str] = ..., data: _Optional[bytes] = ...
        ) -> None: ...

    class table_t(_message.Message):
        __slots__ = ["items", "items_clientside", "table_flags", "table_name"]
        ITEMS_CLIENTSIDE_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        TABLE_FLAGS_FIELD_NUMBER: _ClassVar[int]
        TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
        items: _containers.RepeatedCompositeFieldContainer[CDemoStringTables.items_t]
        items_clientside: _containers.RepeatedCompositeFieldContainer[
            CDemoStringTables.items_t
        ]
        table_flags: int
        table_name: str
        def __init__(
            self,
            table_name: _Optional[str] = ...,
            items: _Optional[
                _Iterable[_Union[CDemoStringTables.items_t, _Mapping]]
            ] = ...,
            items_clientside: _Optional[
                _Iterable[_Union[CDemoStringTables.items_t, _Mapping]]
            ] = ...,
            table_flags: _Optional[int] = ...,
        ) -> None: ...

    TABLES_FIELD_NUMBER: _ClassVar[int]
    tables: _containers.RepeatedCompositeFieldContainer[CDemoStringTables.table_t]
    def __init__(
        self,
        tables: _Optional[_Iterable[_Union[CDemoStringTables.table_t, _Mapping]]] = ...,
    ) -> None: ...

class CDemoSyncTick(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CDemoUserCmd(_message.Message):
    __slots__ = ["cmd_number", "data"]
    CMD_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    cmd_number: int
    data: bytes
    def __init__(
        self, cmd_number: _Optional[int] = ..., data: _Optional[bytes] = ...
    ) -> None: ...

class CGameInfo(_message.Message):
    __slots__ = ["cs", "dota"]

    class CCSGameInfo(_message.Message):
        __slots__ = ["round_start_ticks"]
        ROUND_START_TICKS_FIELD_NUMBER: _ClassVar[int]
        round_start_ticks: _containers.RepeatedScalarFieldContainer[int]
        def __init__(
            self, round_start_ticks: _Optional[_Iterable[int]] = ...
        ) -> None: ...

    class CDotaGameInfo(_message.Message):
        __slots__ = [
            "dire_team_id",
            "dire_team_tag",
            "end_time",
            "game_mode",
            "game_winner",
            "leagueid",
            "match_id",
            "picks_bans",
            "player_info",
            "radiant_team_id",
            "radiant_team_tag",
        ]

        class CHeroSelectEvent(_message.Message):
            __slots__ = ["hero_id", "is_pick", "team"]
            HERO_ID_FIELD_NUMBER: _ClassVar[int]
            IS_PICK_FIELD_NUMBER: _ClassVar[int]
            TEAM_FIELD_NUMBER: _ClassVar[int]
            hero_id: int
            is_pick: bool
            team: int
            def __init__(
                self,
                is_pick: bool = ...,
                team: _Optional[int] = ...,
                hero_id: _Optional[int] = ...,
            ) -> None: ...

        class CPlayerInfo(_message.Message):
            __slots__ = [
                "game_team",
                "hero_name",
                "is_fake_client",
                "player_name",
                "steamid",
            ]
            GAME_TEAM_FIELD_NUMBER: _ClassVar[int]
            HERO_NAME_FIELD_NUMBER: _ClassVar[int]
            IS_FAKE_CLIENT_FIELD_NUMBER: _ClassVar[int]
            PLAYER_NAME_FIELD_NUMBER: _ClassVar[int]
            STEAMID_FIELD_NUMBER: _ClassVar[int]
            game_team: int
            hero_name: str
            is_fake_client: bool
            player_name: str
            steamid: int
            def __init__(
                self,
                hero_name: _Optional[str] = ...,
                player_name: _Optional[str] = ...,
                is_fake_client: bool = ...,
                steamid: _Optional[int] = ...,
                game_team: _Optional[int] = ...,
            ) -> None: ...

        DIRE_TEAM_ID_FIELD_NUMBER: _ClassVar[int]
        DIRE_TEAM_TAG_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        GAME_MODE_FIELD_NUMBER: _ClassVar[int]
        GAME_WINNER_FIELD_NUMBER: _ClassVar[int]
        LEAGUEID_FIELD_NUMBER: _ClassVar[int]
        MATCH_ID_FIELD_NUMBER: _ClassVar[int]
        PICKS_BANS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_INFO_FIELD_NUMBER: _ClassVar[int]
        RADIANT_TEAM_ID_FIELD_NUMBER: _ClassVar[int]
        RADIANT_TEAM_TAG_FIELD_NUMBER: _ClassVar[int]
        dire_team_id: int
        dire_team_tag: str
        end_time: int
        game_mode: int
        game_winner: int
        leagueid: int
        match_id: int
        picks_bans: _containers.RepeatedCompositeFieldContainer[
            CGameInfo.CDotaGameInfo.CHeroSelectEvent
        ]
        player_info: _containers.RepeatedCompositeFieldContainer[
            CGameInfo.CDotaGameInfo.CPlayerInfo
        ]
        radiant_team_id: int
        radiant_team_tag: str
        def __init__(
            self,
            match_id: _Optional[int] = ...,
            game_mode: _Optional[int] = ...,
            game_winner: _Optional[int] = ...,
            player_info: _Optional[
                _Iterable[_Union[CGameInfo.CDotaGameInfo.CPlayerInfo, _Mapping]]
            ] = ...,
            leagueid: _Optional[int] = ...,
            picks_bans: _Optional[
                _Iterable[_Union[CGameInfo.CDotaGameInfo.CHeroSelectEvent, _Mapping]]
            ] = ...,
            radiant_team_id: _Optional[int] = ...,
            dire_team_id: _Optional[int] = ...,
            radiant_team_tag: _Optional[str] = ...,
            dire_team_tag: _Optional[str] = ...,
            end_time: _Optional[int] = ...,
        ) -> None: ...

    CS_FIELD_NUMBER: _ClassVar[int]
    DOTA_FIELD_NUMBER: _ClassVar[int]
    cs: CGameInfo.CCSGameInfo
    dota: CGameInfo.CDotaGameInfo
    def __init__(
        self,
        dota: _Optional[_Union[CGameInfo.CDotaGameInfo, _Mapping]] = ...,
        cs: _Optional[_Union[CGameInfo.CCSGameInfo, _Mapping]] = ...,
    ) -> None: ...

class EDemoCommands(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
