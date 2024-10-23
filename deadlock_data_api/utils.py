import logging
import uuid

from discord_webhook import DiscordWebhook

LOGGER = logging.getLogger(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1286415194427363380/Bb5mGAqn1yicXzRigxOkyYxZiGsL1AXI-PqxMf7Z7oxqTh4wBsN1oGHThbDGhKNZ9NAC"
WEBHOOK = DiscordWebhook(url=WEBHOOK_URL)


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
