from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor
NETWORK_CONNECTION_DETAIL_TOKEN_FIELD_NUMBER: _ClassVar[int]
NETWORK_CONNECTION_TOKEN_FIELD_NUMBER: _ClassVar[int]
NETWORK_DISCONNECT_BADDELTATICK: ENetworkDisconnectionReason
NETWORK_DISCONNECT_BADRELAYPASSWORD: ENetworkDisconnectionReason
NETWORK_DISCONNECT_BADSPECTATORPASSWORD: ENetworkDisconnectionReason
NETWORK_DISCONNECT_BAD_SERVER_PASSWORD: ENetworkDisconnectionReason
NETWORK_DISCONNECT_BANADDED: ENetworkDisconnectionReason
NETWORK_DISCONNECT_CLIENT_CONSISTENCY_FAIL: ENetworkDisconnectionReason
NETWORK_DISCONNECT_CLIENT_DIFFERENT_MAP: ENetworkDisconnectionReason
NETWORK_DISCONNECT_CLIENT_NO_MAP: ENetworkDisconnectionReason
NETWORK_DISCONNECT_CLIENT_UNABLE_TO_CRC_MAP: ENetworkDisconnectionReason
NETWORK_DISCONNECT_CONNECTION_FAILURE: ENetworkDisconnectionReason
NETWORK_DISCONNECT_CONNECT_REQUEST_TIMEDOUT: ENetworkDisconnectionReason
NETWORK_DISCONNECT_CREATE_SERVER_FAILED: ENetworkDisconnectionReason
NETWORK_DISCONNECT_DELTAENTMSG_OVERFLOW: ENetworkDisconnectionReason
NETWORK_DISCONNECT_DIFFERENTCLASSTABLES: ENetworkDisconnectionReason
NETWORK_DISCONNECT_DIRECT_CONNECT_RESERVATION: ENetworkDisconnectionReason
NETWORK_DISCONNECT_DISCONNECTED: ENetworkDisconnectionReason
NETWORK_DISCONNECT_DISCONNECT_BY_SERVER: ENetworkDisconnectionReason
NETWORK_DISCONNECT_DISCONNECT_BY_USER: ENetworkDisconnectionReason
NETWORK_DISCONNECT_EXITING: ENetworkDisconnectionReason
NETWORK_DISCONNECT_HLTVDIRECT: ENetworkDisconnectionReason
NETWORK_DISCONNECT_HLTVRESTRICTED: ENetworkDisconnectionReason
NETWORK_DISCONNECT_HLTVSTOP: ENetworkDisconnectionReason
NETWORK_DISCONNECT_HLTVUNAVAILABLE: ENetworkDisconnectionReason
NETWORK_DISCONNECT_HOST_ENDGAME: ENetworkDisconnectionReason
NETWORK_DISCONNECT_INTERNAL_ERROR: ENetworkDisconnectionReason
NETWORK_DISCONNECT_INVALID: ENetworkDisconnectionReason
NETWORK_DISCONNECT_INVALID_MESSAGE_ERROR: ENetworkDisconnectionReason
NETWORK_DISCONNECT_KICKBANADDED: ENetworkDisconnectionReason
NETWORK_DISCONNECT_KICKED: ENetworkDisconnectionReason
NETWORK_DISCONNECT_KICKED_COMPETITIVECOOLDOWN: ENetworkDisconnectionReason
NETWORK_DISCONNECT_KICKED_CONVICTEDACCOUNT: ENetworkDisconnectionReason
NETWORK_DISCONNECT_KICKED_HOSTAGEKILLING: ENetworkDisconnectionReason
NETWORK_DISCONNECT_KICKED_IDLE: ENetworkDisconnectionReason
NETWORK_DISCONNECT_KICKED_INPUTAUTOMATION: ENetworkDisconnectionReason
NETWORK_DISCONNECT_KICKED_NOSTEAMLOGIN: ENetworkDisconnectionReason
NETWORK_DISCONNECT_KICKED_NOSTEAMTICKET: ENetworkDisconnectionReason
NETWORK_DISCONNECT_KICKED_SUICIDE: ENetworkDisconnectionReason
NETWORK_DISCONNECT_KICKED_TEAMHURTING: ENetworkDisconnectionReason
NETWORK_DISCONNECT_KICKED_TEAMKILLING: ENetworkDisconnectionReason
NETWORK_DISCONNECT_KICKED_TK_START: ENetworkDisconnectionReason
NETWORK_DISCONNECT_KICKED_UNTRUSTEDACCOUNT: ENetworkDisconnectionReason
NETWORK_DISCONNECT_KICKED_VOTEDOFF: ENetworkDisconnectionReason
NETWORK_DISCONNECT_LEAVINGSPLIT: ENetworkDisconnectionReason
NETWORK_DISCONNECT_LOCALPROBLEM_HOSTEDSERVERPRIMARYRELAY: ENetworkDisconnectionReason
NETWORK_DISCONNECT_LOCALPROBLEM_MANYRELAYS: ENetworkDisconnectionReason
NETWORK_DISCONNECT_LOCALPROBLEM_NETWORKCONFIG: ENetworkDisconnectionReason
NETWORK_DISCONNECT_LOCALPROBLEM_OTHER: ENetworkDisconnectionReason
NETWORK_DISCONNECT_LOOPDEACTIVATE: ENetworkDisconnectionReason
NETWORK_DISCONNECT_LOOPSHUTDOWN: ENetworkDisconnectionReason
NETWORK_DISCONNECT_LOOP_LEVELLOAD_ACTIVATE: ENetworkDisconnectionReason
NETWORK_DISCONNECT_LOST: ENetworkDisconnectionReason
NETWORK_DISCONNECT_MESSAGE_PARSE_ERROR: ENetworkDisconnectionReason
NETWORK_DISCONNECT_NOMORESPLITS: ENetworkDisconnectionReason
NETWORK_DISCONNECT_NOSPECTATORS: ENetworkDisconnectionReason
NETWORK_DISCONNECT_NO_PEER_GROUP_HANDLERS: ENetworkDisconnectionReason
NETWORK_DISCONNECT_OVERFLOW: ENetworkDisconnectionReason
NETWORK_DISCONNECT_PURESERVER_CLIENTEXTRA: ENetworkDisconnectionReason
NETWORK_DISCONNECT_PURESERVER_MISMATCH: ENetworkDisconnectionReason
NETWORK_DISCONNECT_RECONNECTION: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECTED_BY_GAME: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_BACKGROUND_MAP: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_BADCHALLENGE: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_BADPASSWORD: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_BANNED: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_CONNECT_FROM_LOBBY: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_FAILEDCHANNEL: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_HIDDEN_GAME: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_INVALIDCERTLEN: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_INVALIDCONNECTION: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_INVALIDKEYLENGTH: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_INVALIDRESERVATION: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_INVALIDSTEAMCERTLEN: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_LANRESTRICT: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_NEWPROTOCOL: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_NOLOBBY: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_OLDPROTOCOL: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_RESERVED_FOR_LOBBY: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_SERVERAUTHDISABLED: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_SERVERCDKEYAUTHINVALID: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_SERVERFULL: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_SINGLE_PLAYER: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REJECT_STEAM: ENetworkDisconnectionReason
NETWORK_DISCONNECT_RELIABLEOVERFLOW: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REMOTE_BADCRYPT: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REMOTE_CERTNOTTRUSTED: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REMOTE_OTHER: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REMOTE_TIMEOUT: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REMOTE_TIMEOUT_CONNECTING: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REPLAY_INCOMPATIBLE: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REQUEST_HOSTSTATE_HLTVRELAY: ENetworkDisconnectionReason
NETWORK_DISCONNECT_REQUEST_HOSTSTATE_IDLE: ENetworkDisconnectionReason
NETWORK_DISCONNECT_SERVERINFO_OVERFLOW: ENetworkDisconnectionReason
NETWORK_DISCONNECT_SERVER_INCOMPATIBLE: ENetworkDisconnectionReason
NETWORK_DISCONNECT_SERVER_REQUIRES_STEAM: ENetworkDisconnectionReason
NETWORK_DISCONNECT_SERVER_SHUTDOWN: ENetworkDisconnectionReason
NETWORK_DISCONNECT_SHUTDOWN: ENetworkDisconnectionReason
NETWORK_DISCONNECT_SNAPSHOTERROR: ENetworkDisconnectionReason
NETWORK_DISCONNECT_SNAPSHOTOVERFLOW: ENetworkDisconnectionReason
NETWORK_DISCONNECT_SOUNDSMSG_OVERFLOW: ENetworkDisconnectionReason
NETWORK_DISCONNECT_STEAM_AUTHALREADYUSED: ENetworkDisconnectionReason
NETWORK_DISCONNECT_STEAM_AUTHCANCELLED: ENetworkDisconnectionReason
NETWORK_DISCONNECT_STEAM_AUTHINVALID: ENetworkDisconnectionReason
NETWORK_DISCONNECT_STEAM_BANNED: ENetworkDisconnectionReason
NETWORK_DISCONNECT_STEAM_DENY_BAD_ANTI_CHEAT: ENetworkDisconnectionReason
NETWORK_DISCONNECT_STEAM_DENY_MISC: ENetworkDisconnectionReason
NETWORK_DISCONNECT_STEAM_DROPPED: ENetworkDisconnectionReason
NETWORK_DISCONNECT_STEAM_INUSE: ENetworkDisconnectionReason
NETWORK_DISCONNECT_STEAM_LOGGED_IN_ELSEWHERE: ENetworkDisconnectionReason
NETWORK_DISCONNECT_STEAM_LOGON: ENetworkDisconnectionReason
NETWORK_DISCONNECT_STEAM_OWNERSHIP: ENetworkDisconnectionReason
NETWORK_DISCONNECT_STEAM_TICKET: ENetworkDisconnectionReason
NETWORK_DISCONNECT_STEAM_VACBANSTATE: ENetworkDisconnectionReason
NETWORK_DISCONNECT_STEAM_VAC_CHECK_TIMEDOUT: ENetworkDisconnectionReason
NETWORK_DISCONNECT_STRINGTABLEMSG_OVERFLOW: ENetworkDisconnectionReason
NETWORK_DISCONNECT_TEMPENTMSG_OVERFLOW: ENetworkDisconnectionReason
NETWORK_DISCONNECT_TICKMSG_OVERFLOW: ENetworkDisconnectionReason
NETWORK_DISCONNECT_TIMEDOUT: ENetworkDisconnectionReason
NETWORK_DISCONNECT_UNUSUAL: ENetworkDisconnectionReason
NETWORK_DISCONNECT_USERCMD: ENetworkDisconnectionReason
network_connection_detail_token: _descriptor.FieldDescriptor
network_connection_token: _descriptor.FieldDescriptor

class ENetworkDisconnectionReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []