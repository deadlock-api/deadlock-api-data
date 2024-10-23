from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from steammessages_unified_base import steamworkssdk_pb2 as _steamworkssdk_pb2

DESCRIPTOR: _descriptor.FileDescriptor
STEAMLEARN_CACHE_DATA_DISABLED: ESteamLearnCacheDataResult
STEAMLEARN_CACHE_DATA_ERROR: ESteamLearnCacheDataResult
STEAMLEARN_CACHE_DATA_ERROR_FORBIDDEN: ESteamLearnCacheDataResult
STEAMLEARN_CACHE_DATA_ERROR_INVALID_KEYS: ESteamLearnCacheDataResult
STEAMLEARN_CACHE_DATA_ERROR_INVALID_TIMESTAMP: ESteamLearnCacheDataResult
STEAMLEARN_CACHE_DATA_ERROR_UNCACHED_DATA_SOURCE: ESteamLearnCacheDataResult
STEAMLEARN_CACHE_DATA_ERROR_UNKNOWN_DATA_SOURCE: ESteamLearnCacheDataResult
STEAMLEARN_CACHE_DATA_SUCCESS: ESteamLearnCacheDataResult
STEAMLEARN_DATATYPE_BOOL: ESteamLearnDataType
STEAMLEARN_DATATYPE_FLOAT32: ESteamLearnDataType
STEAMLEARN_DATATYPE_INT32: ESteamLearnDataType
STEAMLEARN_DATATYPE_INVALID: ESteamLearnDataType
STEAMLEARN_DATATYPE_OBJECT: ESteamLearnDataType
STEAMLEARN_DATATYPE_STRING: ESteamLearnDataType
STEAMLEARN_GET_ACCESS_TOKENS_ERROR: ESteamLearnGetAccessTokensResult
STEAMLEARN_GET_ACCESS_TOKENS_SUCCESS: ESteamLearnGetAccessTokensResult
STEAMLEARN_INFERENCE_ERROR: ESteamLearnInferenceResult
STEAMLEARN_INFERENCE_ERROR_FORBIDDEN: ESteamLearnInferenceResult
STEAMLEARN_INFERENCE_ERROR_INVALID_PROJECT_ID: ESteamLearnInferenceResult
STEAMLEARN_INFERENCE_ERROR_INVALID_PUBLISHED_VERSION: ESteamLearnInferenceResult
STEAMLEARN_INFERENCE_ERROR_INVALID_TIMESTAMP: ESteamLearnInferenceResult
STEAMLEARN_INFERENCE_ERROR_MISSING_CACHED_SCHEMA_DATA: ESteamLearnInferenceResult
STEAMLEARN_INFERENCE_ERROR_NO_FETCH_ID_FOUND: ESteamLearnInferenceResult
STEAMLEARN_INFERENCE_ERROR_NO_PUBLISHED_CONFIG: ESteamLearnInferenceResult
STEAMLEARN_INFERENCE_ERROR_TOO_BUSY: ESteamLearnInferenceResult
STEAMLEARN_INFERENCE_METADATA_ERROR: ESteamLearnInferenceMetadataResult
STEAMLEARN_INFERENCE_METADATA_ERROR_FORBIDDEN: ESteamLearnInferenceMetadataResult
STEAMLEARN_INFERENCE_METADATA_ERROR_INVALID_PROJECT_ID: (
    ESteamLearnInferenceMetadataResult
)
STEAMLEARN_INFERENCE_METADATA_ERROR_INVALID_PUBLISHED_VERSION: (
    ESteamLearnInferenceMetadataResult
)
STEAMLEARN_INFERENCE_METADATA_ERROR_INVALID_TIMESTAMP: (
    ESteamLearnInferenceMetadataResult
)
STEAMLEARN_INFERENCE_METADATA_ERROR_NO_FETCH_ID_FOUND: (
    ESteamLearnInferenceMetadataResult
)
STEAMLEARN_INFERENCE_METADATA_ERROR_NO_PUBLISHED_CONFIG: (
    ESteamLearnInferenceMetadataResult
)
STEAMLEARN_INFERENCE_METADATA_SUCCESS: ESteamLearnInferenceMetadataResult
STEAMLEARN_INFERENCE_SUCCESS: ESteamLearnInferenceResult
STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_DISABLED: ESteammLearnRegisterDataSourceResult
STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR: ESteammLearnRegisterDataSourceResult
STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_DATA_CHANGED: (
    ESteammLearnRegisterDataSourceResult
)
STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_DATA_INVALID: (
    ESteammLearnRegisterDataSourceResult
)
STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_FORBIDDEN: (
    ESteammLearnRegisterDataSourceResult
)
STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_GENERIC: (
    ESteammLearnRegisterDataSourceResult
)
STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_INVALID_NAME: (
    ESteammLearnRegisterDataSourceResult
)
STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_INVALID_TIMESTAMP: (
    ESteammLearnRegisterDataSourceResult
)
STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_INVALID_VERSION: (
    ESteammLearnRegisterDataSourceResult
)
STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_SUCCESS_CREATED: (
    ESteammLearnRegisterDataSourceResult
)
STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_SUCCESS_FOUND: (
    ESteammLearnRegisterDataSourceResult
)
STEAMLEARN_SNAPSHOT_PROJECT_DISABLED: ESteamLearnSnapshotProjectResult
STEAMLEARN_SNAPSHOT_PROJECT_ERROR: ESteamLearnSnapshotProjectResult
STEAMLEARN_SNAPSHOT_PROJECT_ERROR_FORBIDDEN: ESteamLearnSnapshotProjectResult
STEAMLEARN_SNAPSHOT_PROJECT_ERROR_INTERNAL_DATA_SOURCE_ERROR: (
    ESteamLearnSnapshotProjectResult
)
STEAMLEARN_SNAPSHOT_PROJECT_ERROR_INVALID_DATA_SOURCE_KEY: (
    ESteamLearnSnapshotProjectResult
)
STEAMLEARN_SNAPSHOT_PROJECT_ERROR_INVALID_PROJECT_ID: ESteamLearnSnapshotProjectResult
STEAMLEARN_SNAPSHOT_PROJECT_ERROR_INVALID_PUBLISHED_VERSION: (
    ESteamLearnSnapshotProjectResult
)
STEAMLEARN_SNAPSHOT_PROJECT_ERROR_INVALID_TIMESTAMP: ESteamLearnSnapshotProjectResult
STEAMLEARN_SNAPSHOT_PROJECT_ERROR_MISSING_CACHE_DURATION: (
    ESteamLearnSnapshotProjectResult
)
STEAMLEARN_SNAPSHOT_PROJECT_ERROR_NO_PUBLISHED_CONFIG: ESteamLearnSnapshotProjectResult
STEAMLEARN_SNAPSHOT_PROJECT_ERROR_UNKNOWN_DATA_SOURCE: ESteamLearnSnapshotProjectResult
STEAMLEARN_SNAPSHOT_PROJECT_SUCCESS_QUEUED: ESteamLearnSnapshotProjectResult
STEAMLEARN_SNAPSHOT_PROJECT_SUCCESS_STORED: ESteamLearnSnapshotProjectResult

class CMsgSteamLearnAccessTokens(_message.Message):
    __slots__ = [
        "cache_data_access_tokens",
        "inference_access_tokens",
        "register_data_source_access_token",
        "snapshot_project_access_tokens",
    ]

    class CacheDataAccessToken(_message.Message):
        __slots__ = ["access_token", "data_source_id"]
        ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
        DATA_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        access_token: str
        data_source_id: int
        def __init__(
            self,
            data_source_id: _Optional[int] = ...,
            access_token: _Optional[str] = ...,
        ) -> None: ...

    class InferenceAccessToken(_message.Message):
        __slots__ = ["access_token", "project_id"]
        ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
        access_token: str
        project_id: int
        def __init__(
            self, project_id: _Optional[int] = ..., access_token: _Optional[str] = ...
        ) -> None: ...

    class SnapshotProjectAccessToken(_message.Message):
        __slots__ = ["access_token", "project_id"]
        ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
        access_token: str
        project_id: int
        def __init__(
            self, project_id: _Optional[int] = ..., access_token: _Optional[str] = ...
        ) -> None: ...

    CACHE_DATA_ACCESS_TOKENS_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_ACCESS_TOKENS_FIELD_NUMBER: _ClassVar[int]
    REGISTER_DATA_SOURCE_ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_PROJECT_ACCESS_TOKENS_FIELD_NUMBER: _ClassVar[int]
    cache_data_access_tokens: _containers.RepeatedCompositeFieldContainer[
        CMsgSteamLearnAccessTokens.CacheDataAccessToken
    ]
    inference_access_tokens: _containers.RepeatedCompositeFieldContainer[
        CMsgSteamLearnAccessTokens.InferenceAccessToken
    ]
    register_data_source_access_token: str
    snapshot_project_access_tokens: _containers.RepeatedCompositeFieldContainer[
        CMsgSteamLearnAccessTokens.SnapshotProjectAccessToken
    ]
    def __init__(
        self,
        register_data_source_access_token: _Optional[str] = ...,
        cache_data_access_tokens: _Optional[
            _Iterable[_Union[CMsgSteamLearnAccessTokens.CacheDataAccessToken, _Mapping]]
        ] = ...,
        snapshot_project_access_tokens: _Optional[
            _Iterable[
                _Union[CMsgSteamLearnAccessTokens.SnapshotProjectAccessToken, _Mapping]
            ]
        ] = ...,
        inference_access_tokens: _Optional[
            _Iterable[_Union[CMsgSteamLearnAccessTokens.InferenceAccessToken, _Mapping]]
        ] = ...,
    ) -> None: ...

class CMsgSteamLearnData(_message.Message):
    __slots__ = ["data_object", "data_source_id", "keys"]
    DATA_OBJECT_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    data_object: CMsgSteamLearnDataObject
    data_source_id: int
    keys: _containers.RepeatedScalarFieldContainer[int]
    def __init__(
        self,
        data_source_id: _Optional[int] = ...,
        keys: _Optional[_Iterable[int]] = ...,
        data_object: _Optional[_Union[CMsgSteamLearnDataObject, _Mapping]] = ...,
    ) -> None: ...

class CMsgSteamLearnDataElement(_message.Message):
    __slots__ = [
        "data_bools",
        "data_floats",
        "data_int32s",
        "data_objects",
        "data_strings",
        "name",
    ]
    DATA_BOOLS_FIELD_NUMBER: _ClassVar[int]
    DATA_FLOATS_FIELD_NUMBER: _ClassVar[int]
    DATA_INT32S_FIELD_NUMBER: _ClassVar[int]
    DATA_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    DATA_STRINGS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    data_bools: _containers.RepeatedScalarFieldContainer[bool]
    data_floats: _containers.RepeatedScalarFieldContainer[float]
    data_int32s: _containers.RepeatedScalarFieldContainer[int]
    data_objects: _containers.RepeatedCompositeFieldContainer[CMsgSteamLearnDataObject]
    data_strings: _containers.RepeatedScalarFieldContainer[str]
    name: str
    def __init__(
        self,
        name: _Optional[str] = ...,
        data_int32s: _Optional[_Iterable[int]] = ...,
        data_floats: _Optional[_Iterable[float]] = ...,
        data_bools: _Optional[_Iterable[bool]] = ...,
        data_strings: _Optional[_Iterable[str]] = ...,
        data_objects: _Optional[
            _Iterable[_Union[CMsgSteamLearnDataObject, _Mapping]]
        ] = ...,
    ) -> None: ...

class CMsgSteamLearnDataList(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[CMsgSteamLearnData]
    def __init__(
        self, data: _Optional[_Iterable[_Union[CMsgSteamLearnData, _Mapping]]] = ...
    ) -> None: ...

class CMsgSteamLearnDataObject(_message.Message):
    __slots__ = ["elements"]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    elements: _containers.RepeatedCompositeFieldContainer[CMsgSteamLearnDataElement]
    def __init__(
        self,
        elements: _Optional[
            _Iterable[_Union[CMsgSteamLearnDataElement, _Mapping]]
        ] = ...,
    ) -> None: ...

class CMsgSteamLearnDataSource(_message.Message):
    __slots__ = [
        "cache_duration_seconds",
        "id",
        "name",
        "source_description",
        "structure",
        "structure_crc",
        "version",
    ]
    CACHE_DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STRUCTURE_CRC_FIELD_NUMBER: _ClassVar[int]
    STRUCTURE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    cache_duration_seconds: int
    id: int
    name: str
    source_description: str
    structure: CMsgSteamLearnDataSourceDescObject
    structure_crc: int
    version: int
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        version: _Optional[int] = ...,
        source_description: _Optional[str] = ...,
        structure: _Optional[
            _Union[CMsgSteamLearnDataSourceDescObject, _Mapping]
        ] = ...,
        structure_crc: _Optional[int] = ...,
        cache_duration_seconds: _Optional[int] = ...,
    ) -> None: ...

class CMsgSteamLearnDataSourceDescElement(_message.Message):
    __slots__ = ["count", "data_type", "name", "object"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    count: int
    data_type: ESteamLearnDataType
    name: str
    object: CMsgSteamLearnDataSourceDescObject
    def __init__(
        self,
        name: _Optional[str] = ...,
        data_type: _Optional[_Union[ESteamLearnDataType, str]] = ...,
        object: _Optional[_Union[CMsgSteamLearnDataSourceDescObject, _Mapping]] = ...,
        count: _Optional[int] = ...,
    ) -> None: ...

class CMsgSteamLearnDataSourceDescObject(_message.Message):
    __slots__ = ["elements"]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    elements: _containers.RepeatedCompositeFieldContainer[
        CMsgSteamLearnDataSourceDescElement
    ]
    def __init__(
        self,
        elements: _Optional[
            _Iterable[_Union[CMsgSteamLearnDataSourceDescElement, _Mapping]]
        ] = ...,
    ) -> None: ...

class CMsgSteamLearn_BatchOperation_Request(_message.Message):
    __slots__ = ["cache_data_requests", "inference_requests", "snapshot_requests"]
    CACHE_DATA_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    cache_data_requests: _containers.RepeatedCompositeFieldContainer[
        CMsgSteamLearn_CacheData_Request
    ]
    inference_requests: _containers.RepeatedCompositeFieldContainer[
        CMsgSteamLearn_Inference_Request
    ]
    snapshot_requests: _containers.RepeatedCompositeFieldContainer[
        CMsgSteamLearn_SnapshotProject_Request
    ]
    def __init__(
        self,
        cache_data_requests: _Optional[
            _Iterable[_Union[CMsgSteamLearn_CacheData_Request, _Mapping]]
        ] = ...,
        snapshot_requests: _Optional[
            _Iterable[_Union[CMsgSteamLearn_SnapshotProject_Request, _Mapping]]
        ] = ...,
        inference_requests: _Optional[
            _Iterable[_Union[CMsgSteamLearn_Inference_Request, _Mapping]]
        ] = ...,
    ) -> None: ...

class CMsgSteamLearn_BatchOperation_Response(_message.Message):
    __slots__ = ["cache_data_responses", "inference_responses", "snapshot_responses"]
    CACHE_DATA_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    cache_data_responses: _containers.RepeatedCompositeFieldContainer[
        CMsgSteamLearn_CacheData_Response
    ]
    inference_responses: _containers.RepeatedCompositeFieldContainer[
        CMsgSteamLearn_Inference_Response
    ]
    snapshot_responses: _containers.RepeatedCompositeFieldContainer[
        CMsgSteamLearn_SnapshotProject_Response
    ]
    def __init__(
        self,
        cache_data_responses: _Optional[
            _Iterable[_Union[CMsgSteamLearn_CacheData_Response, _Mapping]]
        ] = ...,
        snapshot_responses: _Optional[
            _Iterable[_Union[CMsgSteamLearn_SnapshotProject_Response, _Mapping]]
        ] = ...,
        inference_responses: _Optional[
            _Iterable[_Union[CMsgSteamLearn_Inference_Response, _Mapping]]
        ] = ...,
    ) -> None: ...

class CMsgSteamLearn_CacheData_Request(_message.Message):
    __slots__ = ["access_token", "data"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    data: CMsgSteamLearnData
    def __init__(
        self,
        access_token: _Optional[str] = ...,
        data: _Optional[_Union[CMsgSteamLearnData, _Mapping]] = ...,
    ) -> None: ...

class CMsgSteamLearn_CacheData_Response(_message.Message):
    __slots__ = ["cache_data_result"]
    CACHE_DATA_RESULT_FIELD_NUMBER: _ClassVar[int]
    cache_data_result: ESteamLearnCacheDataResult
    def __init__(
        self,
        cache_data_result: _Optional[_Union[ESteamLearnCacheDataResult, str]] = ...,
    ) -> None: ...

class CMsgSteamLearn_GetAccessTokens_Request(_message.Message):
    __slots__ = ["appid"]
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CMsgSteamLearn_GetAccessTokens_Response(_message.Message):
    __slots__ = ["access_tokens", "result"]
    ACCESS_TOKENS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    access_tokens: CMsgSteamLearnAccessTokens
    result: ESteamLearnGetAccessTokensResult
    def __init__(
        self,
        result: _Optional[_Union[ESteamLearnGetAccessTokensResult, str]] = ...,
        access_tokens: _Optional[_Union[CMsgSteamLearnAccessTokens, _Mapping]] = ...,
    ) -> None: ...

class CMsgSteamLearn_InferenceBackend_Response(_message.Message):
    __slots__ = ["outputs"]

    class BinaryCrossEntropyOutput(_message.Message):
        __slots__ = ["value"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: float
        def __init__(self, value: _Optional[float] = ...) -> None: ...

    class CategoricalCrossEntropyOutput(_message.Message):
        __slots__ = ["value", "weight"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        WEIGHT_FIELD_NUMBER: _ClassVar[int]
        value: _containers.RepeatedScalarFieldContainer[float]
        weight: _containers.RepeatedScalarFieldContainer[float]
        def __init__(
            self,
            weight: _Optional[_Iterable[float]] = ...,
            value: _Optional[_Iterable[float]] = ...,
        ) -> None: ...

    class MutliBinaryCrossEntropyOutput(_message.Message):
        __slots__ = ["value", "weight"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        WEIGHT_FIELD_NUMBER: _ClassVar[int]
        value: _containers.RepeatedScalarFieldContainer[float]
        weight: _containers.RepeatedScalarFieldContainer[float]
        def __init__(
            self,
            weight: _Optional[_Iterable[float]] = ...,
            value: _Optional[_Iterable[float]] = ...,
        ) -> None: ...

    class Output(_message.Message):
        __slots__ = [
            "binary_crossentropy",
            "categorical_crossentropy",
            "multi_binary_crossentropy",
            "regression",
        ]
        BINARY_CROSSENTROPY_FIELD_NUMBER: _ClassVar[int]
        CATEGORICAL_CROSSENTROPY_FIELD_NUMBER: _ClassVar[int]
        MULTI_BINARY_CROSSENTROPY_FIELD_NUMBER: _ClassVar[int]
        REGRESSION_FIELD_NUMBER: _ClassVar[int]
        binary_crossentropy: (
            CMsgSteamLearn_InferenceBackend_Response.BinaryCrossEntropyOutput
        )
        categorical_crossentropy: (
            CMsgSteamLearn_InferenceBackend_Response.CategoricalCrossEntropyOutput
        )
        multi_binary_crossentropy: (
            CMsgSteamLearn_InferenceBackend_Response.MutliBinaryCrossEntropyOutput
        )
        regression: CMsgSteamLearn_InferenceBackend_Response.RegressionOutput
        def __init__(
            self,
            binary_crossentropy: _Optional[
                _Union[
                    CMsgSteamLearn_InferenceBackend_Response.BinaryCrossEntropyOutput,
                    _Mapping,
                ]
            ] = ...,
            categorical_crossentropy: _Optional[
                _Union[
                    CMsgSteamLearn_InferenceBackend_Response.CategoricalCrossEntropyOutput,
                    _Mapping,
                ]
            ] = ...,
            multi_binary_crossentropy: _Optional[
                _Union[
                    CMsgSteamLearn_InferenceBackend_Response.MutliBinaryCrossEntropyOutput,
                    _Mapping,
                ]
            ] = ...,
            regression: _Optional[
                _Union[
                    CMsgSteamLearn_InferenceBackend_Response.RegressionOutput, _Mapping
                ]
            ] = ...,
        ) -> None: ...

    class RegressionOutput(_message.Message):
        __slots__ = ["value"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: float
        def __init__(self, value: _Optional[float] = ...) -> None: ...

    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    outputs: _containers.RepeatedCompositeFieldContainer[
        CMsgSteamLearn_InferenceBackend_Response.Output
    ]
    def __init__(
        self,
        outputs: _Optional[
            _Iterable[_Union[CMsgSteamLearn_InferenceBackend_Response.Output, _Mapping]]
        ] = ...,
    ) -> None: ...

class CMsgSteamLearn_InferenceMetadataBackend_Request(_message.Message):
    __slots__ = ["fetch_id", "project_id"]
    FETCH_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    fetch_id: int
    project_id: int
    def __init__(
        self, project_id: _Optional[int] = ..., fetch_id: _Optional[int] = ...
    ) -> None: ...

class CMsgSteamLearn_InferenceMetadata_Request(_message.Message):
    __slots__ = ["access_token", "override_train_id", "project_id", "published_version"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_TRAIN_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_VERSION_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    override_train_id: int
    project_id: int
    published_version: int
    def __init__(
        self,
        access_token: _Optional[str] = ...,
        project_id: _Optional[int] = ...,
        published_version: _Optional[int] = ...,
        override_train_id: _Optional[int] = ...,
    ) -> None: ...

class CMsgSteamLearn_InferenceMetadata_Response(_message.Message):
    __slots__ = [
        "compact_tables",
        "inference_metadata_result",
        "kmeans",
        "ranges",
        "row_range",
        "snapshot_histogram",
        "std_devs",
    ]

    class CompactTable(_message.Message):
        __slots__ = ["map_mappings", "map_values", "name"]

        class Entry(_message.Message):
            __slots__ = ["count", "mapping", "value"]
            COUNT_FIELD_NUMBER: _ClassVar[int]
            MAPPING_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            count: int
            mapping: int
            value: int
            def __init__(
                self,
                value: _Optional[int] = ...,
                mapping: _Optional[int] = ...,
                count: _Optional[int] = ...,
            ) -> None: ...

        class MapMappingsEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: CMsgSteamLearn_InferenceMetadata_Response.CompactTable.Entry
            def __init__(
                self,
                key: _Optional[int] = ...,
                value: _Optional[
                    _Union[
                        CMsgSteamLearn_InferenceMetadata_Response.CompactTable.Entry,
                        _Mapping,
                    ]
                ] = ...,
            ) -> None: ...

        class MapValuesEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: CMsgSteamLearn_InferenceMetadata_Response.CompactTable.Entry
            def __init__(
                self,
                key: _Optional[int] = ...,
                value: _Optional[
                    _Union[
                        CMsgSteamLearn_InferenceMetadata_Response.CompactTable.Entry,
                        _Mapping,
                    ]
                ] = ...,
            ) -> None: ...

        MAP_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
        MAP_VALUES_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        map_mappings: _containers.RepeatedCompositeFieldContainer[
            CMsgSteamLearn_InferenceMetadata_Response.CompactTable.MapMappingsEntry
        ]
        map_values: _containers.RepeatedCompositeFieldContainer[
            CMsgSteamLearn_InferenceMetadata_Response.CompactTable.MapValuesEntry
        ]
        name: str
        def __init__(
            self,
            name: _Optional[str] = ...,
            map_values: _Optional[
                _Iterable[
                    _Union[
                        CMsgSteamLearn_InferenceMetadata_Response.CompactTable.MapValuesEntry,
                        _Mapping,
                    ]
                ]
            ] = ...,
            map_mappings: _Optional[
                _Iterable[
                    _Union[
                        CMsgSteamLearn_InferenceMetadata_Response.CompactTable.MapMappingsEntry,
                        _Mapping,
                    ]
                ]
            ] = ...,
        ) -> None: ...

    class KMeans(_message.Message):
        __slots__ = ["clusters", "name"]

        class Cluster(_message.Message):
            __slots__ = [
                "radius",
                "radius_25pct",
                "radius_50pct",
                "radius_75pct",
                "x",
                "y",
            ]
            RADIUS_25PCT_FIELD_NUMBER: _ClassVar[int]
            RADIUS_50PCT_FIELD_NUMBER: _ClassVar[int]
            RADIUS_75PCT_FIELD_NUMBER: _ClassVar[int]
            RADIUS_FIELD_NUMBER: _ClassVar[int]
            X_FIELD_NUMBER: _ClassVar[int]
            Y_FIELD_NUMBER: _ClassVar[int]
            radius: float
            radius_25pct: float
            radius_50pct: float
            radius_75pct: float
            x: float
            y: float
            def __init__(
                self,
                x: _Optional[float] = ...,
                y: _Optional[float] = ...,
                radius: _Optional[float] = ...,
                radius_75pct: _Optional[float] = ...,
                radius_50pct: _Optional[float] = ...,
                radius_25pct: _Optional[float] = ...,
            ) -> None: ...

        CLUSTERS_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        clusters: _containers.RepeatedCompositeFieldContainer[
            CMsgSteamLearn_InferenceMetadata_Response.KMeans.Cluster
        ]
        name: str
        def __init__(
            self,
            name: _Optional[str] = ...,
            clusters: _Optional[
                _Iterable[
                    _Union[
                        CMsgSteamLearn_InferenceMetadata_Response.KMeans.Cluster,
                        _Mapping,
                    ]
                ]
            ] = ...,
        ) -> None: ...

    class Range(_message.Message):
        __slots__ = ["data_element_path", "max_value", "min_value"]
        DATA_ELEMENT_PATH_FIELD_NUMBER: _ClassVar[int]
        MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
        MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
        data_element_path: str
        max_value: float
        min_value: float
        def __init__(
            self,
            data_element_path: _Optional[str] = ...,
            min_value: _Optional[float] = ...,
            max_value: _Optional[float] = ...,
        ) -> None: ...

    class RowRange(_message.Message):
        __slots__ = ["max_row", "min_row"]
        MAX_ROW_FIELD_NUMBER: _ClassVar[int]
        MIN_ROW_FIELD_NUMBER: _ClassVar[int]
        max_row: int
        min_row: int
        def __init__(
            self, min_row: _Optional[int] = ..., max_row: _Optional[int] = ...
        ) -> None: ...

    class SnapshotHistogram(_message.Message):
        __slots__ = ["bucket_counts", "max_value", "min_value", "num_buckets"]
        BUCKET_COUNTS_FIELD_NUMBER: _ClassVar[int]
        MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
        MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
        NUM_BUCKETS_FIELD_NUMBER: _ClassVar[int]
        bucket_counts: _containers.RepeatedScalarFieldContainer[int]
        max_value: float
        min_value: float
        num_buckets: int
        def __init__(
            self,
            min_value: _Optional[float] = ...,
            max_value: _Optional[float] = ...,
            num_buckets: _Optional[int] = ...,
            bucket_counts: _Optional[_Iterable[int]] = ...,
        ) -> None: ...

    class StdDev(_message.Message):
        __slots__ = ["data_element_path", "mean", "std_dev"]
        DATA_ELEMENT_PATH_FIELD_NUMBER: _ClassVar[int]
        MEAN_FIELD_NUMBER: _ClassVar[int]
        STD_DEV_FIELD_NUMBER: _ClassVar[int]
        data_element_path: str
        mean: float
        std_dev: float
        def __init__(
            self,
            data_element_path: _Optional[str] = ...,
            mean: _Optional[float] = ...,
            std_dev: _Optional[float] = ...,
        ) -> None: ...

    COMPACT_TABLES_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_METADATA_RESULT_FIELD_NUMBER: _ClassVar[int]
    KMEANS_FIELD_NUMBER: _ClassVar[int]
    RANGES_FIELD_NUMBER: _ClassVar[int]
    ROW_RANGE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
    STD_DEVS_FIELD_NUMBER: _ClassVar[int]
    compact_tables: _containers.RepeatedCompositeFieldContainer[
        CMsgSteamLearn_InferenceMetadata_Response.CompactTable
    ]
    inference_metadata_result: ESteamLearnInferenceMetadataResult
    kmeans: _containers.RepeatedCompositeFieldContainer[
        CMsgSteamLearn_InferenceMetadata_Response.KMeans
    ]
    ranges: _containers.RepeatedCompositeFieldContainer[
        CMsgSteamLearn_InferenceMetadata_Response.Range
    ]
    row_range: CMsgSteamLearn_InferenceMetadata_Response.RowRange
    snapshot_histogram: CMsgSteamLearn_InferenceMetadata_Response.SnapshotHistogram
    std_devs: _containers.RepeatedCompositeFieldContainer[
        CMsgSteamLearn_InferenceMetadata_Response.StdDev
    ]
    def __init__(
        self,
        inference_metadata_result: _Optional[
            _Union[ESteamLearnInferenceMetadataResult, str]
        ] = ...,
        row_range: _Optional[
            _Union[CMsgSteamLearn_InferenceMetadata_Response.RowRange, _Mapping]
        ] = ...,
        ranges: _Optional[
            _Iterable[_Union[CMsgSteamLearn_InferenceMetadata_Response.Range, _Mapping]]
        ] = ...,
        std_devs: _Optional[
            _Iterable[
                _Union[CMsgSteamLearn_InferenceMetadata_Response.StdDev, _Mapping]
            ]
        ] = ...,
        compact_tables: _Optional[
            _Iterable[
                _Union[CMsgSteamLearn_InferenceMetadata_Response.CompactTable, _Mapping]
            ]
        ] = ...,
        kmeans: _Optional[
            _Iterable[
                _Union[CMsgSteamLearn_InferenceMetadata_Response.KMeans, _Mapping]
            ]
        ] = ...,
        snapshot_histogram: _Optional[
            _Union[
                CMsgSteamLearn_InferenceMetadata_Response.SnapshotHistogram, _Mapping
            ]
        ] = ...,
    ) -> None: ...

class CMsgSteamLearn_Inference_Request(_message.Message):
    __slots__ = [
        "access_token",
        "additional_data",
        "data",
        "override_train_id",
        "project_id",
        "published_version",
    ]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_TRAIN_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_VERSION_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    additional_data: _containers.RepeatedScalarFieldContainer[float]
    data: CMsgSteamLearnDataList
    override_train_id: int
    project_id: int
    published_version: int
    def __init__(
        self,
        access_token: _Optional[str] = ...,
        project_id: _Optional[int] = ...,
        published_version: _Optional[int] = ...,
        override_train_id: _Optional[int] = ...,
        data: _Optional[_Union[CMsgSteamLearnDataList, _Mapping]] = ...,
        additional_data: _Optional[_Iterable[float]] = ...,
    ) -> None: ...

class CMsgSteamLearn_Inference_Response(_message.Message):
    __slots__ = ["backend_response", "inference_result", "keys"]
    BACKEND_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_RESULT_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    backend_response: CMsgSteamLearn_InferenceBackend_Response
    inference_result: ESteamLearnInferenceResult
    keys: _containers.RepeatedScalarFieldContainer[int]
    def __init__(
        self,
        inference_result: _Optional[_Union[ESteamLearnInferenceResult, str]] = ...,
        backend_response: _Optional[
            _Union[CMsgSteamLearn_InferenceBackend_Response, _Mapping]
        ] = ...,
        keys: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class CMsgSteamLearn_RegisterDataSource_Request(_message.Message):
    __slots__ = ["access_token", "data_source"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    data_source: CMsgSteamLearnDataSource
    def __init__(
        self,
        access_token: _Optional[str] = ...,
        data_source: _Optional[_Union[CMsgSteamLearnDataSource, _Mapping]] = ...,
    ) -> None: ...

class CMsgSteamLearn_RegisterDataSource_Response(_message.Message):
    __slots__ = ["data_source", "result"]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    data_source: CMsgSteamLearnDataSource
    result: ESteammLearnRegisterDataSourceResult
    def __init__(
        self,
        result: _Optional[_Union[ESteammLearnRegisterDataSourceResult, str]] = ...,
        data_source: _Optional[_Union[CMsgSteamLearnDataSource, _Mapping]] = ...,
    ) -> None: ...

class CMsgSteamLearn_SnapshotProject_Request(_message.Message):
    __slots__ = [
        "access_token",
        "data",
        "keys",
        "pending_data_limit_seconds",
        "project_id",
        "published_version",
    ]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    PENDING_DATA_LIMIT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_VERSION_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    data: _containers.RepeatedCompositeFieldContainer[CMsgSteamLearnData]
    keys: _containers.RepeatedScalarFieldContainer[int]
    pending_data_limit_seconds: int
    project_id: int
    published_version: int
    def __init__(
        self,
        access_token: _Optional[str] = ...,
        project_id: _Optional[int] = ...,
        published_version: _Optional[int] = ...,
        keys: _Optional[_Iterable[int]] = ...,
        data: _Optional[_Iterable[_Union[CMsgSteamLearnData, _Mapping]]] = ...,
        pending_data_limit_seconds: _Optional[int] = ...,
    ) -> None: ...

class CMsgSteamLearn_SnapshotProject_Response(_message.Message):
    __slots__ = ["snapshot_result"]
    SNAPSHOT_RESULT_FIELD_NUMBER: _ClassVar[int]
    snapshot_result: ESteamLearnSnapshotProjectResult
    def __init__(
        self,
        snapshot_result: _Optional[_Union[ESteamLearnSnapshotProjectResult, str]] = ...,
    ) -> None: ...

class ESteamLearnDataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ESteammLearnRegisterDataSourceResult(
    int, metaclass=_enum_type_wrapper.EnumTypeWrapper
):
    __slots__ = []

class ESteamLearnCacheDataResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ESteamLearnSnapshotProjectResult(
    int, metaclass=_enum_type_wrapper.EnumTypeWrapper
):
    __slots__ = []

class ESteamLearnGetAccessTokensResult(
    int, metaclass=_enum_type_wrapper.EnumTypeWrapper
):
    __slots__ = []

class ESteamLearnInferenceResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ESteamLearnInferenceMetadataResult(
    int, metaclass=_enum_type_wrapper.EnumTypeWrapper
):
    __slots__ = []
