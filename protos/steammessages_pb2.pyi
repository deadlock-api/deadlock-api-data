from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor
GCProtoBufMsgSrc_FromGC: GCProtoBufMsgSrc
GCProtoBufMsgSrc_FromSteamID: GCProtoBufMsgSrc
GCProtoBufMsgSrc_FromSystem: GCProtoBufMsgSrc
GCProtoBufMsgSrc_ReplySystem: GCProtoBufMsgSrc
GCProtoBufMsgSrc_SpoofedSteamID: GCProtoBufMsgSrc
GCProtoBufMsgSrc_Unspecified: GCProtoBufMsgSrc
KEY_FIELD_FIELD_NUMBER: _ClassVar[int]
MSGPOOL_HARD_LIMIT_FIELD_NUMBER: _ClassVar[int]
MSGPOOL_SOFT_LIMIT_FIELD_NUMBER: _ClassVar[int]
k_eGCPlatform_Android: EGCPlatform
k_eGCPlatform_Linux: EGCPlatform
k_eGCPlatform_Mac: EGCPlatform
k_eGCPlatform_None: EGCPlatform
k_eGCPlatform_PC: EGCPlatform
k_eGCPlatform_iOS: EGCPlatform
key_field: _descriptor.FieldDescriptor
msgpool_hard_limit: _descriptor.FieldDescriptor
msgpool_soft_limit: _descriptor.FieldDescriptor

class CGCMsgGetIPLocationResponse(_message.Message):
    __slots__ = ["infos"]
    INFOS_FIELD_NUMBER: _ClassVar[int]
    infos: _containers.RepeatedCompositeFieldContainer[CIPLocationInfo]
    def __init__(
        self, infos: _Optional[_Iterable[_Union[CIPLocationInfo, _Mapping]]] = ...
    ) -> None: ...

class CGCSystemMsg_GetAccountDetails(_message.Message):
    __slots__ = ["appid", "steamid"]
    APPID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    steamid: int
    def __init__(
        self, steamid: _Optional[int] = ..., appid: _Optional[int] = ...
    ) -> None: ...

class CGCSystemMsg_GetAccountDetails_Response(_message.Message):
    __slots__ = [
        "account_creation_time",
        "account_name",
        "accountid",
        "currency",
        "eresult_deprecated",
        "free_trial_expiration",
        "friend_count",
        "has_accepted_china_ssa",
        "is_account_locked_down",
        "is_banned_steam_china",
        "is_community_banned",
        "is_cyber_cafe",
        "is_free_trial_account",
        "is_inventory_public",
        "is_limited",
        "is_low_violence",
        "is_phone_identifying",
        "is_phone_verified",
        "is_profile_created",
        "is_profile_public",
        "is_school_account",
        "is_steamguard_enabled",
        "is_subscribed",
        "is_trade_banned",
        "is_two_factor_auth_enabled",
        "is_vac_banned",
        "package",
        "persona_name",
        "phone_id",
        "phone_verification_time",
        "rt_birth_date",
        "rt_identity_linked",
        "steam_level",
        "suspension_end_time",
        "trade_ban_expiration",
        "two_factor_enabled_time",
        "txn_country_code",
    ]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ERESULT_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    FREE_TRIAL_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    FRIEND_COUNT_FIELD_NUMBER: _ClassVar[int]
    HAS_ACCEPTED_CHINA_SSA_FIELD_NUMBER: _ClassVar[int]
    IS_ACCOUNT_LOCKED_DOWN_FIELD_NUMBER: _ClassVar[int]
    IS_BANNED_STEAM_CHINA_FIELD_NUMBER: _ClassVar[int]
    IS_COMMUNITY_BANNED_FIELD_NUMBER: _ClassVar[int]
    IS_CYBER_CAFE_FIELD_NUMBER: _ClassVar[int]
    IS_FREE_TRIAL_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    IS_INVENTORY_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    IS_LIMITED_FIELD_NUMBER: _ClassVar[int]
    IS_LOW_VIOLENCE_FIELD_NUMBER: _ClassVar[int]
    IS_PHONE_IDENTIFYING_FIELD_NUMBER: _ClassVar[int]
    IS_PHONE_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    IS_PROFILE_CREATED_FIELD_NUMBER: _ClassVar[int]
    IS_PROFILE_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    IS_SCHOOL_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    IS_STEAMGUARD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    IS_TRADE_BANNED_FIELD_NUMBER: _ClassVar[int]
    IS_TWO_FACTOR_AUTH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_VAC_BANNED_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    PERSONA_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_ID_FIELD_NUMBER: _ClassVar[int]
    PHONE_VERIFICATION_TIME_FIELD_NUMBER: _ClassVar[int]
    RT_BIRTH_DATE_FIELD_NUMBER: _ClassVar[int]
    RT_IDENTITY_LINKED_FIELD_NUMBER: _ClassVar[int]
    STEAM_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SUSPENSION_END_TIME_FIELD_NUMBER: _ClassVar[int]
    TRADE_BAN_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    TWO_FACTOR_ENABLED_TIME_FIELD_NUMBER: _ClassVar[int]
    TXN_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    account_creation_time: int
    account_name: str
    accountid: int
    currency: str
    eresult_deprecated: int
    free_trial_expiration: int
    friend_count: int
    has_accepted_china_ssa: bool
    is_account_locked_down: bool
    is_banned_steam_china: bool
    is_community_banned: bool
    is_cyber_cafe: bool
    is_free_trial_account: bool
    is_inventory_public: bool
    is_limited: bool
    is_low_violence: bool
    is_phone_identifying: bool
    is_phone_verified: bool
    is_profile_created: bool
    is_profile_public: bool
    is_school_account: bool
    is_steamguard_enabled: bool
    is_subscribed: bool
    is_trade_banned: bool
    is_two_factor_auth_enabled: bool
    is_vac_banned: bool
    package: int
    persona_name: str
    phone_id: int
    phone_verification_time: int
    rt_birth_date: int
    rt_identity_linked: int
    steam_level: int
    suspension_end_time: int
    trade_ban_expiration: int
    two_factor_enabled_time: int
    txn_country_code: str
    def __init__(
        self,
        eresult_deprecated: _Optional[int] = ...,
        account_name: _Optional[str] = ...,
        persona_name: _Optional[str] = ...,
        is_profile_created: bool = ...,
        is_profile_public: bool = ...,
        is_inventory_public: bool = ...,
        is_vac_banned: bool = ...,
        is_cyber_cafe: bool = ...,
        is_school_account: bool = ...,
        is_limited: bool = ...,
        is_subscribed: bool = ...,
        package: _Optional[int] = ...,
        is_free_trial_account: bool = ...,
        free_trial_expiration: _Optional[int] = ...,
        is_low_violence: bool = ...,
        is_account_locked_down: bool = ...,
        is_community_banned: bool = ...,
        is_trade_banned: bool = ...,
        trade_ban_expiration: _Optional[int] = ...,
        accountid: _Optional[int] = ...,
        suspension_end_time: _Optional[int] = ...,
        currency: _Optional[str] = ...,
        steam_level: _Optional[int] = ...,
        friend_count: _Optional[int] = ...,
        account_creation_time: _Optional[int] = ...,
        is_steamguard_enabled: bool = ...,
        is_phone_verified: bool = ...,
        is_two_factor_auth_enabled: bool = ...,
        two_factor_enabled_time: _Optional[int] = ...,
        phone_verification_time: _Optional[int] = ...,
        phone_id: _Optional[int] = ...,
        is_phone_identifying: bool = ...,
        rt_identity_linked: _Optional[int] = ...,
        rt_birth_date: _Optional[int] = ...,
        txn_country_code: _Optional[str] = ...,
        has_accepted_china_ssa: bool = ...,
        is_banned_steam_china: bool = ...,
    ) -> None: ...

class CIPLocationInfo(_message.Message):
    __slots__ = ["city", "country", "ip", "latitude", "longitude", "state"]
    CITY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    city: str
    country: str
    ip: int
    latitude: float
    longitude: float
    state: str
    def __init__(
        self,
        ip: _Optional[int] = ...,
        latitude: _Optional[float] = ...,
        longitude: _Optional[float] = ...,
        country: _Optional[str] = ...,
        state: _Optional[str] = ...,
        city: _Optional[str] = ...,
    ) -> None: ...

class CMsgProtoBufHeader(_message.Message):
    __slots__ = [
        "client_session_id",
        "client_steam_id",
        "eresult",
        "error_message",
        "gc_dir_index_source",
        "gc_msg_src",
        "job_id_source",
        "job_id_target",
        "source_app_id",
        "target_job_name",
    ]
    CLIENT_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GC_DIR_INDEX_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GC_MSG_SRC_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_SOURCE_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_TARGET_FIELD_NUMBER: _ClassVar[int]
    SOURCE_APP_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    client_session_id: int
    client_steam_id: int
    eresult: int
    error_message: str
    gc_dir_index_source: int
    gc_msg_src: GCProtoBufMsgSrc
    job_id_source: int
    job_id_target: int
    source_app_id: int
    target_job_name: str
    def __init__(
        self,
        client_steam_id: _Optional[int] = ...,
        client_session_id: _Optional[int] = ...,
        source_app_id: _Optional[int] = ...,
        job_id_source: _Optional[int] = ...,
        job_id_target: _Optional[int] = ...,
        target_job_name: _Optional[str] = ...,
        eresult: _Optional[int] = ...,
        error_message: _Optional[str] = ...,
        gc_msg_src: _Optional[_Union[GCProtoBufMsgSrc, str]] = ...,
        gc_dir_index_source: _Optional[int] = ...,
    ) -> None: ...

class EGCPlatform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class GCProtoBufMsgSrc(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
