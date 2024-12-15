import logging
import uuid
from base64 import b64decode, b64encode
from datetime import datetime
from typing import TypeVar

import requests
from cachetools.func import ttl_cache
from discord_webhook import DiscordWebhook
from fastapi import HTTPException, Security
from fastapi.openapi.models import APIKey, APIKeyIn
from fastapi.security.api_key import APIKeyBase
from google.protobuf.message import Message
from requests import HTTPError
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.status import (
    HTTP_403_FORBIDDEN,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from starlette.types import ASGIApp, Receive, Scope, Send

from deadlock_data_api.conf import CONFIG
from deadlock_data_api.globs import postgres_conn, redis_conn, s3_cache_conn

LOGGER = logging.getLogger(__name__)

STEAM_ID_64_IDENT = 76561197960265728


def send_webhook_message(message: str):
    if not CONFIG.discord_webhook_url:
        LOGGER.warning("No Discord webhook URL provided")
        return
    webhook = DiscordWebhook(url=CONFIG.discord_webhook_url, content=message)
    LOGGER.info(f"Sending webhook message: {message}")
    webhook.execute()


def is_valid_uuid(value: str | None) -> bool:
    if value is None:
        return False
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        LOGGER.warning(f"Invalid UUID: {value}")
        return False
    except TypeError:
        LOGGER.warning(f"Invalid UUID: {value}")
        return False


R = TypeVar("R", bound=Message)


def call_steam_proxy(
    msg_type: int,
    msg: Message,
    response_type: type[R],
    cooldown_time: int,
    groups: list[str],
    cache_time: int | None = None,
) -> R:
    try:
        cache_key = f"{msg_type}:{msg.SerializeToString().hex()}"
        cached_value = redis_conn(decode_responses=False).get(cache_key)
        if cached_value:
            return response_type.FromString(cached_value)
    except Exception as e:
        LOGGER.warning(f"Failed to parse cached value: {e}")

    MAX_RETRIES = 3
    for i in range(MAX_RETRIES):
        try:
            data = call_steam_proxy_raw(msg_type, msg, cooldown_time, groups)
            try:
                if cache_time:
                    redis_conn().setex(cache_key, cache_time, data)
            except Exception as e:
                LOGGER.warning(f"Failed to cache value: {e}")
            return response_type.FromString(data)
        except Exception as e:
            LOGGER.warning(f"Failed to call Steam proxy: {e}")
            if i == MAX_RETRIES - 1:
                raise
    raise RuntimeError("steam proxy retry raise invariant broken: - should never hit this point")


def call_steam_proxy_raw(
    msg_type: int, msg: Message, cooldown_time: int, groups: list[str]
) -> bytes:
    assert CONFIG.steam_proxy, "SteamProxyConfig must be configured to call the proxy"

    msg_data = b64encode(msg.SerializeToString()).decode("utf-8")
    body = {
        "message_kind": msg_type,
        "job_cooldown_millis": cooldown_time,
        "bot_in_all_groups": groups,
        "data": msg_data,
    }
    response = requests.post(
        CONFIG.steam_proxy.url,
        json=body,
        headers={"Authorization": f"Bearer {CONFIG.steam_proxy.api_token}"},
    )
    try:
        response.raise_for_status()
    except HTTPError as e:
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    data = response.json()["data"]
    return b64decode(data)


class APIKeyHeaderOrQuery(APIKeyBase):
    def __init__(
        self,
        *,
        query_name: str,
        header_name: str,
        scheme_name: str | None = None,
        description: str | None = None,
        auto_error: bool = True,
    ):
        self.model: APIKey = APIKey(
            **{"in": APIKeyIn.query},  # type: ignore[arg-type]
            name=query_name,
            description=description,
        )
        self.header_model: APIKey = APIKey(
            **{"in": APIKeyIn.header},  # type: ignore[arg-type]
            name=header_name,
            description=description,
        )
        self.scheme_name = scheme_name or self.__class__.__name__
        self.auto_error = auto_error

    async def __call__(self, request: Request) -> str | None:
        query_api_key = request.query_params.get(self.model.name)
        header_api_key = request.headers.get(self.header_model.name)
        if not query_api_key and not header_api_key:
            if self.auto_error:
                raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Not authenticated")
            else:
                return None
        return query_api_key or header_api_key


api_key_param = APIKeyHeaderOrQuery(query_name="api_key", header_name="X-API-Key")


@ttl_cache(maxsize=1024, ttl=60)
def is_valid_api_key(api_key: str, data_access: bool = False) -> bool:
    api_key = api_key.lstrip("HEXE-")
    with postgres_conn().cursor() as cursor:
        cursor.execute(
            "SELECT 1 FROM api_keys WHERE key = %s AND disabled IS FALSE AND (data_access OR NOT %s)",
            (str(api_key), data_access),
        )
        return cursor.fetchone() is not None


def validate_account_groups(account_groups: str, api_key: str | None) -> str | None:
    if not account_groups:
        return None
    if not api_key:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Account groups require an API key"
        )
    for group in account_groups.split(","):
        if not has_api_key_account_group_access(api_key, group):
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN, detail=f"Invalid account group: {group}"
            )
    return account_groups


def has_api_key_account_group_access(api_key: str, group_name: str = None):
    if not is_valid_api_key(api_key):
        raise HTTPException(status_code=HTTP_403_FORBIDDEN)
    api_key = api_key.lstrip("HEXE-")
    with postgres_conn().cursor() as cursor:
        cursor.execute(
            "SELECT 1 FROM api_key_account_groups WHERE key = %s AND account_group_name = %s",
            (str(api_key), group_name),
        )
        return cursor.fetchone() is not None


async def get_api_key(api_key: str = Security(api_key_param)):
    if not is_valid_api_key(api_key):
        raise HTTPException(status_code=HTTP_403_FORBIDDEN)
    return api_key


async def get_data_api_key(api_key: str = Security(api_key_param)):
    try:
        if not is_valid_api_key(api_key, True):
            raise HTTPException(status_code=HTTP_403_FORBIDDEN)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_403_FORBIDDEN)
    return api_key


def validate_steam_id_optional(steam_id: int | str | None) -> int | None:
    if not steam_id:
        return None
    return validate_steam_id(steam_id)


def validate_steam_id(steam_id: int | str) -> int:
    try:
        steam_id = int(steam_id)
        if steam_id >= STEAM_ID_64_IDENT:
            return steam_id - STEAM_ID_64_IDENT
        return steam_id
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def cache_file(key: str, data: bytes):
    s3 = s3_cache_conn()
    s3.put_object(Bucket=CONFIG.s3_cache.meta_file_bucket_name, Key=key, Body=data)


def get_cached_file(key: str) -> bytes | None:
    s3 = s3_cache_conn()
    try:
        response = s3.get_object(Bucket=CONFIG.s3_cache.meta_file_bucket_name, Key=key)
        return response["Body"].read()
    except s3.exceptions.NoSuchKey:
        return None
    except Exception as e:
        LOGGER.warning(f"Failed to get cached file: {e}")
        return None


T = TypeVar("T")  # Generic type variable


def notnone(value: T | None, message: str = "Value cannot be None") -> T:
    """
    Asserts that a value is not None and returns it with proper typing.

    Args:
        value: The value to check
        message: Custom error message for when assertion fails

    Returns:
        The input value if it's not None

    Raises:
        AssertionError: If the value is None

    Examples:
        >>> x: str | None = get_optional_string()
        >>> validated_x: str = assert_not_none(x)
    """
    assert value is not None, message
    return value


def subscribe_webhook(webhook_url: str, event_types: list[str]) -> dict:
    response = requests.post(
        f"{CONFIG.hook0.api_url}/subscriptions",
        json={
            "application_id": CONFIG.hook0.application_id,
            "event_types": event_types,
            "is_enabled": True,
            "label_key": "all",
            "label_value": "yes",
            "target": {
                "type": "http",
                "method": "POST",
                "url": webhook_url,
                "headers": {"Content-Type": "application/json"},
            },
        },
        headers={"Authorization": f"Bearer {CONFIG.hook0.api_key}"},
    )
    response.raise_for_status()
    return response.json()


def unsubscribe_webhook(subscription_id: str):
    requests.delete(
        f"{CONFIG.hook0.api_url}/subscriptions/{subscription_id}",
        params={"application_id": CONFIG.hook0.application_id},
        headers={"Authorization": f"Bearer {CONFIG.hook0.api_key}"},
    ).raise_for_status()


def send_webhook_event(event_type: str, data: str):
    requests.post(
        f"{CONFIG.hook0.api_url}/event",
        json={
            "application_id": CONFIG.hook0.application_id,
            "event_id": str(uuid.uuid4()),
            "event_type": event_type,
            "labels": {"all": "yes"},
            "occurred_at": f"{datetime.now().isoformat()}Z",
            "payload_content_type": "application/json",
            "payload": data,
        },
        headers={"Authorization": f"Bearer {CONFIG.hook0.api_key}"},
    ).raise_for_status()


class ExcludeRoutesMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: ASGIApp,
        exclude_routes: list[str],
        proxied_middleware_class: type,
        *proxied_args,
        **proxied_kwargs,
    ):
        super().__init__(app)
        self.exclude_routes = exclude_routes
        self.middleware = proxied_middleware_class(app=app, *proxied_args, **proxied_kwargs)

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)
        path = scope["path"]
        if path in self.exclude_routes:
            return await self.app(scope, receive, send)
        return await self.middleware(scope, receive, send)
