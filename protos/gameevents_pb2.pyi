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
GE_ClearDecalsForSkeletonInstanceEvent: EBaseGameEvents
GE_ClearEntityDecalsEvent: EBaseGameEvents
GE_ClearWorldDecalsEvent: EBaseGameEvents
GE_PlaceDecalEvent: EBaseGameEvents
GE_SosSetLibraryStackFields: EBaseGameEvents
GE_SosSetSoundEventParams: EBaseGameEvents
GE_SosStartSoundEvent: EBaseGameEvents
GE_SosStopSoundEvent: EBaseGameEvents
GE_SosStopSoundEventHash: EBaseGameEvents
GE_Source1LegacyGameEvent: EBaseGameEvents
GE_Source1LegacyGameEventList: EBaseGameEvents
GE_Source1LegacyListenEvents: EBaseGameEvents
GE_VDebugGameSessionIDEvent: EBaseGameEvents

class CMsgClearDecalsForSkeletonInstanceEvent(_message.Message):
    __slots__ = ["entityhandleindex", "flagstoclear", "skeletoninstancehash"]
    ENTITYHANDLEINDEX_FIELD_NUMBER: _ClassVar[int]
    FLAGSTOCLEAR_FIELD_NUMBER: _ClassVar[int]
    SKELETONINSTANCEHASH_FIELD_NUMBER: _ClassVar[int]
    entityhandleindex: int
    flagstoclear: int
    skeletoninstancehash: int
    def __init__(
        self,
        flagstoclear: _Optional[int] = ...,
        entityhandleindex: _Optional[int] = ...,
        skeletoninstancehash: _Optional[int] = ...,
    ) -> None: ...

class CMsgClearEntityDecalsEvent(_message.Message):
    __slots__ = ["flagstoclear"]
    FLAGSTOCLEAR_FIELD_NUMBER: _ClassVar[int]
    flagstoclear: int
    def __init__(self, flagstoclear: _Optional[int] = ...) -> None: ...

class CMsgClearWorldDecalsEvent(_message.Message):
    __slots__ = ["flagstoclear"]
    FLAGSTOCLEAR_FIELD_NUMBER: _ClassVar[int]
    flagstoclear: int
    def __init__(self, flagstoclear: _Optional[int] = ...) -> None: ...

class CMsgPlaceDecalEvent(_message.Message):
    __slots__ = [
        "boneindex",
        "color",
        "decalmaterialindex",
        "depth",
        "entityhandleindex",
        "flags",
        "height",
        "is_adjacent",
        "normal",
        "position",
        "saxis",
        "skeletoninstancehash",
        "translucenthit",
        "width",
    ]
    BONEINDEX_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    DECALMATERIALINDEX_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    ENTITYHANDLEINDEX_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    IS_ADJACENT_FIELD_NUMBER: _ClassVar[int]
    NORMAL_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    SAXIS_FIELD_NUMBER: _ClassVar[int]
    SKELETONINSTANCEHASH_FIELD_NUMBER: _ClassVar[int]
    TRANSLUCENTHIT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    boneindex: int
    color: int
    decalmaterialindex: int
    depth: float
    entityhandleindex: int
    flags: int
    height: float
    is_adjacent: bool
    normal: _networkbasetypes_pb2.CMsgVector
    position: _networkbasetypes_pb2.CMsgVector
    saxis: _networkbasetypes_pb2.CMsgVector
    skeletoninstancehash: int
    translucenthit: bool
    width: float
    def __init__(
        self,
        position: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...,
        normal: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...,
        saxis: _Optional[_Union[_networkbasetypes_pb2.CMsgVector, _Mapping]] = ...,
        decalmaterialindex: _Optional[int] = ...,
        flags: _Optional[int] = ...,
        color: _Optional[int] = ...,
        width: _Optional[float] = ...,
        height: _Optional[float] = ...,
        depth: _Optional[float] = ...,
        entityhandleindex: _Optional[int] = ...,
        skeletoninstancehash: _Optional[int] = ...,
        boneindex: _Optional[int] = ...,
        translucenthit: bool = ...,
        is_adjacent: bool = ...,
    ) -> None: ...

class CMsgSosSetLibraryStackFields(_message.Message):
    __slots__ = ["packed_fields", "stack_hash"]
    PACKED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    STACK_HASH_FIELD_NUMBER: _ClassVar[int]
    packed_fields: bytes
    stack_hash: int
    def __init__(
        self, stack_hash: _Optional[int] = ..., packed_fields: _Optional[bytes] = ...
    ) -> None: ...

class CMsgSosSetSoundEventParams(_message.Message):
    __slots__ = ["packed_params", "soundevent_guid"]
    PACKED_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SOUNDEVENT_GUID_FIELD_NUMBER: _ClassVar[int]
    packed_params: bytes
    soundevent_guid: int
    def __init__(
        self,
        soundevent_guid: _Optional[int] = ...,
        packed_params: _Optional[bytes] = ...,
    ) -> None: ...

class CMsgSosStartSoundEvent(_message.Message):
    __slots__ = [
        "packed_params",
        "seed",
        "soundevent_guid",
        "soundevent_hash",
        "source_entity_index",
        "start_time",
    ]
    PACKED_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    SOUNDEVENT_GUID_FIELD_NUMBER: _ClassVar[int]
    SOUNDEVENT_HASH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITY_INDEX_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    packed_params: bytes
    seed: int
    soundevent_guid: int
    soundevent_hash: int
    source_entity_index: int
    start_time: float
    def __init__(
        self,
        soundevent_guid: _Optional[int] = ...,
        soundevent_hash: _Optional[int] = ...,
        source_entity_index: _Optional[int] = ...,
        seed: _Optional[int] = ...,
        packed_params: _Optional[bytes] = ...,
        start_time: _Optional[float] = ...,
    ) -> None: ...

class CMsgSosStopSoundEvent(_message.Message):
    __slots__ = ["soundevent_guid"]
    SOUNDEVENT_GUID_FIELD_NUMBER: _ClassVar[int]
    soundevent_guid: int
    def __init__(self, soundevent_guid: _Optional[int] = ...) -> None: ...

class CMsgSosStopSoundEventHash(_message.Message):
    __slots__ = ["soundevent_hash", "source_entity_index"]
    SOUNDEVENT_HASH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITY_INDEX_FIELD_NUMBER: _ClassVar[int]
    soundevent_hash: int
    source_entity_index: int
    def __init__(
        self,
        soundevent_hash: _Optional[int] = ...,
        source_entity_index: _Optional[int] = ...,
    ) -> None: ...

class CMsgSource1LegacyGameEvent(_message.Message):
    __slots__ = ["event_name", "eventid", "keys", "passthrough", "server_tick"]

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
    PASSTHROUGH_FIELD_NUMBER: _ClassVar[int]
    SERVER_TICK_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    eventid: int
    keys: _containers.RepeatedCompositeFieldContainer[CMsgSource1LegacyGameEvent.key_t]
    passthrough: int
    server_tick: int
    def __init__(
        self,
        event_name: _Optional[str] = ...,
        eventid: _Optional[int] = ...,
        keys: _Optional[
            _Iterable[_Union[CMsgSource1LegacyGameEvent.key_t, _Mapping]]
        ] = ...,
        server_tick: _Optional[int] = ...,
        passthrough: _Optional[int] = ...,
    ) -> None: ...

class CMsgSource1LegacyGameEventList(_message.Message):
    __slots__ = ["descriptors"]

    class descriptor_t(_message.Message):
        __slots__ = ["eventid", "keys", "name"]
        EVENTID_FIELD_NUMBER: _ClassVar[int]
        KEYS_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        eventid: int
        keys: _containers.RepeatedCompositeFieldContainer[
            CMsgSource1LegacyGameEventList.key_t
        ]
        name: str
        def __init__(
            self,
            eventid: _Optional[int] = ...,
            name: _Optional[str] = ...,
            keys: _Optional[
                _Iterable[_Union[CMsgSource1LegacyGameEventList.key_t, _Mapping]]
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
        CMsgSource1LegacyGameEventList.descriptor_t
    ]
    def __init__(
        self,
        descriptors: _Optional[
            _Iterable[_Union[CMsgSource1LegacyGameEventList.descriptor_t, _Mapping]]
        ] = ...,
    ) -> None: ...

class CMsgSource1LegacyListenEvents(_message.Message):
    __slots__ = ["eventarraybits", "playerslot"]
    EVENTARRAYBITS_FIELD_NUMBER: _ClassVar[int]
    PLAYERSLOT_FIELD_NUMBER: _ClassVar[int]
    eventarraybits: _containers.RepeatedScalarFieldContainer[int]
    playerslot: int
    def __init__(
        self,
        playerslot: _Optional[int] = ...,
        eventarraybits: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class CMsgVDebugGameSessionIDEvent(_message.Message):
    __slots__ = ["clientid", "gamesessionid"]
    CLIENTID_FIELD_NUMBER: _ClassVar[int]
    GAMESESSIONID_FIELD_NUMBER: _ClassVar[int]
    clientid: int
    gamesessionid: str
    def __init__(
        self, clientid: _Optional[int] = ..., gamesessionid: _Optional[str] = ...
    ) -> None: ...

class EBaseGameEvents(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
