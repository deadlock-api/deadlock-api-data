import uuid

from discord_webhook import DiscordWebhook


class State:
    is_up: bool = True


APP_STATE = State()

WEBHOOK_URL = "https://discord.com/api/webhooks/1286415194427363380/Bb5mGAqn1yicXzRigxOkyYxZiGsL1AXI-PqxMf7Z7oxqTh4wBsN1oGHThbDGhKNZ9NAC"
WEBHOOK = DiscordWebhook(url=WEBHOOK_URL)


def send_webhook_message(message: str):
    WEBHOOK.content = message
    WEBHOOK.execute()


def is_valid_uuid(value: str) -> bool:
    if value is None:
        return False
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        print(f"Invalid UUID: {value}")
        return False
    except TypeError:
        print(f"Invalid UUID: {value}")
        return False
