import logging
import os
import uuid
from base64 import b64decode, b64encode
from typing import TypeVar

import requests
from cachetools.func import ttl_cache
from discord_webhook import DiscordWebhook
from fastapi import HTTPException, Security
from fastapi.openapi.models import APIKey, APIKeyIn
from fastapi.security.api_key import APIKeyBase
from google.protobuf.message import Message
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN

from deadlock_data_api.globs import postgres_conn

LOGGER = logging.getLogger(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1286415194427363380/Bb5mGAqn1yicXzRigxOkyYxZiGsL1AXI-PqxMf7Z7oxqTh4wBsN1oGHThbDGhKNZ9NAC"
WEBHOOK = DiscordWebhook(url=WEBHOOK_URL)
STEAM_PROXY_URL = os.environ.get("STEAM_PROXY_URL")
STEAM_PROXY_API_TOKEN = os.environ.get("STEAM_PROXY_API_TOKEN")


def send_webhook_message(message: str):
    LOGGER.info(f"Sending webhook message: {message}")
    WEBHOOK.content = message
    WEBHOOK.execute()


def is_valid_uuid(value: str) -> bool:
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


def call_steam_proxy(msg_type: int, msg: Message, response_type: type[R]) -> R:
    data = call_steam_proxy_raw(msg_type, msg)
    return response_type.FromString(data)


def call_steam_proxy_raw(msg_type, msg):
    msg_data = b64encode(msg.SerializeToString()).decode("utf-8")
    body = {
        "messageType": msg_type,
        "timeoutMillis": 10_000,
        "rateLimit": {
            "messagePeriodMillis": 10,
        },
        "limitBufferingBehavior": "too_many_requests",
        "data": msg_data,
    }
    response = requests.post(
        STEAM_PROXY_URL,
        json=body,
        headers={"Authorization": f"Bearer {STEAM_PROXY_API_TOKEN}"},
    )
    response.raise_for_status()
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
                raise HTTPException(
                    status_code=HTTP_403_FORBIDDEN, detail="Not authenticated"
                )
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
