import logging
import os
import uuid
from base64 import b64decode, b64encode
from typing import TypeVar

import requests
from cachetools.func import ttl_cache
from discord_webhook import DiscordWebhook
from fastapi import HTTPException, Security
from fastapi.security import APIKeyQuery
from google.protobuf.message import Message
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
    msg_data = b64encode(msg.SerializeToString()).decode("utf-8")
    body = {
        "messageType": msg_type,
        "timeoutMillis": 10_000,
        "rateLimit": {
            "messagePeriodMillis": 2_000,
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
    data = b64decode(data)
    return response_type.FromString(data)


api_key_query = APIKeyQuery(name="api_key", auto_error=True)


@ttl_cache(maxsize=1024, ttl=60)
def is_valid_api_key(api_key: str, data_access: bool = False) -> bool:
    api_key = api_key.lstrip("HEXE-")
    with postgres_conn().cursor() as cursor:
        cursor.execute(
            "SELECT 1 FROM api_keys WHERE key = %s AND (data_access OR NOT %s)",
            (str(api_key), data_access),
        )
        return cursor.fetchone() is not None


async def get_api_key(api_key: str = Security(api_key_query)):
    if not is_valid_api_key(api_key):
        raise HTTPException(status_code=HTTP_403_FORBIDDEN)
    return api_key


async def get_data_api_key(api_key: str = Security(api_key_query)):
    try:
        if not is_valid_api_key(api_key, True):
            raise HTTPException(status_code=HTTP_403_FORBIDDEN)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_403_FORBIDDEN)
    return api_key
