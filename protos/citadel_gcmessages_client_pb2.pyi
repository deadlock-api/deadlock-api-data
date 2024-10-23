from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

import citadel_gcmessages_common_pb2 as _citadel_gcmessages_common_pb2
import gcsdk_gcmessages_pb2 as _gcsdk_gcmessages_pb2
import steammessages_pb2 as _steammessages_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor
k_EMsgClientToGCBookUnlock: EGCCitadelClientMessages
k_EMsgClientToGCBookUnlockResponse: EGCCitadelClientMessages
k_EMsgClientToGCCommendPlayerFromMatch: EGCCitadelClientMessages
k_EMsgClientToGCCommendPlayerFromMatchResponse: EGCCitadelClientMessages
k_EMsgClientToGCDeleteHeroBuild: EGCCitadelClientMessages
k_EMsgClientToGCDeleteHeroBuildResponse: EGCCitadelClientMessages
k_EMsgClientToGCDevAction: EGCCitadelClientMessages
k_EMsgClientToGCDevActionResponse: EGCCitadelClientMessages
k_EMsgClientToGCDevSetMMBias: EGCCitadelClientMessages
k_EMsgClientToGCFindHeroBuilds: EGCCitadelClientMessages
k_EMsgClientToGCFindHeroBuildsResponse: EGCCitadelClientMessages
k_EMsgClientToGCGetAccountMatchReports: EGCCitadelClientMessages
k_EMsgClientToGCGetAccountMatchReportsResponse: EGCCitadelClientMessages
k_EMsgClientToGCGetAccountStats: EGCCitadelClientMessages
k_EMsgClientToGCGetAccountStatsResponse: EGCCitadelClientMessages
k_EMsgClientToGCGetActiveMatches: EGCCitadelClientMessages
k_EMsgClientToGCGetActiveMatchesResponse: EGCCitadelClientMessages
k_EMsgClientToGCGetBook: EGCCitadelClientMessages
k_EMsgClientToGCGetBookResponse: EGCCitadelClientMessages
k_EMsgClientToGCGetDiscordLink: EGCCitadelClientMessages
k_EMsgClientToGCGetDiscordLinkResponse: EGCCitadelClientMessages
k_EMsgClientToGCGetFriendGameStatus: EGCCitadelClientMessages
k_EMsgClientToGCGetFriendGameStatusResponse: EGCCitadelClientMessages
k_EMsgClientToGCGetHeroChoice: EGCCitadelClientMessages
k_EMsgClientToGCGetHeroChoiceResponse: EGCCitadelClientMessages
k_EMsgClientToGCGetMatchHistory: EGCCitadelClientMessages
k_EMsgClientToGCGetMatchHistoryResponse: EGCCitadelClientMessages
k_EMsgClientToGCGetMatchMetaData: EGCCitadelClientMessages
k_EMsgClientToGCGetMatchMetaDataResponse: EGCCitadelClientMessages
k_EMsgClientToGCGetOldHeroBuildData: EGCCitadelClientMessages
k_EMsgClientToGCGetOldHeroBuildDataResponse: EGCCitadelClientMessages
k_EMsgClientToGCGetProfileCard: EGCCitadelClientMessages
k_EMsgClientToGCGetProfileCardResponse: EGCCitadelClientMessages
k_EMsgClientToGCGrantForumAccess: EGCCitadelClientMessages
k_EMsgClientToGCGrantForumAccessResponse: EGCCitadelClientMessages
k_EMsgClientToGCIsInMatchmaking: EGCCitadelClientMessages
k_EMsgClientToGCIsInMatchmakingResponse: EGCCitadelClientMessages
k_EMsgClientToGCLeaveLobby: EGCCitadelClientMessages
k_EMsgClientToGCLeaveLobbyResponse: EGCCitadelClientMessages
k_EMsgClientToGCModeratorRequest: EGCCitadelClientMessages
k_EMsgClientToGCModeratorRequestResponse: EGCCitadelClientMessages
k_EMsgClientToGCModifyDevAnnouncements: EGCCitadelClientMessages
k_EMsgClientToGCModifyDevAnnouncementsResponse: EGCCitadelClientMessages
k_EMsgClientToGCPartyAction: EGCCitadelClientMessages
k_EMsgClientToGCPartyActionResponse: EGCCitadelClientMessages
k_EMsgClientToGCPartyCreate: EGCCitadelClientMessages
k_EMsgClientToGCPartyCreateResponse: EGCCitadelClientMessages
k_EMsgClientToGCPartyInviteUser: EGCCitadelClientMessages
k_EMsgClientToGCPartyInviteUserResponse: EGCCitadelClientMessages
k_EMsgClientToGCPartyJoin: EGCCitadelClientMessages
k_EMsgClientToGCPartyJoinResponse: EGCCitadelClientMessages
k_EMsgClientToGCPartyJoinViaCode: EGCCitadelClientMessages
k_EMsgClientToGCPartyJoinViaCodeResponse: EGCCitadelClientMessages
k_EMsgClientToGCPartyLeave: EGCCitadelClientMessages
k_EMsgClientToGCPartyLeaveResponse: EGCCitadelClientMessages
k_EMsgClientToGCPartySetMode: EGCCitadelClientMessages
k_EMsgClientToGCPartySetModeResponse: EGCCitadelClientMessages
k_EMsgClientToGCPartySetReadyState: EGCCitadelClientMessages
k_EMsgClientToGCPartySetReadyStateResponse: EGCCitadelClientMessages
k_EMsgClientToGCPartyStartMatch: EGCCitadelClientMessages
k_EMsgClientToGCPartyStartMatchResponse: EGCCitadelClientMessages
k_EMsgClientToGCPostMatchSurveyResponse: EGCCitadelClientMessages
k_EMsgClientToGCRecordClientEvents: EGCCitadelClientMessages
k_EMsgClientToGCRecordClientEventsResponse: EGCCitadelClientMessages
k_EMsgClientToGCReplacementSDRTicket: EGCCitadelClientMessages
k_EMsgClientToGCReplacementSDRTicketResponse: EGCCitadelClientMessages
k_EMsgClientToGCReportPlayerFromMatch: EGCCitadelClientMessages
k_EMsgClientToGCReportPlayerFromMatchResponse: EGCCitadelClientMessages
k_EMsgClientToGCSetNewPlayerProgress: EGCCitadelClientMessages
k_EMsgClientToGCSetNewPlayerProgressResponse: EGCCitadelClientMessages
k_EMsgClientToGCSetRankedSchedule: EGCCitadelClientMessages
k_EMsgClientToGCSetRankedScheduleResponse: EGCCitadelClientMessages
k_EMsgClientToGCSetServerConVar: EGCCitadelClientMessages
k_EMsgClientToGCSetServerConVarResponse: EGCCitadelClientMessages
k_EMsgClientToGCSpectateLobby: EGCCitadelClientMessages
k_EMsgClientToGCSpectateLobbyResponse: EGCCitadelClientMessages
k_EMsgClientToGCSpectateUser: EGCCitadelClientMessages
k_EMsgClientToGCSpectateUserResponse: EGCCitadelClientMessages
k_EMsgClientToGCStartMatchmaking: EGCCitadelClientMessages
k_EMsgClientToGCStartMatchmakingResponse: EGCCitadelClientMessages
k_EMsgClientToGCStopMatchmaking: EGCCitadelClientMessages
k_EMsgClientToGCStopMatchmakingResponse: EGCCitadelClientMessages
k_EMsgClientToGCSubmitPlaytestUser: EGCCitadelClientMessages
k_EMsgClientToGCSubmitPlaytestUserResponse: EGCCitadelClientMessages
k_EMsgClientToGCUnlockHero: EGCCitadelClientMessages
k_EMsgClientToGCUnlockHeroResponse: EGCCitadelClientMessages
k_EMsgClientToGCUpdateAccountSync: EGCCitadelClientMessages
k_EMsgClientToGCUpdateAccountSyncResponse: EGCCitadelClientMessages
k_EMsgClientToGCUpdateHeroBuild: EGCCitadelClientMessages
k_EMsgClientToGCUpdateHeroBuildPreference: EGCCitadelClientMessages
k_EMsgClientToGCUpdateHeroBuildPreferenceResponse: EGCCitadelClientMessages
k_EMsgClientToGCUpdateHeroBuildResponse: EGCCitadelClientMessages
k_EMsgClientToGCUpdateRoster: EGCCitadelClientMessages
k_EMsgClientToGCUpdateRosterResponse: EGCCitadelClientMessages
k_EMsgClientToGCUpdateSpectatorStatus: EGCCitadelClientMessages
k_EMsgGCToClientAccountStatsUpdated: EGCCitadelClientMessages
k_EMsgGCToClientBookUpdated: EGCCitadelClientMessages
k_EMsgGCToClientCanRejoinParty: EGCCitadelClientMessages
k_EMsgGCToClientCommendNotification: EGCCitadelClientMessages
k_EMsgGCToClientDevAnnouncements: EGCCitadelClientMessages
k_EMsgGCToClientDevPlaytestStatus: EGCCitadelClientMessages
k_EMsgGCToClientMatchmakingStopped: EGCCitadelClientMessages
k_EMsgGCToClientPartyEvent: EGCCitadelClientMessages
k_EMsgGCToClientProfileCardUpdated: EGCCitadelClientMessages
k_EMsgGCToClientRankedSchedule: EGCCitadelClientMessages
k_EMsgGCToClientSDRTicket: EGCCitadelClientMessages
k_EProfileCardSlotType_Empty: EProfileCardSlotType
k_EProfileCardSlotType_Hero: EProfileCardSlotType
k_EProfileCardSlotType_Stat: EProfileCardSlotType
k_eAcceptPartyInvite: ECitadelClientAccountEvent
k_eAccountPermission_Ranked: ECitadelAccountPermissionFlag
k_eBotMatch_Easy: ECitadelClientAccountEvent
k_eBotMatch_Guided: ECitadelClientAccountEvent
k_eBotMatch_Hard: ECitadelClientAccountEvent
k_eConnectAttemptReconnect: ECitadelClientAccountEvent
k_eConnectReacquireTicket: ECitadelClientAccountEvent
k_eCreatedParty: ECitadelClientAccountEvent
k_eCreatedPartyWithInvite: ECitadelClientAccountEvent
k_eDeleteReplay: ECitadelClientAccountEvent
k_eDisconnectConfirmed: ECitadelClientAccountEvent
k_eDisconnectPresentedPrompt: ECitadelClientAccountEvent
k_eDownloadedReplay: ECitadelClientAccountEvent
k_eEditRoster: ECitadelClientAccountEvent
k_eEnteredMatchMaking: ECitadelClientAccountEvent
k_eEnteredPartyMatchMaking: ECitadelClientAccountEvent
k_eFriendly: ECommendType
k_eInvalid: ECommendType
k_eJoinedPartyCode: ECitadelClientAccountEvent
k_eLaunchedClient: ECitadelClientAccountEvent
k_eLaunchedHeroTest: ECitadelClientAccountEvent
k_eLeftMatchMaking: ECitadelClientAccountEvent
k_eLeftPartyMatchMaking: ECitadelClientAccountEvent
k_eLiveUpdatedRoster: ECitadelClientAccountEvent
k_eMatchDetailsTab: ECitadelClientAccountEvent
k_eMatchMakingIdle_Displayed: ECitadelClientAccountEvent
k_eMatchMakingIdle_Stopped: ECitadelClientAccountEvent
k_eNewPlayerProgress_GettingStarted: ECitadelNewPlayerProgressFlag
k_eNewPlayerProgress_HeroTraining: ECitadelNewPlayerProgressFlag
k_eNewPlayerProgress_LaneTraining: ECitadelNewPlayerProgressFlag
k_eOpenedBookTest: ECitadelClientAccountEvent
k_eOpenedSubmitFeedback: ECitadelClientAccountEvent
k_eRejectPartyInvite: ECitadelClientAccountEvent
k_eSandboxViaHeroPage: ECitadelClientAccountEvent
k_eSentPartyInvite: ECitadelClientAccountEvent
k_eSkilled: ECommendType
k_eSpectateMatch: ECitadelClientAccountEvent
k_eSpectateUser: ECitadelClientAccountEvent
k_eTeamwork: ECommendType
k_eTutorialSkip_Confirmed: ECitadelClientAccountEvent
k_eTutorialSkip_Pressed: ECitadelClientAccountEvent
k_eViewMatchDetails: ECitadelClientAccountEvent
k_eViewedEvents: ECitadelClientAccountEvent
k_eViewedGettingStarted: ECitadelClientAccountEvent
k_eViewedGuidePage: ECitadelClientAccountEvent
k_eViewedGuidePage_15s: ECitadelClientAccountEvent
k_eViewedGuidePage_30s: ECitadelClientAccountEvent
k_eViewedGuidePage_5s: ECitadelClientAccountEvent
k_eViewedGuidePage_60s: ECitadelClientAccountEvent
k_eViewedHeroDetails: ECitadelClientAccountEvent
k_eViewedHeroes: ECitadelClientAccountEvent
k_eViewedPatchNotes: ECitadelClientAccountEvent
k_eViewedProfile: ECitadelClientAccountEvent
k_eViewedSelfProfile: ECitadelClientAccountEvent
k_eViewedSettings_About: ECitadelClientAccountEvent
k_eViewedSettings_Audio: ECitadelClientAccountEvent
k_eViewedSettings_ChatWheel: ECitadelClientAccountEvent
k_eViewedSettings_HotKey: ECitadelClientAccountEvent
k_eViewedSettings_Options: ECitadelClientAccountEvent
k_eViewedSettings_Video: ECitadelClientAccountEvent
k_eViewedSocial: ECitadelClientAccountEvent
k_eViewedWatch: ECitadelClientAccountEvent
k_eWatchedReplay: ECitadelClientAccountEvent

class CMsgAccountBook(_message.Message):
    __slots__ = ["book_id", "book_xp", "spent_xp", "unlocks"]

    class Unlock(_message.Message):
        __slots__ = ["flags", "unlock_id"]
        FLAGS_FIELD_NUMBER: _ClassVar[int]
        UNLOCK_ID_FIELD_NUMBER: _ClassVar[int]
        flags: int
        unlock_id: int
        def __init__(
            self, unlock_id: _Optional[int] = ..., flags: _Optional[int] = ...
        ) -> None: ...

    BOOK_ID_FIELD_NUMBER: _ClassVar[int]
    BOOK_XP_FIELD_NUMBER: _ClassVar[int]
    SPENT_XP_FIELD_NUMBER: _ClassVar[int]
    UNLOCKS_FIELD_NUMBER: _ClassVar[int]
    book_id: int
    book_xp: int
    spent_xp: int
    unlocks: _containers.RepeatedCompositeFieldContainer[CMsgAccountBook.Unlock]
    def __init__(
        self,
        book_id: _Optional[int] = ...,
        book_xp: _Optional[int] = ...,
        spent_xp: _Optional[int] = ...,
        unlocks: _Optional[_Iterable[_Union[CMsgAccountBook.Unlock, _Mapping]]] = ...,
    ) -> None: ...

class CMsgCitadelClientHello(_message.Message):
    __slots__ = ["region_mode"]
    REGION_MODE_FIELD_NUMBER: _ClassVar[int]
    region_mode: _citadel_gcmessages_common_pb2.ECitadelRegionMode
    def __init__(
        self,
        region_mode: _Optional[
            _Union[_citadel_gcmessages_common_pb2.ECitadelRegionMode, str]
        ] = ...,
    ) -> None: ...

class CMsgCitadelProfileCard(_message.Message):
    __slots__ = ["account_id", "ranked_badge_level", "slots"]

    class EStatID(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    class Slot(_message.Message):
        __slots__ = ["hero", "slot_id", "stat"]

        class Hero(_message.Message):
            __slots__ = ["hero_id", "hero_kills", "hero_wins"]
            HERO_ID_FIELD_NUMBER: _ClassVar[int]
            HERO_KILLS_FIELD_NUMBER: _ClassVar[int]
            HERO_WINS_FIELD_NUMBER: _ClassVar[int]
            hero_id: int
            hero_kills: int
            hero_wins: int
            def __init__(
                self,
                hero_id: _Optional[int] = ...,
                hero_wins: _Optional[int] = ...,
                hero_kills: _Optional[int] = ...,
            ) -> None: ...

        class Stat(_message.Message):
            __slots__ = ["stat_id", "stat_score"]
            STAT_ID_FIELD_NUMBER: _ClassVar[int]
            STAT_SCORE_FIELD_NUMBER: _ClassVar[int]
            stat_id: CMsgCitadelProfileCard.EStatID
            stat_score: int
            def __init__(
                self,
                stat_id: _Optional[_Union[CMsgCitadelProfileCard.EStatID, str]] = ...,
                stat_score: _Optional[int] = ...,
            ) -> None: ...

        HERO_FIELD_NUMBER: _ClassVar[int]
        SLOT_ID_FIELD_NUMBER: _ClassVar[int]
        STAT_FIELD_NUMBER: _ClassVar[int]
        hero: CMsgCitadelProfileCard.Slot.Hero
        slot_id: int
        stat: CMsgCitadelProfileCard.Slot.Stat
        def __init__(
            self,
            slot_id: _Optional[int] = ...,
            stat: _Optional[_Union[CMsgCitadelProfileCard.Slot.Stat, _Mapping]] = ...,
            hero: _Optional[_Union[CMsgCitadelProfileCard.Slot.Hero, _Mapping]] = ...,
        ) -> None: ...

    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    RANKED_BADGE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    k_eStat_GamesPlayed: CMsgCitadelProfileCard.EStatID
    k_eStat_Invalid: CMsgCitadelProfileCard.EStatID
    k_eStat_Kills: CMsgCitadelProfileCard.EStatID
    k_eStat_Wins: CMsgCitadelProfileCard.EStatID
    ranked_badge_level: int
    slots: _containers.RepeatedCompositeFieldContainer[CMsgCitadelProfileCard.Slot]
    def __init__(
        self,
        account_id: _Optional[int] = ...,
        slots: _Optional[
            _Iterable[_Union[CMsgCitadelProfileCard.Slot, _Mapping]]
        ] = ...,
        ranked_badge_level: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCBookUnlock(_message.Message):
    __slots__ = ["book_id", "client_version", "expected_cost", "unlock_id"]
    BOOK_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_COST_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    book_id: int
    client_version: int
    expected_cost: int
    unlock_id: int
    def __init__(
        self,
        book_id: _Optional[int] = ...,
        unlock_id: _Optional[int] = ...,
        expected_cost: _Optional[int] = ...,
        client_version: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCBookUnlockResponse(_message.Message):
    __slots__ = ["result", "updated_book"]

    class EResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    RESULT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BOOK_FIELD_NUMBER: _ClassVar[int]
    k_eAlreadyUnlocked: CMsgClientToGCBookUnlockResponse.EResult
    k_eDisabled: CMsgClientToGCBookUnlockResponse.EResult
    k_eInternalError: CMsgClientToGCBookUnlockResponse.EResult
    k_eInvalidFunds: CMsgClientToGCBookUnlockResponse.EResult
    k_eOutOfDateClient: CMsgClientToGCBookUnlockResponse.EResult
    k_eSuccess: CMsgClientToGCBookUnlockResponse.EResult
    k_eTooBusy: CMsgClientToGCBookUnlockResponse.EResult
    result: CMsgClientToGCBookUnlockResponse.EResult
    updated_book: CMsgAccountBook
    def __init__(
        self,
        result: _Optional[_Union[CMsgClientToGCBookUnlockResponse.EResult, str]] = ...,
        updated_book: _Optional[_Union[CMsgAccountBook, _Mapping]] = ...,
    ) -> None: ...

class CMsgClientToGCCommendPlayerFromMatch(_message.Message):
    __slots__ = ["commend_type", "commender_hero_id", "match_id", "target_account_id"]
    COMMENDER_HERO_ID_FIELD_NUMBER: _ClassVar[int]
    COMMEND_TYPE_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    commend_type: ECommendType
    commender_hero_id: int
    match_id: int
    target_account_id: int
    def __init__(
        self,
        match_id: _Optional[int] = ...,
        target_account_id: _Optional[int] = ...,
        commender_hero_id: _Optional[int] = ...,
        commend_type: _Optional[_Union[ECommendType, str]] = ...,
    ) -> None: ...

class CMsgClientToGCCommendPlayerFromMatchResponse(_message.Message):
    __slots__ = ["result"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    RESULT_FIELD_NUMBER: _ClassVar[int]
    k_eDisabled: CMsgClientToGCCommendPlayerFromMatchResponse.EResponse
    k_eInternalError: CMsgClientToGCCommendPlayerFromMatchResponse.EResponse
    k_eRateLimited: CMsgClientToGCCommendPlayerFromMatchResponse.EResponse
    k_eSuccess: CMsgClientToGCCommendPlayerFromMatchResponse.EResponse
    k_eTooBusy: CMsgClientToGCCommendPlayerFromMatchResponse.EResponse
    result: CMsgClientToGCCommendPlayerFromMatchResponse.EResponse
    def __init__(
        self,
        result: _Optional[
            _Union[CMsgClientToGCCommendPlayerFromMatchResponse.EResponse, str]
        ] = ...,
    ) -> None: ...

class CMsgClientToGCDeleteHeroBuild(_message.Message):
    __slots__ = ["author_account_id", "hero_build_id"]
    AUTHOR_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    HERO_BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    author_account_id: int
    hero_build_id: int
    def __init__(
        self,
        author_account_id: _Optional[int] = ...,
        hero_build_id: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCDeleteHeroBuildResponse(_message.Message):
    __slots__ = ["builds_deleted", "response"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    BUILDS_DELETED_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    builds_deleted: int
    k_eInternalError: CMsgClientToGCDeleteHeroBuildResponse.EResponse
    k_eSuccess: CMsgClientToGCDeleteHeroBuildResponse.EResponse
    response: CMsgClientToGCDeleteHeroBuildResponse.EResponse
    def __init__(
        self,
        response: _Optional[
            _Union[CMsgClientToGCDeleteHeroBuildResponse.EResponse, str]
        ] = ...,
        builds_deleted: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCDevAction(_message.Message):
    __slots__ = [
        "account_id",
        "action",
        "bool_value",
        "int_value",
        "str_value",
        "uint_value",
    ]

    class EAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    STR_VALUE_FIELD_NUMBER: _ClassVar[int]
    UINT_VALUE_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    action: CMsgClientToGCDevAction.EAction
    bool_value: bool
    int_value: int
    k_eBanAccount: CMsgClientToGCDevAction.EAction
    k_eBookReset: CMsgClientToGCDevAction.EAction
    k_eBookXPGrant: CMsgClientToGCDevAction.EAction
    k_eForceAccountStorage: CMsgClientToGCDevAction.EAction
    k_eSetDeveloper: CMsgClientToGCDevAction.EAction
    k_eSetHeroStatus: CMsgClientToGCDevAction.EAction
    k_eSetMMR: CMsgClientToGCDevAction.EAction
    k_eSetMMRUncertainty: CMsgClientToGCDevAction.EAction
    k_eSetNewPlayerProgress: CMsgClientToGCDevAction.EAction
    k_eSetPermission: CMsgClientToGCDevAction.EAction
    str_value: str
    uint_value: int
    def __init__(
        self,
        action: _Optional[_Union[CMsgClientToGCDevAction.EAction, str]] = ...,
        account_id: _Optional[int] = ...,
        uint_value: _Optional[int] = ...,
        int_value: _Optional[int] = ...,
        bool_value: bool = ...,
        str_value: _Optional[str] = ...,
    ) -> None: ...

class CMsgClientToGCDevActionResponse(_message.Message):
    __slots__ = ["result"]

    class EResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    RESULT_FIELD_NUMBER: _ClassVar[int]
    k_eInternalError: CMsgClientToGCDevActionResponse.EResult
    k_eInvalidPermission: CMsgClientToGCDevActionResponse.EResult
    k_eInvalidTarget: CMsgClientToGCDevActionResponse.EResult
    k_eSuccess: CMsgClientToGCDevActionResponse.EResult
    result: CMsgClientToGCDevActionResponse.EResult
    def __init__(
        self,
        result: _Optional[_Union[CMsgClientToGCDevActionResponse.EResult, str]] = ...,
    ) -> None: ...

class CMsgClientToGCDevSetMMBias(_message.Message):
    __slots__ = ["account_id", "value"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    value: int
    def __init__(
        self, account_id: _Optional[int] = ..., value: _Optional[int] = ...
    ) -> None: ...

class CMsgClientToGCFindHeroBuilds(_message.Message):
    __slots__ = [
        "author_account_id",
        "hero_build_id",
        "hero_id",
        "language",
        "search_text",
    ]
    AUTHOR_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    HERO_BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    HERO_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TEXT_FIELD_NUMBER: _ClassVar[int]
    author_account_id: int
    hero_build_id: int
    hero_id: int
    language: _containers.RepeatedScalarFieldContainer[int]
    search_text: str
    def __init__(
        self,
        author_account_id: _Optional[int] = ...,
        hero_id: _Optional[int] = ...,
        language: _Optional[_Iterable[int]] = ...,
        search_text: _Optional[str] = ...,
        hero_build_id: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCFindHeroBuildsResponse(_message.Message):
    __slots__ = ["response", "results"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    class HeroBuildResult(_message.Message):
        __slots__ = [
            "hero_build",
            "num_daily_favorites",
            "num_favorites",
            "num_ignores",
            "num_reports",
            "num_weekly_favorites",
            "preference",
            "rollup_category",
        ]
        HERO_BUILD_FIELD_NUMBER: _ClassVar[int]
        NUM_DAILY_FAVORITES_FIELD_NUMBER: _ClassVar[int]
        NUM_FAVORITES_FIELD_NUMBER: _ClassVar[int]
        NUM_IGNORES_FIELD_NUMBER: _ClassVar[int]
        NUM_REPORTS_FIELD_NUMBER: _ClassVar[int]
        NUM_WEEKLY_FAVORITES_FIELD_NUMBER: _ClassVar[int]
        PREFERENCE_FIELD_NUMBER: _ClassVar[int]
        ROLLUP_CATEGORY_FIELD_NUMBER: _ClassVar[int]
        hero_build: CMsgHeroBuild
        num_daily_favorites: int
        num_favorites: int
        num_ignores: int
        num_reports: int
        num_weekly_favorites: int
        preference: CMsgHeroBuildPreference
        rollup_category: int
        def __init__(
            self,
            hero_build: _Optional[_Union[CMsgHeroBuild, _Mapping]] = ...,
            preference: _Optional[_Union[CMsgHeroBuildPreference, _Mapping]] = ...,
            num_favorites: _Optional[int] = ...,
            num_ignores: _Optional[int] = ...,
            num_reports: _Optional[int] = ...,
            num_weekly_favorites: _Optional[int] = ...,
            num_daily_favorites: _Optional[int] = ...,
            rollup_category: _Optional[int] = ...,
        ) -> None: ...

    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    k_eInternalError: CMsgClientToGCFindHeroBuildsResponse.EResponse
    k_eSuccess: CMsgClientToGCFindHeroBuildsResponse.EResponse
    k_eTooBusy: CMsgClientToGCFindHeroBuildsResponse.EResponse
    response: CMsgClientToGCFindHeroBuildsResponse.EResponse
    results: _containers.RepeatedCompositeFieldContainer[
        CMsgClientToGCFindHeroBuildsResponse.HeroBuildResult
    ]
    def __init__(
        self,
        response: _Optional[
            _Union[CMsgClientToGCFindHeroBuildsResponse.EResponse, str]
        ] = ...,
        results: _Optional[
            _Iterable[
                _Union[CMsgClientToGCFindHeroBuildsResponse.HeroBuildResult, _Mapping]
            ]
        ] = ...,
    ) -> None: ...

class CMsgClientToGCGetAccountMatchReports(_message.Message):
    __slots__ = ["match_id"]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    match_id: int
    def __init__(self, match_id: _Optional[int] = ...) -> None: ...

class CMsgClientToGCGetAccountMatchReportsResponse(_message.Message):
    __slots__ = ["commends", "reports", "response"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    class Commend(_message.Message):
        __slots__ = ["account_id"]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        account_id: int
        def __init__(self, account_id: _Optional[int] = ...) -> None: ...

    class Report(_message.Message):
        __slots__ = ["account_id"]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        account_id: int
        def __init__(self, account_id: _Optional[int] = ...) -> None: ...

    COMMENDS_FIELD_NUMBER: _ClassVar[int]
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    commends: _containers.RepeatedCompositeFieldContainer[
        CMsgClientToGCGetAccountMatchReportsResponse.Commend
    ]
    k_eDisabled: CMsgClientToGCGetAccountMatchReportsResponse.EResponse
    k_eInternalError: CMsgClientToGCGetAccountMatchReportsResponse.EResponse
    k_eSuccess: CMsgClientToGCGetAccountMatchReportsResponse.EResponse
    k_eTooBusy: CMsgClientToGCGetAccountMatchReportsResponse.EResponse
    reports: _containers.RepeatedCompositeFieldContainer[
        CMsgClientToGCGetAccountMatchReportsResponse.Report
    ]
    response: CMsgClientToGCGetAccountMatchReportsResponse.EResponse
    def __init__(
        self,
        response: _Optional[
            _Union[CMsgClientToGCGetAccountMatchReportsResponse.EResponse, str]
        ] = ...,
        reports: _Optional[
            _Iterable[
                _Union[CMsgClientToGCGetAccountMatchReportsResponse.Report, _Mapping]
            ]
        ] = ...,
        commends: _Optional[
            _Iterable[
                _Union[CMsgClientToGCGetAccountMatchReportsResponse.Commend, _Mapping]
            ]
        ] = ...,
    ) -> None: ...

class CMsgClientToGCGetAccountStats(_message.Message):
    __slots__ = ["account_id", "dev_access_hint", "friend_access_hint"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    DEV_ACCESS_HINT_FIELD_NUMBER: _ClassVar[int]
    FRIEND_ACCESS_HINT_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    dev_access_hint: bool
    friend_access_hint: bool
    def __init__(
        self,
        account_id: _Optional[int] = ...,
        dev_access_hint: bool = ...,
        friend_access_hint: bool = ...,
    ) -> None: ...

class CMsgClientToGCGetAccountStatsResponse(_message.Message):
    __slots__ = ["result", "stats"]

    class EResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    RESULT_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    k_eDisabled: CMsgClientToGCGetAccountStatsResponse.EResult
    k_eInternalError: CMsgClientToGCGetAccountStatsResponse.EResult
    k_eInvalidPermissions: CMsgClientToGCGetAccountStatsResponse.EResult
    k_eRateLimited: CMsgClientToGCGetAccountStatsResponse.EResult
    k_eSuccess: CMsgClientToGCGetAccountStatsResponse.EResult
    k_eTooBusy: CMsgClientToGCGetAccountStatsResponse.EResult
    result: CMsgClientToGCGetAccountStatsResponse.EResult
    stats: _citadel_gcmessages_common_pb2.CMsgAccountStats
    def __init__(
        self,
        result: _Optional[
            _Union[CMsgClientToGCGetAccountStatsResponse.EResult, str]
        ] = ...,
        stats: _Optional[
            _Union[_citadel_gcmessages_common_pb2.CMsgAccountStats, _Mapping]
        ] = ...,
    ) -> None: ...

class CMsgClientToGCGetActiveMatches(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgClientToGCGetActiveMatchesResponse(_message.Message):
    __slots__ = ["active_matches"]
    ACTIVE_MATCHES_FIELD_NUMBER: _ClassVar[int]
    active_matches: _containers.RepeatedCompositeFieldContainer[CMsgDevMatchInfo]
    def __init__(
        self,
        active_matches: _Optional[_Iterable[_Union[CMsgDevMatchInfo, _Mapping]]] = ...,
    ) -> None: ...

class CMsgClientToGCGetBook(_message.Message):
    __slots__ = ["book_id"]
    BOOK_ID_FIELD_NUMBER: _ClassVar[int]
    book_id: int
    def __init__(self, book_id: _Optional[int] = ...) -> None: ...

class CMsgClientToGCGetBookResponse(_message.Message):
    __slots__ = ["book", "result"]

    class EResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    BOOK_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    book: CMsgAccountBook
    k_eDisabled: CMsgClientToGCGetBookResponse.EResult
    k_eInternalError: CMsgClientToGCGetBookResponse.EResult
    k_eInvalidBook: CMsgClientToGCGetBookResponse.EResult
    k_eSuccess: CMsgClientToGCGetBookResponse.EResult
    k_eTooBusy: CMsgClientToGCGetBookResponse.EResult
    result: CMsgClientToGCGetBookResponse.EResult
    def __init__(
        self,
        result: _Optional[_Union[CMsgClientToGCGetBookResponse.EResult, str]] = ...,
        book: _Optional[_Union[CMsgAccountBook, _Mapping]] = ...,
    ) -> None: ...

class CMsgClientToGCGetDiscordLink(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgClientToGCGetDiscordLinkResponse(_message.Message):
    __slots__ = ["discord_link", "response", "valid_hours"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    DISCORD_LINK_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    VALID_HOURS_FIELD_NUMBER: _ClassVar[int]
    discord_link: str
    k_eAlreadyClaimed: CMsgClientToGCGetDiscordLinkResponse.EResponse
    k_eDisabled: CMsgClientToGCGetDiscordLinkResponse.EResponse
    k_eDiscordTooBusy: CMsgClientToGCGetDiscordLinkResponse.EResponse
    k_eInternalError: CMsgClientToGCGetDiscordLinkResponse.EResponse
    k_eSuccess: CMsgClientToGCGetDiscordLinkResponse.EResponse
    response: CMsgClientToGCGetDiscordLinkResponse.EResponse
    valid_hours: int
    def __init__(
        self,
        response: _Optional[
            _Union[CMsgClientToGCGetDiscordLinkResponse.EResponse, str]
        ] = ...,
        discord_link: _Optional[str] = ...,
        valid_hours: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCGetFriendGameStatus(_message.Message):
    __slots__ = ["include_invited"]
    INCLUDE_INVITED_FIELD_NUMBER: _ClassVar[int]
    include_invited: bool
    def __init__(self, include_invited: bool = ...) -> None: ...

class CMsgClientToGCGetFriendGameStatusResponse(_message.Message):
    __slots__ = [
        "friends_invited",
        "friends_invites_sent",
        "friends_played_game",
        "response",
    ]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    FRIENDS_INVITED_FIELD_NUMBER: _ClassVar[int]
    FRIENDS_INVITES_SENT_FIELD_NUMBER: _ClassVar[int]
    FRIENDS_PLAYED_GAME_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    friends_invited: _containers.RepeatedScalarFieldContainer[int]
    friends_invites_sent: _containers.RepeatedScalarFieldContainer[int]
    friends_played_game: _containers.RepeatedScalarFieldContainer[int]
    k_eDisabled: CMsgClientToGCGetFriendGameStatusResponse.EResponse
    k_eInternalError: CMsgClientToGCGetFriendGameStatusResponse.EResponse
    k_eSuccess: CMsgClientToGCGetFriendGameStatusResponse.EResponse
    k_eTooBusy: CMsgClientToGCGetFriendGameStatusResponse.EResponse
    response: CMsgClientToGCGetFriendGameStatusResponse.EResponse
    def __init__(
        self,
        response: _Optional[
            _Union[CMsgClientToGCGetFriendGameStatusResponse.EResponse, str]
        ] = ...,
        friends_played_game: _Optional[_Iterable[int]] = ...,
        friends_invited: _Optional[_Iterable[int]] = ...,
        friends_invites_sent: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class CMsgClientToGCGetHeroChoice(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgClientToGCGetHeroChoiceResponse(_message.Message):
    __slots__ = ["hero_choice_id", "hero_selections", "result", "select_count"]

    class EResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    class Hero(_message.Message):
        __slots__ = ["hero_id"]
        HERO_ID_FIELD_NUMBER: _ClassVar[int]
        hero_id: int
        def __init__(self, hero_id: _Optional[int] = ...) -> None: ...

    HERO_CHOICE_ID_FIELD_NUMBER: _ClassVar[int]
    HERO_SELECTIONS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    SELECT_COUNT_FIELD_NUMBER: _ClassVar[int]
    hero_choice_id: int
    hero_selections: _containers.RepeatedCompositeFieldContainer[
        CMsgClientToGCGetHeroChoiceResponse.Hero
    ]
    k_eChoiceClosed: CMsgClientToGCGetHeroChoiceResponse.EResult
    k_eDisabled: CMsgClientToGCGetHeroChoiceResponse.EResult
    k_eInternalError: CMsgClientToGCGetHeroChoiceResponse.EResult
    k_eInvalidTarget: CMsgClientToGCGetHeroChoiceResponse.EResult
    k_eNoChoices: CMsgClientToGCGetHeroChoiceResponse.EResult
    k_eSuccess: CMsgClientToGCGetHeroChoiceResponse.EResult
    k_eTooBusy: CMsgClientToGCGetHeroChoiceResponse.EResult
    result: CMsgClientToGCGetHeroChoiceResponse.EResult
    select_count: int
    def __init__(
        self,
        result: _Optional[
            _Union[CMsgClientToGCGetHeroChoiceResponse.EResult, str]
        ] = ...,
        hero_selections: _Optional[
            _Iterable[_Union[CMsgClientToGCGetHeroChoiceResponse.Hero, _Mapping]]
        ] = ...,
        hero_choice_id: _Optional[int] = ...,
        select_count: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCGetMatchHistory(_message.Message):
    __slots__ = ["account_id", "continue_cursor", "ranked_interval"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    RANKED_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    continue_cursor: int
    ranked_interval: int
    def __init__(
        self,
        account_id: _Optional[int] = ...,
        continue_cursor: _Optional[int] = ...,
        ranked_interval: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCGetMatchHistoryResponse(_message.Message):
    __slots__ = ["continue_cursor", "matches", "result"]

    class EResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    class Match(_message.Message):
        __slots__ = [
            "abandoned_time_s",
            "denies",
            "game_mode",
            "hero_id",
            "hero_level",
            "last_hits",
            "match_duration_s",
            "match_id",
            "match_mode",
            "match_result",
            "net_worth",
            "objectives_mask_team0",
            "objectives_mask_team1",
            "player_assists",
            "player_deaths",
            "player_kills",
            "player_team",
            "start_time",
            "team_abandoned",
        ]
        ABANDONED_TIME_S_FIELD_NUMBER: _ClassVar[int]
        DENIES_FIELD_NUMBER: _ClassVar[int]
        GAME_MODE_FIELD_NUMBER: _ClassVar[int]
        HERO_ID_FIELD_NUMBER: _ClassVar[int]
        HERO_LEVEL_FIELD_NUMBER: _ClassVar[int]
        LAST_HITS_FIELD_NUMBER: _ClassVar[int]
        MATCH_DURATION_S_FIELD_NUMBER: _ClassVar[int]
        MATCH_ID_FIELD_NUMBER: _ClassVar[int]
        MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
        MATCH_RESULT_FIELD_NUMBER: _ClassVar[int]
        NET_WORTH_FIELD_NUMBER: _ClassVar[int]
        OBJECTIVES_MASK_TEAM0_FIELD_NUMBER: _ClassVar[int]
        OBJECTIVES_MASK_TEAM1_FIELD_NUMBER: _ClassVar[int]
        PLAYER_ASSISTS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_DEATHS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_KILLS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_TEAM_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        TEAM_ABANDONED_FIELD_NUMBER: _ClassVar[int]
        abandoned_time_s: int
        denies: int
        game_mode: _citadel_gcmessages_common_pb2.ECitadelGameMode
        hero_id: int
        hero_level: int
        last_hits: int
        match_duration_s: int
        match_id: int
        match_mode: _citadel_gcmessages_common_pb2.ECitadelMatchMode
        match_result: int
        net_worth: int
        objectives_mask_team0: int
        objectives_mask_team1: int
        player_assists: int
        player_deaths: int
        player_kills: int
        player_team: _citadel_gcmessages_common_pb2.ECitadelLobbyTeam
        start_time: int
        team_abandoned: bool
        def __init__(
            self,
            match_id: _Optional[int] = ...,
            hero_id: _Optional[int] = ...,
            match_duration_s: _Optional[int] = ...,
            start_time: _Optional[int] = ...,
            match_result: _Optional[int] = ...,
            player_team: _Optional[
                _Union[_citadel_gcmessages_common_pb2.ECitadelLobbyTeam, str]
            ] = ...,
            player_kills: _Optional[int] = ...,
            player_deaths: _Optional[int] = ...,
            player_assists: _Optional[int] = ...,
            last_hits: _Optional[int] = ...,
            denies: _Optional[int] = ...,
            hero_level: _Optional[int] = ...,
            net_worth: _Optional[int] = ...,
            objectives_mask_team0: _Optional[int] = ...,
            objectives_mask_team1: _Optional[int] = ...,
            team_abandoned: bool = ...,
            abandoned_time_s: _Optional[int] = ...,
            match_mode: _Optional[
                _Union[_citadel_gcmessages_common_pb2.ECitadelMatchMode, str]
            ] = ...,
            game_mode: _Optional[
                _Union[_citadel_gcmessages_common_pb2.ECitadelGameMode, str]
            ] = ...,
        ) -> None: ...

    CONTINUE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    MATCHES_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    continue_cursor: int
    k_eResult_InternalError: CMsgClientToGCGetMatchHistoryResponse.EResult
    k_eResult_InvalidPermission: CMsgClientToGCGetMatchHistoryResponse.EResult
    k_eResult_RateLimited: CMsgClientToGCGetMatchHistoryResponse.EResult
    k_eResult_Success: CMsgClientToGCGetMatchHistoryResponse.EResult
    k_eResult_TemporarilyDisabled: CMsgClientToGCGetMatchHistoryResponse.EResult
    k_eResult_TooBusy: CMsgClientToGCGetMatchHistoryResponse.EResult
    matches: _containers.RepeatedCompositeFieldContainer[
        CMsgClientToGCGetMatchHistoryResponse.Match
    ]
    result: CMsgClientToGCGetMatchHistoryResponse.EResult
    def __init__(
        self,
        result: _Optional[
            _Union[CMsgClientToGCGetMatchHistoryResponse.EResult, str]
        ] = ...,
        continue_cursor: _Optional[int] = ...,
        matches: _Optional[
            _Iterable[_Union[CMsgClientToGCGetMatchHistoryResponse.Match, _Mapping]]
        ] = ...,
    ) -> None: ...

class CMsgClientToGCGetMatchMetaData(_message.Message):
    __slots__ = ["match_id", "metadata_salt", "target_account_id"]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_SALT_FIELD_NUMBER: _ClassVar[int]
    TARGET_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    match_id: int
    metadata_salt: int
    target_account_id: int
    def __init__(
        self,
        match_id: _Optional[int] = ...,
        metadata_salt: _Optional[int] = ...,
        target_account_id: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCGetMatchMetaDataResponse(_message.Message):
    __slots__ = [
        "cluster_id",
        "metadata_salt",
        "replay_processing_through",
        "replay_salt",
        "replay_valid_through",
        "result",
    ]

    class EResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_SALT_FIELD_NUMBER: _ClassVar[int]
    REPLAY_PROCESSING_THROUGH_FIELD_NUMBER: _ClassVar[int]
    REPLAY_SALT_FIELD_NUMBER: _ClassVar[int]
    REPLAY_VALID_THROUGH_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    k_eResult_InternalError: CMsgClientToGCGetMatchMetaDataResponse.EResult
    k_eResult_InvalidMatch: CMsgClientToGCGetMatchMetaDataResponse.EResult
    k_eResult_InvalidPermission: CMsgClientToGCGetMatchMetaDataResponse.EResult
    k_eResult_MatchInFlight: CMsgClientToGCGetMatchMetaDataResponse.EResult
    k_eResult_RateLimited: CMsgClientToGCGetMatchMetaDataResponse.EResult
    k_eResult_Success: CMsgClientToGCGetMatchMetaDataResponse.EResult
    k_eResult_TemporarilyDisabled: CMsgClientToGCGetMatchMetaDataResponse.EResult
    k_eResult_TooBusy: CMsgClientToGCGetMatchMetaDataResponse.EResult
    metadata_salt: int
    replay_processing_through: int
    replay_salt: int
    replay_valid_through: int
    result: CMsgClientToGCGetMatchMetaDataResponse.EResult
    def __init__(
        self,
        result: _Optional[
            _Union[CMsgClientToGCGetMatchMetaDataResponse.EResult, str]
        ] = ...,
        replay_salt: _Optional[int] = ...,
        metadata_salt: _Optional[int] = ...,
        replay_valid_through: _Optional[int] = ...,
        cluster_id: _Optional[int] = ...,
        replay_processing_through: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCGetOldHeroBuildData(_message.Message):
    __slots__ = ["author_account_id"]
    AUTHOR_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    author_account_id: int
    def __init__(self, author_account_id: _Optional[int] = ...) -> None: ...

class CMsgClientToGCGetOldHeroBuildDataResponse(_message.Message):
    __slots__ = ["author_account_id", "response", "results"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    class OldBuild(_message.Message):
        __slots__ = ["description", "details", "hero_id", "name"]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        HERO_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        description: str
        details: CMsgClientToGCGetOldHeroBuildDataResponse.OldDetails_V0
        hero_id: int
        name: str
        def __init__(
            self,
            name: _Optional[str] = ...,
            hero_id: _Optional[int] = ...,
            description: _Optional[str] = ...,
            details: _Optional[
                _Union[
                    CMsgClientToGCGetOldHeroBuildDataResponse.OldDetails_V0, _Mapping
                ]
            ] = ...,
        ) -> None: ...

    class OldDetails_V0(_message.Message):
        __slots__ = ["recommended_mod_ability_ids"]
        RECOMMENDED_MOD_ABILITY_IDS_FIELD_NUMBER: _ClassVar[int]
        recommended_mod_ability_ids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(
            self, recommended_mod_ability_ids: _Optional[_Iterable[int]] = ...
        ) -> None: ...

    AUTHOR_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    author_account_id: int
    k_eInternalError: CMsgClientToGCGetOldHeroBuildDataResponse.EResponse
    k_eSuccess: CMsgClientToGCGetOldHeroBuildDataResponse.EResponse
    response: CMsgClientToGCGetOldHeroBuildDataResponse.EResponse
    results: _containers.RepeatedCompositeFieldContainer[
        CMsgClientToGCGetOldHeroBuildDataResponse.OldBuild
    ]
    def __init__(
        self,
        response: _Optional[
            _Union[CMsgClientToGCGetOldHeroBuildDataResponse.EResponse, str]
        ] = ...,
        author_account_id: _Optional[int] = ...,
        results: _Optional[
            _Iterable[
                _Union[CMsgClientToGCGetOldHeroBuildDataResponse.OldBuild, _Mapping]
            ]
        ] = ...,
    ) -> None: ...

class CMsgClientToGCGetProfileCard(_message.Message):
    __slots__ = ["account_id", "dev_access_hint", "friend_access_hint"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    DEV_ACCESS_HINT_FIELD_NUMBER: _ClassVar[int]
    FRIEND_ACCESS_HINT_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    dev_access_hint: bool
    friend_access_hint: bool
    def __init__(
        self,
        account_id: _Optional[int] = ...,
        dev_access_hint: bool = ...,
        friend_access_hint: bool = ...,
    ) -> None: ...

class CMsgClientToGCGrantForumAccess(_message.Message):
    __slots__ = ["email"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class CMsgClientToGCGrantForumAccessResponse(_message.Message):
    __slots__ = ["email", "forum_password", "response", "username"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FORUM_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    email: str
    forum_password: str
    k_eAlreadyClaimed: CMsgClientToGCGrantForumAccessResponse.EResponse
    k_eDisabled: CMsgClientToGCGrantForumAccessResponse.EResponse
    k_eEmailUsed: CMsgClientToGCGrantForumAccessResponse.EResponse
    k_eInternalError: CMsgClientToGCGrantForumAccessResponse.EResponse
    k_eSuccess: CMsgClientToGCGrantForumAccessResponse.EResponse
    response: CMsgClientToGCGrantForumAccessResponse.EResponse
    username: str
    def __init__(
        self,
        response: _Optional[
            _Union[CMsgClientToGCGrantForumAccessResponse.EResponse, str]
        ] = ...,
        email: _Optional[str] = ...,
        username: _Optional[str] = ...,
        forum_password: _Optional[str] = ...,
    ) -> None: ...

class CMsgClientToGCIsInMatchmaking(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgClientToGCIsInMatchmakingResponse(_message.Message):
    __slots__ = ["in_matchmaking"]
    IN_MATCHMAKING_FIELD_NUMBER: _ClassVar[int]
    in_matchmaking: bool
    def __init__(self, in_matchmaking: bool = ...) -> None: ...

class CMsgClientToGCLeaveLobby(_message.Message):
    __slots__ = ["lobby_id"]
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    lobby_id: int
    def __init__(self, lobby_id: _Optional[int] = ...) -> None: ...

class CMsgClientToGCLeaveLobbyResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgClientToGCModeratorRequest(_message.Message):
    __slots__ = ["account_id"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    def __init__(self, account_id: _Optional[int] = ...) -> None: ...

class CMsgClientToGCModeratorRequestResponse(_message.Message):
    __slots__ = ["response_text", "success"]
    RESPONSE_TEXT_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    response_text: _containers.RepeatedScalarFieldContainer[str]
    success: bool
    def __init__(
        self, success: bool = ..., response_text: _Optional[_Iterable[str]] = ...
    ) -> None: ...

class CMsgClientToGCModifyDevAnnouncements(_message.Message):
    __slots__ = [
        "message",
        "operation",
        "patch_version",
        "priority",
        "target_id",
        "title",
        "url",
    ]

    class EOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PATCH_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    k_eCreate: CMsgClientToGCModifyDevAnnouncements.EOperation
    k_eDelete: CMsgClientToGCModifyDevAnnouncements.EOperation
    k_eUpdate: CMsgClientToGCModifyDevAnnouncements.EOperation
    message: str
    operation: CMsgClientToGCModifyDevAnnouncements.EOperation
    patch_version: str
    priority: int
    target_id: int
    title: str
    url: str
    def __init__(
        self,
        operation: _Optional[
            _Union[CMsgClientToGCModifyDevAnnouncements.EOperation, str]
        ] = ...,
        target_id: _Optional[int] = ...,
        priority: _Optional[int] = ...,
        title: _Optional[str] = ...,
        message: _Optional[str] = ...,
        url: _Optional[str] = ...,
        patch_version: _Optional[str] = ...,
    ) -> None: ...

class CMsgClientToGCModifyDevAnnouncementsResponse(_message.Message):
    __slots__ = ["result"]

    class EResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    RESULT_FIELD_NUMBER: _ClassVar[int]
    k_eInternalError: CMsgClientToGCModifyDevAnnouncementsResponse.EResult
    k_eInvalidPermission: CMsgClientToGCModifyDevAnnouncementsResponse.EResult
    k_eInvalidTarget: CMsgClientToGCModifyDevAnnouncementsResponse.EResult
    k_eSuccess: CMsgClientToGCModifyDevAnnouncementsResponse.EResult
    result: CMsgClientToGCModifyDevAnnouncementsResponse.EResult
    def __init__(
        self,
        result: _Optional[
            _Union[CMsgClientToGCModifyDevAnnouncementsResponse.EResult, str]
        ] = ...,
    ) -> None: ...

class CMsgClientToGCPartyAction(_message.Message):
    __slots__ = [
        "action_id",
        "bool_value",
        "party_id",
        "str_value",
        "target_account_id",
        "uint_value",
    ]

    class EAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    STR_VALUE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    UINT_VALUE_FIELD_NUMBER: _ClassVar[int]
    action_id: CMsgClientToGCPartyAction.EAction
    bool_value: bool
    k_eCancelFindMatch: CMsgClientToGCPartyAction.EAction
    k_eCancelInvite: CMsgClientToGCPartyAction.EAction
    k_eEnablePartyCode: CMsgClientToGCPartyAction.EAction
    k_eKickUser: CMsgClientToGCPartyAction.EAction
    k_eSetBotDifficulty: CMsgClientToGCPartyAction.EAction
    k_eSetChatMode: CMsgClientToGCPartyAction.EAction
    k_eSetCheatsEnabled: CMsgClientToGCPartyAction.EAction
    k_eSetDuplicateHeroesEnabled: CMsgClientToGCPartyAction.EAction
    k_eSetMemberTeam: CMsgClientToGCPartyAction.EAction
    k_eSetPlayerSlot: CMsgClientToGCPartyAction.EAction
    k_eSetPlayerType: CMsgClientToGCPartyAction.EAction
    k_eSetPubliclyVisible: CMsgClientToGCPartyAction.EAction
    k_eSetRandomizedLanes: CMsgClientToGCPartyAction.EAction
    k_eSetRegionMode: CMsgClientToGCPartyAction.EAction
    k_eSetSearchKey: CMsgClientToGCPartyAction.EAction
    k_eSetServerRegion: CMsgClientToGCPartyAction.EAction
    k_eShuffleLanes: CMsgClientToGCPartyAction.EAction
    k_eShuffleLobby: CMsgClientToGCPartyAction.EAction
    k_eSwapTeams: CMsgClientToGCPartyAction.EAction
    party_id: int
    str_value: str
    target_account_id: int
    uint_value: int
    def __init__(
        self,
        party_id: _Optional[int] = ...,
        target_account_id: _Optional[int] = ...,
        action_id: _Optional[_Union[CMsgClientToGCPartyAction.EAction, str]] = ...,
        uint_value: _Optional[int] = ...,
        bool_value: bool = ...,
        str_value: _Optional[str] = ...,
    ) -> None: ...

class CMsgClientToGCPartyActionResponse(_message.Message):
    __slots__ = ["result"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    RESULT_FIELD_NUMBER: _ClassVar[int]
    k_eCannotChangeWhileReady: CMsgClientToGCPartyActionResponse.EResponse
    k_eDisabled: CMsgClientToGCPartyActionResponse.EResponse
    k_eInMatch: CMsgClientToGCPartyActionResponse.EResponse
    k_eInMatchMaking: CMsgClientToGCPartyActionResponse.EResponse
    k_eInternalError: CMsgClientToGCPartyActionResponse.EResponse
    k_eInvalidPartyID: CMsgClientToGCPartyActionResponse.EResponse
    k_eInvalidPermissions: CMsgClientToGCPartyActionResponse.EResponse
    k_eInvalidTarget: CMsgClientToGCPartyActionResponse.EResponse
    k_eInvalidValue: CMsgClientToGCPartyActionResponse.EResponse
    k_eRateLimited: CMsgClientToGCPartyActionResponse.EResponse
    k_eSlotTaken: CMsgClientToGCPartyActionResponse.EResponse
    k_eSuccess: CMsgClientToGCPartyActionResponse.EResponse
    k_eTooBusy: CMsgClientToGCPartyActionResponse.EResponse
    result: CMsgClientToGCPartyActionResponse.EResponse
    def __init__(
        self,
        result: _Optional[
            _Union[CMsgClientToGCPartyActionResponse.EResponse, str]
        ] = ...,
    ) -> None: ...

class CMsgClientToGCPartyCreate(_message.Message):
    __slots__ = [
        "disable_party_code",
        "invite_account_id",
        "is_private_lobby",
        "party_mm_info",
        "region_mode",
        "server_search_key",
    ]
    DISABLE_PARTY_CODE_FIELD_NUMBER: _ClassVar[int]
    INVITE_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_PRIVATE_LOBBY_FIELD_NUMBER: _ClassVar[int]
    PARTY_MM_INFO_FIELD_NUMBER: _ClassVar[int]
    REGION_MODE_FIELD_NUMBER: _ClassVar[int]
    SERVER_SEARCH_KEY_FIELD_NUMBER: _ClassVar[int]
    disable_party_code: bool
    invite_account_id: int
    is_private_lobby: bool
    party_mm_info: CMsgPartyMMInfo
    region_mode: _citadel_gcmessages_common_pb2.ECitadelRegionMode
    server_search_key: str
    def __init__(
        self,
        party_mm_info: _Optional[_Union[CMsgPartyMMInfo, _Mapping]] = ...,
        invite_account_id: _Optional[int] = ...,
        disable_party_code: bool = ...,
        is_private_lobby: bool = ...,
        region_mode: _Optional[
            _Union[_citadel_gcmessages_common_pb2.ECitadelRegionMode, str]
        ] = ...,
        server_search_key: _Optional[str] = ...,
    ) -> None: ...

class CMsgClientToGCPartyCreateResponse(_message.Message):
    __slots__ = ["party_id", "result"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    k_eAlreadyInParty: CMsgClientToGCPartyCreateResponse.EResponse
    k_eDisabled: CMsgClientToGCPartyCreateResponse.EResponse
    k_eDurationControlBlocked: CMsgClientToGCPartyCreateResponse.EResponse
    k_eInMatchmaking: CMsgClientToGCPartyCreateResponse.EResponse
    k_eInternalError: CMsgClientToGCPartyCreateResponse.EResponse
    k_eInvalidVersion: CMsgClientToGCPartyCreateResponse.EResponse
    k_eNoRegionPings: CMsgClientToGCPartyCreateResponse.EResponse
    k_eNotFriends: CMsgClientToGCPartyCreateResponse.EResponse
    k_ePlayerDoesntHaveGame: CMsgClientToGCPartyCreateResponse.EResponse
    k_eRateLimited: CMsgClientToGCPartyCreateResponse.EResponse
    k_eRegionInfoNotProvided: CMsgClientToGCPartyCreateResponse.EResponse
    k_eSuccess: CMsgClientToGCPartyCreateResponse.EResponse
    k_eTooBusy: CMsgClientToGCPartyCreateResponse.EResponse
    party_id: int
    result: CMsgClientToGCPartyCreateResponse.EResponse
    def __init__(
        self,
        result: _Optional[
            _Union[CMsgClientToGCPartyCreateResponse.EResponse, str]
        ] = ...,
        party_id: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCPartyInviteUser(_message.Message):
    __slots__ = ["invite_account_id", "party_id"]
    INVITE_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    invite_account_id: int
    party_id: int
    def __init__(
        self, party_id: _Optional[int] = ..., invite_account_id: _Optional[int] = ...
    ) -> None: ...

class CMsgClientToGCPartyInviteUserResponse(_message.Message):
    __slots__ = ["result", "user_online"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    RESULT_FIELD_NUMBER: _ClassVar[int]
    USER_ONLINE_FIELD_NUMBER: _ClassVar[int]
    k_eAlreadyInvited: CMsgClientToGCPartyInviteUserResponse.EResponse
    k_eDisabled: CMsgClientToGCPartyInviteUserResponse.EResponse
    k_eInternalError: CMsgClientToGCPartyInviteUserResponse.EResponse
    k_eInvalidPartyID: CMsgClientToGCPartyInviteUserResponse.EResponse
    k_eInvalidPartyMode: CMsgClientToGCPartyInviteUserResponse.EResponse
    k_eInvalidPermissions: CMsgClientToGCPartyInviteUserResponse.EResponse
    k_eNotFriends: CMsgClientToGCPartyInviteUserResponse.EResponse
    k_ePlayerDoesntHaveGame: CMsgClientToGCPartyInviteUserResponse.EResponse
    k_eRateLimited: CMsgClientToGCPartyInviteUserResponse.EResponse
    k_eSuccess: CMsgClientToGCPartyInviteUserResponse.EResponse
    k_eTooBusy: CMsgClientToGCPartyInviteUserResponse.EResponse
    k_eTooManyInvites: CMsgClientToGCPartyInviteUserResponse.EResponse
    result: CMsgClientToGCPartyInviteUserResponse.EResponse
    user_online: bool
    def __init__(
        self,
        result: _Optional[
            _Union[CMsgClientToGCPartyInviteUserResponse.EResponse, str]
        ] = ...,
        user_online: bool = ...,
    ) -> None: ...

class CMsgClientToGCPartyJoin(_message.Message):
    __slots__ = ["is_rejoin", "party_id", "party_mm_info"]
    IS_REJOIN_FIELD_NUMBER: _ClassVar[int]
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    PARTY_MM_INFO_FIELD_NUMBER: _ClassVar[int]
    is_rejoin: bool
    party_id: int
    party_mm_info: CMsgPartyMMInfo
    def __init__(
        self,
        party_id: _Optional[int] = ...,
        is_rejoin: bool = ...,
        party_mm_info: _Optional[_Union[CMsgPartyMMInfo, _Mapping]] = ...,
    ) -> None: ...

class CMsgClientToGCPartyJoinResponse(_message.Message):
    __slots__ = ["result"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    RESULT_FIELD_NUMBER: _ClassVar[int]
    k_eAlreadyInParty: CMsgClientToGCPartyJoinResponse.EResponse
    k_eDisabled: CMsgClientToGCPartyJoinResponse.EResponse
    k_eDurationControlBlocked: CMsgClientToGCPartyJoinResponse.EResponse
    k_eInMatchmaking: CMsgClientToGCPartyJoinResponse.EResponse
    k_eInternalError: CMsgClientToGCPartyJoinResponse.EResponse
    k_eInvalidCode: CMsgClientToGCPartyJoinResponse.EResponse
    k_eInvalidPartyID: CMsgClientToGCPartyJoinResponse.EResponse
    k_eInvalidPermissions: CMsgClientToGCPartyJoinResponse.EResponse
    k_eInvalidVersion: CMsgClientToGCPartyJoinResponse.EResponse
    k_eNoRegionPings: CMsgClientToGCPartyJoinResponse.EResponse
    k_ePartyFull: CMsgClientToGCPartyJoinResponse.EResponse
    k_ePartyInMatchMaking: CMsgClientToGCPartyJoinResponse.EResponse
    k_eRateLimited: CMsgClientToGCPartyJoinResponse.EResponse
    k_eRegionInfoNotProvided: CMsgClientToGCPartyJoinResponse.EResponse
    k_eSuccess: CMsgClientToGCPartyJoinResponse.EResponse
    k_eTooBusy: CMsgClientToGCPartyJoinResponse.EResponse
    result: CMsgClientToGCPartyJoinResponse.EResponse
    def __init__(
        self,
        result: _Optional[_Union[CMsgClientToGCPartyJoinResponse.EResponse, str]] = ...,
    ) -> None: ...

class CMsgClientToGCPartyJoinViaCode(_message.Message):
    __slots__ = ["join_code", "party_mm_info"]
    JOIN_CODE_FIELD_NUMBER: _ClassVar[int]
    PARTY_MM_INFO_FIELD_NUMBER: _ClassVar[int]
    join_code: int
    party_mm_info: CMsgPartyMMInfo
    def __init__(
        self,
        join_code: _Optional[int] = ...,
        party_mm_info: _Optional[_Union[CMsgPartyMMInfo, _Mapping]] = ...,
    ) -> None: ...

class CMsgClientToGCPartyJoinViaCodeResponse(_message.Message):
    __slots__ = ["party_id", "result"]
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    party_id: int
    result: CMsgClientToGCPartyJoinResponse.EResponse
    def __init__(
        self,
        result: _Optional[_Union[CMsgClientToGCPartyJoinResponse.EResponse, str]] = ...,
        party_id: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCPartyLeave(_message.Message):
    __slots__ = ["party_id"]
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    party_id: int
    def __init__(self, party_id: _Optional[int] = ...) -> None: ...

class CMsgClientToGCPartyLeaveResponse(_message.Message):
    __slots__ = ["result"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    RESULT_FIELD_NUMBER: _ClassVar[int]
    k_eInMatchMaking: CMsgClientToGCPartyLeaveResponse.EResponse
    k_eInternalError: CMsgClientToGCPartyLeaveResponse.EResponse
    k_eNotInParty: CMsgClientToGCPartyLeaveResponse.EResponse
    k_eSuccess: CMsgClientToGCPartyLeaveResponse.EResponse
    result: CMsgClientToGCPartyLeaveResponse.EResponse
    def __init__(
        self,
        result: _Optional[
            _Union[CMsgClientToGCPartyLeaveResponse.EResponse, str]
        ] = ...,
    ) -> None: ...

class CMsgClientToGCPartySetMode(_message.Message):
    __slots__ = [
        "bot_difficulty",
        "dev_server_command",
        "game_mode",
        "match_mode",
        "party_id",
        "ranked_schedule",
        "region_mode",
    ]
    BOT_DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    DEV_SERVER_COMMAND_FIELD_NUMBER: _ClassVar[int]
    GAME_MODE_FIELD_NUMBER: _ClassVar[int]
    MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    RANKED_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    REGION_MODE_FIELD_NUMBER: _ClassVar[int]
    bot_difficulty: _citadel_gcmessages_common_pb2.ECitadelBotDifficulty
    dev_server_command: str
    game_mode: _citadel_gcmessages_common_pb2.ECitadelGameMode
    match_mode: _citadel_gcmessages_common_pb2.ECitadelMatchMode
    party_id: int
    ranked_schedule: int
    region_mode: _citadel_gcmessages_common_pb2.ECitadelRegionMode
    def __init__(
        self,
        party_id: _Optional[int] = ...,
        match_mode: _Optional[
            _Union[_citadel_gcmessages_common_pb2.ECitadelMatchMode, str]
        ] = ...,
        game_mode: _Optional[
            _Union[_citadel_gcmessages_common_pb2.ECitadelGameMode, str]
        ] = ...,
        bot_difficulty: _Optional[
            _Union[_citadel_gcmessages_common_pb2.ECitadelBotDifficulty, str]
        ] = ...,
        dev_server_command: _Optional[str] = ...,
        region_mode: _Optional[
            _Union[_citadel_gcmessages_common_pb2.ECitadelRegionMode, str]
        ] = ...,
        ranked_schedule: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCPartySetModeResponse(_message.Message):
    __slots__ = ["account_id", "result", "time_stamp"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    k_eAlreadyDrafting: CMsgClientToGCPartySetModeResponse.EResponse
    k_eCannotChangeWhileReady: CMsgClientToGCPartySetModeResponse.EResponse
    k_eDisabled: CMsgClientToGCPartySetModeResponse.EResponse
    k_eFiveStacksNotAllowed: CMsgClientToGCPartySetModeResponse.EResponse
    k_eInMatch: CMsgClientToGCPartySetModeResponse.EResponse
    k_eInMatchMaking: CMsgClientToGCPartySetModeResponse.EResponse
    k_eInternalError: CMsgClientToGCPartySetModeResponse.EResponse
    k_eInvalidPartyID: CMsgClientToGCPartySetModeResponse.EResponse
    k_eInvalidPermissions: CMsgClientToGCPartySetModeResponse.EResponse
    k_eInvalidValue: CMsgClientToGCPartySetModeResponse.EResponse
    k_ePlayerBanned: CMsgClientToGCPartySetModeResponse.EResponse
    k_ePlayerPermanentBanned: CMsgClientToGCPartySetModeResponse.EResponse
    k_eRankedMMNotOpen: CMsgClientToGCPartySetModeResponse.EResponse
    k_eRankedNotunlocked: CMsgClientToGCPartySetModeResponse.EResponse
    k_eRateLimited: CMsgClientToGCPartySetModeResponse.EResponse
    k_eSuccess: CMsgClientToGCPartySetModeResponse.EResponse
    k_eTooBusy: CMsgClientToGCPartySetModeResponse.EResponse
    k_eTooFewPlayers: CMsgClientToGCPartySetModeResponse.EResponse
    k_eTooManyHighMMR: CMsgClientToGCPartySetModeResponse.EResponse
    k_eTooManyPlayers: CMsgClientToGCPartySetModeResponse.EResponse
    result: CMsgClientToGCPartySetModeResponse.EResponse
    time_stamp: int
    def __init__(
        self,
        result: _Optional[
            _Union[CMsgClientToGCPartySetModeResponse.EResponse, str]
        ] = ...,
        time_stamp: _Optional[int] = ...,
        account_id: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCPartySetReadyState(_message.Message):
    __slots__ = ["hero_roster", "party_id", "ready_state"]
    HERO_ROSTER_FIELD_NUMBER: _ClassVar[int]
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    READY_STATE_FIELD_NUMBER: _ClassVar[int]
    hero_roster: _citadel_gcmessages_common_pb2.CMsgHeroSelectionMatchInfo
    party_id: int
    ready_state: bool
    def __init__(
        self,
        party_id: _Optional[int] = ...,
        ready_state: bool = ...,
        hero_roster: _Optional[
            _Union[_citadel_gcmessages_common_pb2.CMsgHeroSelectionMatchInfo, _Mapping]
        ] = ...,
    ) -> None: ...

class CMsgClientToGCPartySetReadyStateResponse(_message.Message):
    __slots__ = ["result"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    RESULT_FIELD_NUMBER: _ClassVar[int]
    k_eDisabled: CMsgClientToGCPartySetReadyStateResponse.EResponse
    k_eHeroesNotUnlocked: CMsgClientToGCPartySetReadyStateResponse.EResponse
    k_eInMatch: CMsgClientToGCPartySetReadyStateResponse.EResponse
    k_eInternalError: CMsgClientToGCPartySetReadyStateResponse.EResponse
    k_eInvalidGroupRoster: CMsgClientToGCPartySetReadyStateResponse.EResponse
    k_eInvalidPermissions: CMsgClientToGCPartySetReadyStateResponse.EResponse
    k_eInvalidRoster: CMsgClientToGCPartySetReadyStateResponse.EResponse
    k_eMatchForming: CMsgClientToGCPartySetReadyStateResponse.EResponse
    k_eModeBanned: CMsgClientToGCPartySetReadyStateResponse.EResponse
    k_eModeLocked: CMsgClientToGCPartySetReadyStateResponse.EResponse
    k_eRateLimited: CMsgClientToGCPartySetReadyStateResponse.EResponse
    k_eSuccess: CMsgClientToGCPartySetReadyStateResponse.EResponse
    k_eTooBusy: CMsgClientToGCPartySetReadyStateResponse.EResponse
    result: CMsgClientToGCPartySetReadyStateResponse.EResponse
    def __init__(
        self,
        result: _Optional[
            _Union[CMsgClientToGCPartySetReadyStateResponse.EResponse, str]
        ] = ...,
    ) -> None: ...

class CMsgClientToGCPartyStartMatch(_message.Message):
    __slots__ = ["party_id"]
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    party_id: int
    def __init__(self, party_id: _Optional[int] = ...) -> None: ...

class CMsgClientToGCPartyStartMatchResponse(_message.Message):
    __slots__ = ["account_id", "result"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    k_eCannotSelectRegion: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eDisabled: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eInMatch: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eInMatchmaking: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eInternalError: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eInvalidGroupHeroLineup: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eInvalidHeroLineup: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eInvalidPartyID: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eInvalidPartyMatchMode: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eInvalidPermissions: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eInvalidTeam: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eInvalidVersion: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eMismatchedVersions: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eNotAllPlayersAvailable: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_ePlayerBannedFromMode: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_ePlayersNotReady: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eRankedMMNotOpen: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eSuccess: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eTooBusy: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eTooFewPlayersForMM: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eTooFewPlayersForPrivate: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eTooManyPlayersForMM: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eTooManyPlayersForPrivate: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eTooManyPlayersOnTeam: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eTooManySpectatorsForMM: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eTooManySpectatorsForPrivate: CMsgClientToGCPartyStartMatchResponse.EResponse
    k_eUnassignedPlayers: CMsgClientToGCPartyStartMatchResponse.EResponse
    result: CMsgClientToGCPartyStartMatchResponse.EResponse
    def __init__(
        self,
        result: _Optional[
            _Union[CMsgClientToGCPartyStartMatchResponse.EResponse, str]
        ] = ...,
        account_id: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCPostMatchSurveyResponse(_message.Message):
    __slots__ = ["match_id", "post_match_survey"]

    class PostMatchSurvey(_message.Message):
        __slots__ = ["question_id", "response_value"]
        QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
        RESPONSE_VALUE_FIELD_NUMBER: _ClassVar[int]
        question_id: int
        response_value: int
        def __init__(
            self,
            question_id: _Optional[int] = ...,
            response_value: _Optional[int] = ...,
        ) -> None: ...

    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    POST_MATCH_SURVEY_FIELD_NUMBER: _ClassVar[int]
    match_id: int
    post_match_survey: _containers.RepeatedCompositeFieldContainer[
        CMsgClientToGCPostMatchSurveyResponse.PostMatchSurvey
    ]
    def __init__(
        self,
        post_match_survey: _Optional[
            _Iterable[
                _Union[CMsgClientToGCPostMatchSurveyResponse.PostMatchSurvey, _Mapping]
            ]
        ] = ...,
        match_id: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCRecordClientEvents(_message.Message):
    __slots__ = ["client_run_token", "events"]

    class Event(_message.Message):
        __slots__ = ["client_event_index", "event_data", "event_id", "time_stamp"]
        CLIENT_EVENT_INDEX_FIELD_NUMBER: _ClassVar[int]
        EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
        EVENT_ID_FIELD_NUMBER: _ClassVar[int]
        TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
        client_event_index: int
        event_data: int
        event_id: ECitadelClientAccountEvent
        time_stamp: int
        def __init__(
            self,
            time_stamp: _Optional[int] = ...,
            event_id: _Optional[_Union[ECitadelClientAccountEvent, str]] = ...,
            event_data: _Optional[int] = ...,
            client_event_index: _Optional[int] = ...,
        ) -> None: ...

    CLIENT_RUN_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    client_run_token: int
    events: _containers.RepeatedCompositeFieldContainer[
        CMsgClientToGCRecordClientEvents.Event
    ]
    def __init__(
        self,
        events: _Optional[
            _Iterable[_Union[CMsgClientToGCRecordClientEvents.Event, _Mapping]]
        ] = ...,
        client_run_token: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCRecordClientEventsResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class CMsgClientToGCReplacementSDRTicket(_message.Message):
    __slots__ = ["lobby_id"]
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    lobby_id: int
    def __init__(self, lobby_id: _Optional[int] = ...) -> None: ...

class CMsgClientToGCReplacementSDRTicketResponse(_message.Message):
    __slots__ = ["error_message", "ticket"]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    ticket: bytes
    def __init__(
        self, ticket: _Optional[bytes] = ..., error_message: _Optional[str] = ...
    ) -> None: ...

class CMsgClientToGCReportPlayerFromMatch(_message.Message):
    __slots__ = ["match_id", "report_text", "report_type", "target_account_id"]

    class EReportType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_TEXT_FIELD_NUMBER: _ClassVar[int]
    REPORT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    k_eReport_Cheating: CMsgClientToGCReportPlayerFromMatch.EReportType
    k_eReport_Griefing: CMsgClientToGCReportPlayerFromMatch.EReportType
    k_eReport_LeftMatch: CMsgClientToGCReportPlayerFromMatch.EReportType
    k_eReport_Matchmaking: CMsgClientToGCReportPlayerFromMatch.EReportType
    k_eReport_None: CMsgClientToGCReportPlayerFromMatch.EReportType
    k_eReport_VoiceChat: CMsgClientToGCReportPlayerFromMatch.EReportType
    match_id: int
    report_text: str
    report_type: CMsgClientToGCReportPlayerFromMatch.EReportType
    target_account_id: int
    def __init__(
        self,
        match_id: _Optional[int] = ...,
        target_account_id: _Optional[int] = ...,
        report_type: _Optional[
            _Union[CMsgClientToGCReportPlayerFromMatch.EReportType, str]
        ] = ...,
        report_text: _Optional[str] = ...,
    ) -> None: ...

class CMsgClientToGCReportPlayerFromMatchResponse(_message.Message):
    __slots__ = ["response"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    k_eAlreadyReported: CMsgClientToGCReportPlayerFromMatchResponse.EResponse
    k_eBannedFromReporting: CMsgClientToGCReportPlayerFromMatchResponse.EResponse
    k_eDisabled: CMsgClientToGCReportPlayerFromMatchResponse.EResponse
    k_eInternalError: CMsgClientToGCReportPlayerFromMatchResponse.EResponse
    k_eInvalidPermissions: CMsgClientToGCReportPlayerFromMatchResponse.EResponse
    k_eRateLimited: CMsgClientToGCReportPlayerFromMatchResponse.EResponse
    k_eReportingWindowExpired: CMsgClientToGCReportPlayerFromMatchResponse.EResponse
    k_eSuccess: CMsgClientToGCReportPlayerFromMatchResponse.EResponse
    k_eTooBusy: CMsgClientToGCReportPlayerFromMatchResponse.EResponse
    response: CMsgClientToGCReportPlayerFromMatchResponse.EResponse
    def __init__(
        self,
        response: _Optional[
            _Union[CMsgClientToGCReportPlayerFromMatchResponse.EResponse, str]
        ] = ...,
    ) -> None: ...

class CMsgClientToGCSetNewPlayerProgress(_message.Message):
    __slots__ = ["flag"]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    flag: ECitadelNewPlayerProgressFlag
    def __init__(
        self, flag: _Optional[_Union[ECitadelNewPlayerProgressFlag, str]] = ...
    ) -> None: ...

class CMsgClientToGCSetNewPlayerProgressResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class CMsgClientToGCSetRankedSchedule(_message.Message):
    __slots__ = ["region_mode", "schedule"]
    REGION_MODE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    region_mode: _citadel_gcmessages_common_pb2.ECitadelRegionMode
    schedule: int
    def __init__(
        self,
        region_mode: _Optional[
            _Union[_citadel_gcmessages_common_pb2.ECitadelRegionMode, str]
        ] = ...,
        schedule: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCSetRankedScheduleResponse(_message.Message):
    __slots__ = ["result"]

    class EResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    RESULT_FIELD_NUMBER: _ClassVar[int]
    k_eInCooldown: CMsgClientToGCSetRankedScheduleResponse.EResult
    k_eInternalError: CMsgClientToGCSetRankedScheduleResponse.EResult
    k_eInvalidValue: CMsgClientToGCSetRankedScheduleResponse.EResult
    k_eRankedNotUnlocked: CMsgClientToGCSetRankedScheduleResponse.EResult
    k_eSuccess: CMsgClientToGCSetRankedScheduleResponse.EResult
    result: CMsgClientToGCSetRankedScheduleResponse.EResult
    def __init__(
        self,
        result: _Optional[
            _Union[CMsgClientToGCSetRankedScheduleResponse.EResult, str]
        ] = ...,
    ) -> None: ...

class CMsgClientToGCSetServerConVar(_message.Message):
    __slots__ = ["convar_name", "convar_value", "lobby_id"]
    CONVAR_NAME_FIELD_NUMBER: _ClassVar[int]
    CONVAR_VALUE_FIELD_NUMBER: _ClassVar[int]
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    convar_name: str
    convar_value: str
    lobby_id: int
    def __init__(
        self,
        convar_name: _Optional[str] = ...,
        convar_value: _Optional[str] = ...,
        lobby_id: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCSetServerConVarResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class CMsgClientToGCSpectateLobby(_message.Message):
    __slots__ = [
        "client_platform",
        "client_version",
        "lobby_id",
        "match_id",
        "region_mode",
    ]
    CLIENT_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_MODE_FIELD_NUMBER: _ClassVar[int]
    client_platform: _steammessages_pb2.EGCPlatform
    client_version: int
    lobby_id: int
    match_id: int
    region_mode: _citadel_gcmessages_common_pb2.ECitadelRegionMode
    def __init__(
        self,
        lobby_id: _Optional[int] = ...,
        region_mode: _Optional[
            _Union[_citadel_gcmessages_common_pb2.ECitadelRegionMode, str]
        ] = ...,
        client_version: _Optional[int] = ...,
        client_platform: _Optional[_Union[_steammessages_pb2.EGCPlatform, str]] = ...,
        match_id: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCSpectateLobbyResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: CMsgClientToGCSpectateUserResponse
    def __init__(
        self,
        result: _Optional[_Union[CMsgClientToGCSpectateUserResponse, _Mapping]] = ...,
    ) -> None: ...

class CMsgClientToGCSpectateUser(_message.Message):
    __slots__ = [
        "client_platform",
        "client_version",
        "region_mode",
        "spectate_account_id",
    ]
    CLIENT_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    REGION_MODE_FIELD_NUMBER: _ClassVar[int]
    SPECTATE_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    client_platform: _steammessages_pb2.EGCPlatform
    client_version: int
    region_mode: _citadel_gcmessages_common_pb2.ECitadelRegionMode
    spectate_account_id: int
    def __init__(
        self,
        spectate_account_id: _Optional[int] = ...,
        region_mode: _Optional[
            _Union[_citadel_gcmessages_common_pb2.ECitadelRegionMode, str]
        ] = ...,
        client_version: _Optional[int] = ...,
        client_platform: _Optional[_Union[_steammessages_pb2.EGCPlatform, str]] = ...,
    ) -> None: ...

class CMsgClientToGCSpectateUserResponse(_message.Message):
    __slots__ = [
        "client_broadcast_url",
        "lobby_id",
        "result",
        "sdr_key",
        "server_steam_id",
        "udp_connect_ip",
        "udp_connect_port",
    ]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    CLIENT_BROADCAST_URL_FIELD_NUMBER: _ClassVar[int]
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    SDR_KEY_FIELD_NUMBER: _ClassVar[int]
    SERVER_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    UDP_CONNECT_IP_FIELD_NUMBER: _ClassVar[int]
    UDP_CONNECT_PORT_FIELD_NUMBER: _ClassVar[int]
    client_broadcast_url: str
    k_eDisabled: CMsgClientToGCSpectateUserResponse.EResponse
    k_eDisabledForGame: CMsgClientToGCSpectateUserResponse.EResponse
    k_eDurationControlBlocked: CMsgClientToGCSpectateUserResponse.EResponse
    k_eInternalError: CMsgClientToGCSpectateUserResponse.EResponse
    k_eInvalidClientVersion: CMsgClientToGCSpectateUserResponse.EResponse
    k_eInvalidRegion: CMsgClientToGCSpectateUserResponse.EResponse
    k_eNotFriends: CMsgClientToGCSpectateUserResponse.EResponse
    k_eNotInGame: CMsgClientToGCSpectateUserResponse.EResponse
    k_eRateLimited: CMsgClientToGCSpectateUserResponse.EResponse
    k_eRegionInfoNotProvided: CMsgClientToGCSpectateUserResponse.EResponse
    k_eServerFull: CMsgClientToGCSpectateUserResponse.EResponse
    k_eSuccess: CMsgClientToGCSpectateUserResponse.EResponse
    k_eTooBusy: CMsgClientToGCSpectateUserResponse.EResponse
    lobby_id: int
    result: CMsgClientToGCSpectateUserResponse.EResponse
    sdr_key: bytes
    server_steam_id: int
    udp_connect_ip: int
    udp_connect_port: int
    def __init__(
        self,
        result: _Optional[
            _Union[CMsgClientToGCSpectateUserResponse.EResponse, str]
        ] = ...,
        server_steam_id: _Optional[int] = ...,
        sdr_key: _Optional[bytes] = ...,
        udp_connect_ip: _Optional[int] = ...,
        udp_connect_port: _Optional[int] = ...,
        lobby_id: _Optional[int] = ...,
        client_broadcast_url: _Optional[str] = ...,
    ) -> None: ...

class CMsgClientToGCStartMatchmaking(_message.Message):
    __slots__ = [
        "client_platform",
        "client_version",
        "heroes",
        "match_info",
        "ping_times",
    ]
    CLIENT_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    HEROES_FIELD_NUMBER: _ClassVar[int]
    MATCH_INFO_FIELD_NUMBER: _ClassVar[int]
    PING_TIMES_FIELD_NUMBER: _ClassVar[int]
    client_platform: _steammessages_pb2.EGCPlatform
    client_version: int
    heroes: _citadel_gcmessages_common_pb2.CMsgHeroSelectionMatchInfo
    match_info: _citadel_gcmessages_common_pb2.CMsgStartFindingMatchInfo
    ping_times: _citadel_gcmessages_common_pb2.CMsgRegionPingTimesClient
    def __init__(
        self,
        client_version: _Optional[int] = ...,
        client_platform: _Optional[_Union[_steammessages_pb2.EGCPlatform, str]] = ...,
        match_info: _Optional[
            _Union[_citadel_gcmessages_common_pb2.CMsgStartFindingMatchInfo, _Mapping]
        ] = ...,
        ping_times: _Optional[
            _Union[_citadel_gcmessages_common_pb2.CMsgRegionPingTimesClient, _Mapping]
        ] = ...,
        heroes: _Optional[
            _Union[_citadel_gcmessages_common_pb2.CMsgHeroSelectionMatchInfo, _Mapping]
        ] = ...,
    ) -> None: ...

class CMsgClientToGCStartMatchmakingResponse(_message.Message):
    __slots__ = ["debug_message", "result", "time_stamp"]

    class EResultCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    DEBUG_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    debug_message: str
    k_EResult_AlreadyFindingMatch: CMsgClientToGCStartMatchmakingResponse.EResultCode
    k_EResult_DurationControlBlocked: CMsgClientToGCStartMatchmakingResponse.EResultCode
    k_EResult_HeroesNotUnlocked: CMsgClientToGCStartMatchmakingResponse.EResultCode
    k_EResult_InParty: CMsgClientToGCStartMatchmakingResponse.EResultCode
    k_EResult_InternalError: CMsgClientToGCStartMatchmakingResponse.EResultCode
    k_EResult_InvalidClientVersion: CMsgClientToGCStartMatchmakingResponse.EResultCode
    k_EResult_InvalidHeroSelection: CMsgClientToGCStartMatchmakingResponse.EResultCode
    k_EResult_MatchmakingDisabled: CMsgClientToGCStartMatchmakingResponse.EResultCode
    k_EResult_MatchmakingTooBusy: CMsgClientToGCStartMatchmakingResponse.EResultCode
    k_EResult_ModeBanned: CMsgClientToGCStartMatchmakingResponse.EResultCode
    k_EResult_ModeLocked: CMsgClientToGCStartMatchmakingResponse.EResultCode
    k_EResult_NoRankedWhileCommsBanned: (
        CMsgClientToGCStartMatchmakingResponse.EResultCode
    )
    k_EResult_NoRankedWhileInLowPri: CMsgClientToGCStartMatchmakingResponse.EResultCode
    k_EResult_NoRankedWhileReportBanned: (
        CMsgClientToGCStartMatchmakingResponse.EResultCode
    )
    k_EResult_NoRegionPings: CMsgClientToGCStartMatchmakingResponse.EResultCode
    k_EResult_OK: CMsgClientToGCStartMatchmakingResponse.EResultCode
    k_EResult_PartyMemberInLobby: CMsgClientToGCStartMatchmakingResponse.EResultCode
    k_EResult_PermanentBan: CMsgClientToGCStartMatchmakingResponse.EResultCode
    k_EResult_RankedMMNotOpen: CMsgClientToGCStartMatchmakingResponse.EResultCode
    k_EResult_RankedNotUnlocked: CMsgClientToGCStartMatchmakingResponse.EResultCode
    k_EResult_RegionInfoNotProvided: CMsgClientToGCStartMatchmakingResponse.EResultCode
    result: CMsgClientToGCStartMatchmakingResponse.EResultCode
    time_stamp: int
    def __init__(
        self,
        result: _Optional[
            _Union[CMsgClientToGCStartMatchmakingResponse.EResultCode, str]
        ] = ...,
        time_stamp: _Optional[int] = ...,
        debug_message: _Optional[str] = ...,
    ) -> None: ...

class CMsgClientToGCStopMatchmaking(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CMsgClientToGCStopMatchmakingResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class CMsgClientToGCSubmitPlaytestUser(_message.Message):
    __slots__ = ["location", "target_account_id"]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TARGET_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    location: str
    target_account_id: int
    def __init__(
        self, location: _Optional[str] = ..., target_account_id: _Optional[int] = ...
    ) -> None: ...

class CMsgClientToGCSubmitPlaytestUserResponse(_message.Message):
    __slots__ = ["response"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    eResponse_AlreadyHasGame: CMsgClientToGCSubmitPlaytestUserResponse.EResponse
    eResponse_InternalError: CMsgClientToGCSubmitPlaytestUserResponse.EResponse
    eResponse_InvalidFriend: CMsgClientToGCSubmitPlaytestUserResponse.EResponse
    eResponse_InviteLimitReached: CMsgClientToGCSubmitPlaytestUserResponse.EResponse
    eResponse_LimitedUser: CMsgClientToGCSubmitPlaytestUserResponse.EResponse
    eResponse_NotFriendsLongEnough: CMsgClientToGCSubmitPlaytestUserResponse.EResponse
    eResponse_Success: CMsgClientToGCSubmitPlaytestUserResponse.EResponse
    response: CMsgClientToGCSubmitPlaytestUserResponse.EResponse
    def __init__(
        self,
        response: _Optional[
            _Union[CMsgClientToGCSubmitPlaytestUserResponse.EResponse, str]
        ] = ...,
    ) -> None: ...

class CMsgClientToGCUnlockHero(_message.Message):
    __slots__ = ["hero_choice_id", "hero_ids"]
    HERO_CHOICE_ID_FIELD_NUMBER: _ClassVar[int]
    HERO_IDS_FIELD_NUMBER: _ClassVar[int]
    hero_choice_id: int
    hero_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(
        self,
        hero_ids: _Optional[_Iterable[int]] = ...,
        hero_choice_id: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCUnlockHeroResponse(_message.Message):
    __slots__ = ["result"]

    class EResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    RESULT_FIELD_NUMBER: _ClassVar[int]
    k_eDisabled: CMsgClientToGCUnlockHeroResponse.EResult
    k_eInternalError: CMsgClientToGCUnlockHeroResponse.EResult
    k_eInvalidHero: CMsgClientToGCUnlockHeroResponse.EResult
    k_eOutOfSync: CMsgClientToGCUnlockHeroResponse.EResult
    k_eSuccess: CMsgClientToGCUnlockHeroResponse.EResult
    k_eTooBusy: CMsgClientToGCUnlockHeroResponse.EResult
    result: CMsgClientToGCUnlockHeroResponse.EResult
    def __init__(
        self,
        result: _Optional[_Union[CMsgClientToGCUnlockHeroResponse.EResult, str]] = ...,
    ) -> None: ...

class CMsgClientToGCUpdateAccountSync(_message.Message):
    __slots__ = ["ids", "values"]
    IDS_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[int]
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(
        self,
        ids: _Optional[_Iterable[int]] = ...,
        values: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class CMsgClientToGCUpdateAccountSyncResponse(_message.Message):
    __slots__ = ["result"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    RESULT_FIELD_NUMBER: _ClassVar[int]
    k_eDisabled: CMsgClientToGCUpdateAccountSyncResponse.EResponse
    k_eInternalError: CMsgClientToGCUpdateAccountSyncResponse.EResponse
    k_eInvalidMessage: CMsgClientToGCUpdateAccountSyncResponse.EResponse
    k_eSuccess: CMsgClientToGCUpdateAccountSyncResponse.EResponse
    k_eTooBusy: CMsgClientToGCUpdateAccountSyncResponse.EResponse
    result: CMsgClientToGCUpdateAccountSyncResponse.EResponse
    def __init__(
        self,
        result: _Optional[
            _Union[CMsgClientToGCUpdateAccountSyncResponse.EResponse, str]
        ] = ...,
    ) -> None: ...

class CMsgClientToGCUpdateHeroBuild(_message.Message):
    __slots__ = ["hero_build"]
    HERO_BUILD_FIELD_NUMBER: _ClassVar[int]
    hero_build: CMsgHeroBuild
    def __init__(
        self, hero_build: _Optional[_Union[CMsgHeroBuild, _Mapping]] = ...
    ) -> None: ...

class CMsgClientToGCUpdateHeroBuildPreference(_message.Message):
    __slots__ = ["hero_build_id", "preference"]
    HERO_BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    hero_build_id: int
    preference: CMsgHeroBuildPreference
    def __init__(
        self,
        hero_build_id: _Optional[int] = ...,
        preference: _Optional[_Union[CMsgHeroBuildPreference, _Mapping]] = ...,
    ) -> None: ...

class CMsgClientToGCUpdateHeroBuildPreferenceResponse(_message.Message):
    __slots__ = ["response"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    k_eInternalError: CMsgClientToGCUpdateHeroBuildPreferenceResponse.EResponse
    k_eSuccess: CMsgClientToGCUpdateHeroBuildPreferenceResponse.EResponse
    response: CMsgClientToGCUpdateHeroBuildPreferenceResponse.EResponse
    def __init__(
        self,
        response: _Optional[
            _Union[CMsgClientToGCUpdateHeroBuildPreferenceResponse.EResponse, str]
        ] = ...,
    ) -> None: ...

class CMsgClientToGCUpdateHeroBuildResponse(_message.Message):
    __slots__ = ["hero_build_id", "response", "version"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    HERO_BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    hero_build_id: int
    k_eInternalError: CMsgClientToGCUpdateHeroBuildResponse.EResponse
    k_eSuccess: CMsgClientToGCUpdateHeroBuildResponse.EResponse
    response: CMsgClientToGCUpdateHeroBuildResponse.EResponse
    version: int
    def __init__(
        self,
        response: _Optional[
            _Union[CMsgClientToGCUpdateHeroBuildResponse.EResponse, str]
        ] = ...,
        hero_build_id: _Optional[int] = ...,
        version: _Optional[int] = ...,
    ) -> None: ...

class CMsgClientToGCUpdateRoster(_message.Message):
    __slots__ = ["game_mode", "heroes", "match_mode", "solo_match"]
    GAME_MODE_FIELD_NUMBER: _ClassVar[int]
    HEROES_FIELD_NUMBER: _ClassVar[int]
    MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    SOLO_MATCH_FIELD_NUMBER: _ClassVar[int]
    game_mode: _citadel_gcmessages_common_pb2.ECitadelGameMode
    heroes: _citadel_gcmessages_common_pb2.CMsgHeroSelectionMatchInfo
    match_mode: _citadel_gcmessages_common_pb2.ECitadelMatchMode
    solo_match: bool
    def __init__(
        self,
        heroes: _Optional[
            _Union[_citadel_gcmessages_common_pb2.CMsgHeroSelectionMatchInfo, _Mapping]
        ] = ...,
        game_mode: _Optional[
            _Union[_citadel_gcmessages_common_pb2.ECitadelGameMode, str]
        ] = ...,
        match_mode: _Optional[
            _Union[_citadel_gcmessages_common_pb2.ECitadelMatchMode, str]
        ] = ...,
        solo_match: bool = ...,
    ) -> None: ...

class CMsgClientToGCUpdateRosterResponse(_message.Message):
    __slots__ = ["result"]

    class EResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    RESULT_FIELD_NUMBER: _ClassVar[int]
    k_eDisabled: CMsgClientToGCUpdateRosterResponse.EResponse
    k_eHeroesNotUnlocked: CMsgClientToGCUpdateRosterResponse.EResponse
    k_eInternalError: CMsgClientToGCUpdateRosterResponse.EResponse
    k_eInvalidHeroSelection: CMsgClientToGCUpdateRosterResponse.EResponse
    k_eMMBusy: CMsgClientToGCUpdateRosterResponse.EResponse
    k_eRateLimited: CMsgClientToGCUpdateRosterResponse.EResponse
    k_eSuccess: CMsgClientToGCUpdateRosterResponse.EResponse
    k_eTooBusy: CMsgClientToGCUpdateRosterResponse.EResponse
    result: CMsgClientToGCUpdateRosterResponse.EResponse
    def __init__(
        self,
        result: _Optional[
            _Union[CMsgClientToGCUpdateRosterResponse.EResponse, str]
        ] = ...,
    ) -> None: ...

class CMsgClientToGCUpdateSpectatorStatus(_message.Message):
    __slots__ = ["spectating_lobby_id", "stopped_spectating"]
    SPECTATING_LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    STOPPED_SPECTATING_FIELD_NUMBER: _ClassVar[int]
    spectating_lobby_id: int
    stopped_spectating: bool
    def __init__(
        self, spectating_lobby_id: _Optional[int] = ..., stopped_spectating: bool = ...
    ) -> None: ...

class CMsgClientWelcomeCitadel(_message.Message):
    __slots__ = ["compatibility_version", "currency", "extra_messages", "region_mode"]
    COMPATIBILITY_VERSION_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    EXTRA_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    REGION_MODE_FIELD_NUMBER: _ClassVar[int]
    compatibility_version: int
    currency: int
    extra_messages: _containers.RepeatedCompositeFieldContainer[
        _gcsdk_gcmessages_pb2.CExtraMsgBlock
    ]
    region_mode: _citadel_gcmessages_common_pb2.ECitadelRegionMode
    def __init__(
        self,
        currency: _Optional[int] = ...,
        extra_messages: _Optional[
            _Iterable[_Union[_gcsdk_gcmessages_pb2.CExtraMsgBlock, _Mapping]]
        ] = ...,
        compatibility_version: _Optional[int] = ...,
        region_mode: _Optional[
            _Union[_citadel_gcmessages_common_pb2.ECitadelRegionMode, str]
        ] = ...,
    ) -> None: ...

class CMsgDevMatchInfo(_message.Message):
    __slots__ = [
        "duration_s",
        "game_mode",
        "lobby_id",
        "match_id",
        "match_mode",
        "match_score",
        "net_worth_team_0",
        "net_worth_team_1",
        "objectives_mask_team0",
        "objectives_mask_team1",
        "open_spectator_slots",
        "players",
        "region_mode",
        "spectators",
        "start_time",
        "winning_team",
    ]

    class MatchPlayer(_message.Message):
        __slots__ = ["abandoned", "account_id", "hero_id", "team"]
        ABANDONED_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        HERO_ID_FIELD_NUMBER: _ClassVar[int]
        TEAM_FIELD_NUMBER: _ClassVar[int]
        abandoned: bool
        account_id: int
        hero_id: int
        team: _citadel_gcmessages_common_pb2.ECitadelLobbyTeam
        def __init__(
            self,
            account_id: _Optional[int] = ...,
            team: _Optional[
                _Union[_citadel_gcmessages_common_pb2.ECitadelLobbyTeam, str]
            ] = ...,
            abandoned: bool = ...,
            hero_id: _Optional[int] = ...,
        ) -> None: ...

    DURATION_S_FIELD_NUMBER: _ClassVar[int]
    GAME_MODE_FIELD_NUMBER: _ClassVar[int]
    LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    MATCH_SCORE_FIELD_NUMBER: _ClassVar[int]
    NET_WORTH_TEAM_0_FIELD_NUMBER: _ClassVar[int]
    NET_WORTH_TEAM_1_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVES_MASK_TEAM0_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVES_MASK_TEAM1_FIELD_NUMBER: _ClassVar[int]
    OPEN_SPECTATOR_SLOTS_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    REGION_MODE_FIELD_NUMBER: _ClassVar[int]
    SPECTATORS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    WINNING_TEAM_FIELD_NUMBER: _ClassVar[int]
    duration_s: int
    game_mode: _citadel_gcmessages_common_pb2.ECitadelGameMode
    lobby_id: int
    match_id: int
    match_mode: _citadel_gcmessages_common_pb2.ECitadelMatchMode
    match_score: int
    net_worth_team_0: int
    net_worth_team_1: int
    objectives_mask_team0: int
    objectives_mask_team1: int
    open_spectator_slots: int
    players: _containers.RepeatedCompositeFieldContainer[CMsgDevMatchInfo.MatchPlayer]
    region_mode: _citadel_gcmessages_common_pb2.ECitadelRegionMode
    spectators: int
    start_time: int
    winning_team: _citadel_gcmessages_common_pb2.ECitadelLobbyTeam
    def __init__(
        self,
        start_time: _Optional[int] = ...,
        winning_team: _Optional[
            _Union[_citadel_gcmessages_common_pb2.ECitadelLobbyTeam, str]
        ] = ...,
        match_id: _Optional[int] = ...,
        players: _Optional[
            _Iterable[_Union[CMsgDevMatchInfo.MatchPlayer, _Mapping]]
        ] = ...,
        lobby_id: _Optional[int] = ...,
        net_worth_team_0: _Optional[int] = ...,
        net_worth_team_1: _Optional[int] = ...,
        duration_s: _Optional[int] = ...,
        spectators: _Optional[int] = ...,
        open_spectator_slots: _Optional[int] = ...,
        objectives_mask_team0: _Optional[int] = ...,
        objectives_mask_team1: _Optional[int] = ...,
        match_mode: _Optional[
            _Union[_citadel_gcmessages_common_pb2.ECitadelMatchMode, str]
        ] = ...,
        game_mode: _Optional[
            _Union[_citadel_gcmessages_common_pb2.ECitadelGameMode, str]
        ] = ...,
        match_score: _Optional[int] = ...,
        region_mode: _Optional[
            _Union[_citadel_gcmessages_common_pb2.ECitadelRegionMode, str]
        ] = ...,
    ) -> None: ...

class CMsgGCToClientBookUpdated(_message.Message):
    __slots__ = ["book"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    book: CMsgAccountBook
    def __init__(
        self, book: _Optional[_Union[CMsgAccountBook, _Mapping]] = ...
    ) -> None: ...

class CMsgGCToClientCanRejoinParty(_message.Message):
    __slots__ = ["party_id"]
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    party_id: int
    def __init__(self, party_id: _Optional[int] = ...) -> None: ...

class CMsgGCToClientCommendNotification(_message.Message):
    __slots__ = [
        "commend_type",
        "commender_account_id",
        "commender_hero_id",
        "commender_name",
    ]
    COMMENDER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENDER_HERO_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENDER_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMEND_TYPE_FIELD_NUMBER: _ClassVar[int]
    commend_type: ECommendType
    commender_account_id: int
    commender_hero_id: int
    commender_name: str
    def __init__(
        self,
        commender_account_id: _Optional[int] = ...,
        commender_name: _Optional[str] = ...,
        commender_hero_id: _Optional[int] = ...,
        commend_type: _Optional[_Union[ECommendType, str]] = ...,
    ) -> None: ...

class CMsgGCToClientDevAnnouncements(_message.Message):
    __slots__ = ["announcements"]

    class Announcement(_message.Message):
        __slots__ = [
            "message",
            "patch_version",
            "posted_time",
            "priority",
            "title",
            "unique_id",
            "url",
        ]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        PATCH_VERSION_FIELD_NUMBER: _ClassVar[int]
        POSTED_TIME_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        message: str
        patch_version: str
        posted_time: int
        priority: int
        title: str
        unique_id: int
        url: str
        def __init__(
            self,
            priority: _Optional[int] = ...,
            title: _Optional[str] = ...,
            message: _Optional[str] = ...,
            url: _Optional[str] = ...,
            unique_id: _Optional[int] = ...,
            posted_time: _Optional[int] = ...,
            patch_version: _Optional[str] = ...,
        ) -> None: ...

    ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
    announcements: _containers.RepeatedCompositeFieldContainer[
        CMsgGCToClientDevAnnouncements.Announcement
    ]
    def __init__(
        self,
        announcements: _Optional[
            _Iterable[_Union[CMsgGCToClientDevAnnouncements.Announcement, _Mapping]]
        ] = ...,
    ) -> None: ...

class CMsgGCToClientDevPlaytestStatus(_message.Message):
    __slots__ = [
        "active_match_count",
        "hero_whitelists",
        "is_mm_enabled",
        "locked_heroes",
        "mm_pause_time",
        "party_shared_heroes",
        "regions",
        "valid_client_versions",
    ]

    class HeroWhitelist(_message.Message):
        __slots__ = ["account_ids", "hero_id"]
        ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
        HERO_ID_FIELD_NUMBER: _ClassVar[int]
        account_ids: _containers.RepeatedScalarFieldContainer[int]
        hero_id: int
        def __init__(
            self,
            hero_id: _Optional[int] = ...,
            account_ids: _Optional[_Iterable[int]] = ...,
        ) -> None: ...

    class RegionInfo(_message.Message):
        __slots__ = [
            "available_servers",
            "coop_mm_formation_time",
            "coop_queue_size",
            "region",
            "unranked_queue_size",
        ]
        AVAILABLE_SERVERS_FIELD_NUMBER: _ClassVar[int]
        COOP_MM_FORMATION_TIME_FIELD_NUMBER: _ClassVar[int]
        COOP_QUEUE_SIZE_FIELD_NUMBER: _ClassVar[int]
        REGION_FIELD_NUMBER: _ClassVar[int]
        UNRANKED_QUEUE_SIZE_FIELD_NUMBER: _ClassVar[int]
        available_servers: int
        coop_mm_formation_time: int
        coop_queue_size: int
        region: _citadel_gcmessages_common_pb2.ECitadelRegionMode
        unranked_queue_size: int
        def __init__(
            self,
            region: _Optional[
                _Union[_citadel_gcmessages_common_pb2.ECitadelRegionMode, str]
            ] = ...,
            unranked_queue_size: _Optional[int] = ...,
            coop_queue_size: _Optional[int] = ...,
            coop_mm_formation_time: _Optional[int] = ...,
            available_servers: _Optional[int] = ...,
        ) -> None: ...

    ACTIVE_MATCH_COUNT_FIELD_NUMBER: _ClassVar[int]
    HERO_WHITELISTS_FIELD_NUMBER: _ClassVar[int]
    IS_MM_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LOCKED_HEROES_FIELD_NUMBER: _ClassVar[int]
    MM_PAUSE_TIME_FIELD_NUMBER: _ClassVar[int]
    PARTY_SHARED_HEROES_FIELD_NUMBER: _ClassVar[int]
    REGIONS_FIELD_NUMBER: _ClassVar[int]
    VALID_CLIENT_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    active_match_count: int
    hero_whitelists: _containers.RepeatedCompositeFieldContainer[
        CMsgGCToClientDevPlaytestStatus.HeroWhitelist
    ]
    is_mm_enabled: bool
    locked_heroes: bool
    mm_pause_time: int
    party_shared_heroes: bool
    regions: _containers.RepeatedCompositeFieldContainer[
        CMsgGCToClientDevPlaytestStatus.RegionInfo
    ]
    valid_client_versions: _containers.RepeatedScalarFieldContainer[int]
    def __init__(
        self,
        is_mm_enabled: bool = ...,
        locked_heroes: bool = ...,
        party_shared_heroes: bool = ...,
        hero_whitelists: _Optional[
            _Iterable[_Union[CMsgGCToClientDevPlaytestStatus.HeroWhitelist, _Mapping]]
        ] = ...,
        mm_pause_time: _Optional[int] = ...,
        valid_client_versions: _Optional[_Iterable[int]] = ...,
        active_match_count: _Optional[int] = ...,
        regions: _Optional[
            _Iterable[_Union[CMsgGCToClientDevPlaytestStatus.RegionInfo, _Mapping]]
        ] = ...,
    ) -> None: ...

class CMsgGCToClientMatchmakingStopped(_message.Message):
    __slots__ = ["reason"]

    class EReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    REASON_FIELD_NUMBER: _ClassVar[int]
    k_EResult_FailedReadyUp: CMsgGCToClientMatchmakingStopped.EReason
    k_EResult_Unspecified: CMsgGCToClientMatchmakingStopped.EReason
    k_EResult_VersionUpdated: CMsgGCToClientMatchmakingStopped.EReason
    reason: CMsgGCToClientMatchmakingStopped.EReason
    def __init__(
        self,
        reason: _Optional[_Union[CMsgGCToClientMatchmakingStopped.EReason, str]] = ...,
    ) -> None: ...

class CMsgGCToClientPartyEvent(_message.Message):
    __slots__ = [
        "bytes_data",
        "event",
        "initiator_account_id",
        "party_id",
        "str_data",
        "target_account_id",
        "uint_data",
    ]

    class EEvent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    BYTES_DATA_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    STR_DATA_FIELD_NUMBER: _ClassVar[int]
    TARGET_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    UINT_DATA_FIELD_NUMBER: _ClassVar[int]
    bytes_data: bytes
    event: CMsgGCToClientPartyEvent.EEvent
    initiator_account_id: int
    k_eDeclinedInvite: CMsgGCToClientPartyEvent.EEvent
    k_eDraftEnded_User: CMsgGCToClientPartyEvent.EEvent
    k_eJoinedParty: CMsgGCToClientPartyEvent.EEvent
    k_eLeftParty: CMsgGCToClientPartyEvent.EEvent
    k_eMatchCompleted: CMsgGCToClientPartyEvent.EEvent
    k_eMatchMakingStopped_Cancelled: CMsgGCToClientPartyEvent.EEvent
    k_eMatchMakingStopped_FailedOther: CMsgGCToClientPartyEvent.EEvent
    k_eMatchMakingStopped_NoServerRegion: CMsgGCToClientPartyEvent.EEvent
    k_eMatchMakingStopped_User: CMsgGCToClientPartyEvent.EEvent
    k_eMatchMakingStopped_Version: CMsgGCToClientPartyEvent.EEvent
    k_ePlayerKicked: CMsgGCToClientPartyEvent.EEvent
    k_eStartDraftMMFailed: CMsgGCToClientPartyEvent.EEvent
    party_id: int
    str_data: str
    target_account_id: int
    uint_data: int
    def __init__(
        self,
        party_id: _Optional[int] = ...,
        event: _Optional[_Union[CMsgGCToClientPartyEvent.EEvent, str]] = ...,
        initiator_account_id: _Optional[int] = ...,
        target_account_id: _Optional[int] = ...,
        bytes_data: _Optional[bytes] = ...,
        str_data: _Optional[str] = ...,
        uint_data: _Optional[int] = ...,
    ) -> None: ...

class CMsgGCToClientRankedSchedule(_message.Message):
    __slots__ = [
        "active_interval_end",
        "active_interval_start",
        "active_ranked_interval",
        "schedules",
    ]

    class Schedule(_message.Message):
        __slots__ = ["is_open", "regions", "schedule_id", "weekdays", "weekends"]
        IS_OPEN_FIELD_NUMBER: _ClassVar[int]
        REGIONS_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
        WEEKDAYS_FIELD_NUMBER: _ClassVar[int]
        WEEKENDS_FIELD_NUMBER: _ClassVar[int]
        is_open: bool
        regions: _containers.RepeatedScalarFieldContainer[
            _citadel_gcmessages_common_pb2.ECitadelRegionMode
        ]
        schedule_id: int
        weekdays: _containers.RepeatedCompositeFieldContainer[
            CMsgGCToClientRankedSchedule.TimeRange
        ]
        weekends: _containers.RepeatedCompositeFieldContainer[
            CMsgGCToClientRankedSchedule.TimeRange
        ]
        def __init__(
            self,
            schedule_id: _Optional[int] = ...,
            weekends: _Optional[
                _Iterable[_Union[CMsgGCToClientRankedSchedule.TimeRange, _Mapping]]
            ] = ...,
            weekdays: _Optional[
                _Iterable[_Union[CMsgGCToClientRankedSchedule.TimeRange, _Mapping]]
            ] = ...,
            is_open: bool = ...,
            regions: _Optional[
                _Iterable[
                    _Union[_citadel_gcmessages_common_pb2.ECitadelRegionMode, str]
                ]
            ] = ...,
        ) -> None: ...

    class TimeRange(_message.Message):
        __slots__ = ["end_time", "start_time"]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        end_time: int
        start_time: int
        def __init__(
            self, start_time: _Optional[int] = ..., end_time: _Optional[int] = ...
        ) -> None: ...

    ACTIVE_INTERVAL_END_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_INTERVAL_START_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_RANKED_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    active_interval_end: int
    active_interval_start: int
    active_ranked_interval: int
    schedules: _containers.RepeatedCompositeFieldContainer[
        CMsgGCToClientRankedSchedule.Schedule
    ]
    def __init__(
        self,
        schedules: _Optional[
            _Iterable[_Union[CMsgGCToClientRankedSchedule.Schedule, _Mapping]]
        ] = ...,
        active_ranked_interval: _Optional[int] = ...,
        active_interval_start: _Optional[int] = ...,
        active_interval_end: _Optional[int] = ...,
    ) -> None: ...

class CMsgGCToClientSDRTicket(_message.Message):
    __slots__ = ["ticket"]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket: bytes
    def __init__(self, ticket: _Optional[bytes] = ...) -> None: ...

class CMsgHeroBuild(_message.Message):
    __slots__ = [
        "author_account_id",
        "description",
        "details",
        "hero_build_id",
        "hero_id",
        "language",
        "last_updated_timestamp",
        "name",
        "origin_build_id",
        "version",
    ]

    class AbilityOrder(_message.Message):
        __slots__ = ["currency_changes"]
        CURRENCY_CHANGES_FIELD_NUMBER: _ClassVar[int]
        currency_changes: _containers.RepeatedCompositeFieldContainer[
            CMsgHeroBuild.CurrencyChange
        ]
        def __init__(
            self,
            currency_changes: _Optional[
                _Iterable[_Union[CMsgHeroBuild.CurrencyChange, _Mapping]]
            ] = ...,
        ) -> None: ...

    class BuildModCategory(_message.Message):
        __slots__ = ["description", "height", "mods", "name", "width"]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        MODS_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        description: str
        height: float
        mods: _containers.RepeatedCompositeFieldContainer[CMsgHeroBuild.BuildModEntry]
        name: str
        width: float
        def __init__(
            self,
            mods: _Optional[
                _Iterable[_Union[CMsgHeroBuild.BuildModEntry, _Mapping]]
            ] = ...,
            name: _Optional[str] = ...,
            description: _Optional[str] = ...,
            width: _Optional[float] = ...,
            height: _Optional[float] = ...,
        ) -> None: ...

    class BuildModEntry(_message.Message):
        __slots__ = ["ability_id", "annotation"]
        ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
        ANNOTATION_FIELD_NUMBER: _ClassVar[int]
        ability_id: int
        annotation: str
        def __init__(
            self, ability_id: _Optional[int] = ..., annotation: _Optional[str] = ...
        ) -> None: ...

    class CurrencyChange(_message.Message):
        __slots__ = ["ability_id", "annotation", "currency_type", "delta"]
        ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
        ANNOTATION_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_TYPE_FIELD_NUMBER: _ClassVar[int]
        DELTA_FIELD_NUMBER: _ClassVar[int]
        ability_id: int
        annotation: str
        currency_type: int
        delta: int
        def __init__(
            self,
            ability_id: _Optional[int] = ...,
            currency_type: _Optional[int] = ...,
            delta: _Optional[int] = ...,
            annotation: _Optional[str] = ...,
        ) -> None: ...

    class Details_V0(_message.Message):
        __slots__ = ["ability_order", "mod_categories"]
        ABILITY_ORDER_FIELD_NUMBER: _ClassVar[int]
        MOD_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
        ability_order: CMsgHeroBuild.AbilityOrder
        mod_categories: _containers.RepeatedCompositeFieldContainer[
            CMsgHeroBuild.BuildModCategory
        ]
        def __init__(
            self,
            mod_categories: _Optional[
                _Iterable[_Union[CMsgHeroBuild.BuildModCategory, _Mapping]]
            ] = ...,
            ability_order: _Optional[
                _Union[CMsgHeroBuild.AbilityOrder, _Mapping]
            ] = ...,
        ) -> None: ...

    AUTHOR_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    HERO_BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    HERO_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    author_account_id: int
    description: str
    details: CMsgHeroBuild.Details_V0
    hero_build_id: int
    hero_id: int
    language: int
    last_updated_timestamp: int
    name: str
    origin_build_id: int
    version: int
    def __init__(
        self,
        hero_build_id: _Optional[int] = ...,
        hero_id: _Optional[int] = ...,
        author_account_id: _Optional[int] = ...,
        last_updated_timestamp: _Optional[int] = ...,
        name: _Optional[str] = ...,
        description: _Optional[str] = ...,
        language: _Optional[int] = ...,
        version: _Optional[int] = ...,
        origin_build_id: _Optional[int] = ...,
        details: _Optional[_Union[CMsgHeroBuild.Details_V0, _Mapping]] = ...,
    ) -> None: ...

class CMsgHeroBuildPreference(_message.Message):
    __slots__ = ["favorited", "ignored", "reported"]
    FAVORITED_FIELD_NUMBER: _ClassVar[int]
    IGNORED_FIELD_NUMBER: _ClassVar[int]
    REPORTED_FIELD_NUMBER: _ClassVar[int]
    favorited: bool
    ignored: bool
    reported: bool
    def __init__(
        self, favorited: bool = ..., ignored: bool = ..., reported: bool = ...
    ) -> None: ...

class CMsgPartyMMInfo(_message.Message):
    __slots__ = ["client_version", "ping_times", "platform", "region_mode"]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    PING_TIMES_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    REGION_MODE_FIELD_NUMBER: _ClassVar[int]
    client_version: int
    ping_times: _citadel_gcmessages_common_pb2.CMsgRegionPingTimesClient
    platform: _steammessages_pb2.EGCPlatform
    region_mode: _citadel_gcmessages_common_pb2.ECitadelRegionMode
    def __init__(
        self,
        platform: _Optional[_Union[_steammessages_pb2.EGCPlatform, str]] = ...,
        ping_times: _Optional[
            _Union[_citadel_gcmessages_common_pb2.CMsgRegionPingTimesClient, _Mapping]
        ] = ...,
        client_version: _Optional[int] = ...,
        region_mode: _Optional[
            _Union[_citadel_gcmessages_common_pb2.ECitadelRegionMode, str]
        ] = ...,
    ) -> None: ...

class CSOAccountHeroInfo(_message.Message):
    __slots__ = ["account_id", "hero_id", "kills", "status", "wins"]

    class EHeroStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    HERO_ID_FIELD_NUMBER: _ClassVar[int]
    KILLS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    WINS_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    hero_id: int
    k_eLocked: CSOAccountHeroInfo.EHeroStatus
    k_eOwned: CSOAccountHeroInfo.EHeroStatus
    kills: int
    status: CSOAccountHeroInfo.EHeroStatus
    wins: int
    def __init__(
        self,
        account_id: _Optional[int] = ...,
        hero_id: _Optional[int] = ...,
        status: _Optional[_Union[CSOAccountHeroInfo.EHeroStatus, str]] = ...,
        wins: _Optional[int] = ...,
        kills: _Optional[int] = ...,
    ) -> None: ...

class CSOAccountSyncStorage(_message.Message):
    __slots__ = ["account_id", "id", "value"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    id: int
    value: int
    def __init__(
        self,
        account_id: _Optional[int] = ...,
        id: _Optional[int] = ...,
        value: _Optional[int] = ...,
    ) -> None: ...

class CSOGameAccountClient(_message.Message):
    __slots__ = [
        "account_id",
        "comms_ban_until",
        "flags",
        "hero_unlock_credits",
        "kills",
        "losses",
        "low_priority_games_remaining",
        "mm_ban_until",
        "most_played_hero_id",
        "new_player_progress",
        "permissions",
        "ranked_badge_detail",
        "ranked_badge_interval",
        "ranked_badge_level",
        "ranked_interval",
        "ranked_matches",
        "ranked_schedule",
        "ranked_schedule_time",
        "report_ban_until",
        "wins",
    ]

    class EFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMS_BAN_UNTIL_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    HERO_UNLOCK_CREDITS_FIELD_NUMBER: _ClassVar[int]
    KILLS_FIELD_NUMBER: _ClassVar[int]
    LOSSES_FIELD_NUMBER: _ClassVar[int]
    LOW_PRIORITY_GAMES_REMAINING_FIELD_NUMBER: _ClassVar[int]
    MM_BAN_UNTIL_FIELD_NUMBER: _ClassVar[int]
    MOST_PLAYED_HERO_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_PLAYER_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    RANKED_BADGE_DETAIL_FIELD_NUMBER: _ClassVar[int]
    RANKED_BADGE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    RANKED_BADGE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    RANKED_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    RANKED_MATCHES_FIELD_NUMBER: _ClassVar[int]
    RANKED_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    RANKED_SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
    REPORT_BAN_UNTIL_FIELD_NUMBER: _ClassVar[int]
    WINS_FIELD_NUMBER: _ClassVar[int]
    account_id: int
    comms_ban_until: int
    flags: int
    hero_unlock_credits: int
    k_eAccountBanned: CSOGameAccountClient.EFlags
    k_eClaimedDiscordLink: CSOGameAccountClient.EFlags
    k_eClaimedForum: CSOGameAccountClient.EFlags
    k_eDeveloper: CSOGameAccountClient.EFlags
    k_eExternalModerator: CSOGameAccountClient.EFlags
    k_eGotInitialHeroes: CSOGameAccountClient.EFlags
    kills: int
    losses: int
    low_priority_games_remaining: int
    mm_ban_until: int
    most_played_hero_id: int
    new_player_progress: int
    permissions: int
    ranked_badge_detail: int
    ranked_badge_interval: int
    ranked_badge_level: int
    ranked_interval: int
    ranked_matches: int
    ranked_schedule: int
    ranked_schedule_time: int
    report_ban_until: int
    wins: int
    def __init__(
        self,
        account_id: _Optional[int] = ...,
        flags: _Optional[int] = ...,
        wins: _Optional[int] = ...,
        losses: _Optional[int] = ...,
        kills: _Optional[int] = ...,
        most_played_hero_id: _Optional[int] = ...,
        permissions: _Optional[int] = ...,
        new_player_progress: _Optional[int] = ...,
        hero_unlock_credits: _Optional[int] = ...,
        mm_ban_until: _Optional[int] = ...,
        comms_ban_until: _Optional[int] = ...,
        low_priority_games_remaining: _Optional[int] = ...,
        report_ban_until: _Optional[int] = ...,
        ranked_badge_level: _Optional[int] = ...,
        ranked_badge_detail: _Optional[int] = ...,
        ranked_badge_interval: _Optional[int] = ...,
        ranked_matches: _Optional[int] = ...,
        ranked_interval: _Optional[int] = ...,
        ranked_schedule: _Optional[int] = ...,
        ranked_schedule_time: _Optional[int] = ...,
    ) -> None: ...

class EGCCitadelClientMessages(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ECitadelAccountPermissionFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ECitadelNewPlayerProgressFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EProfileCardSlotType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ECitadelClientAccountEvent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ECommendType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
