import time

from discord_webhook import DiscordWebhook


class State:
    is_up: bool = True


APP_STATE = State()


WEBHOOK_URL = "https://discord.com/api/webhooks/1286415194427363380/Bb5mGAqn1yicXzRigxOkyYxZiGsL1AXI-PqxMf7Z7oxqTh4wBsN1oGHThbDGhKNZ9NAC"
WEBHOOK = DiscordWebhook(url=WEBHOOK_URL)


def dynamic_cache_time(last_modified: float, max_cache_age: int) -> int:
    age = time.time() - last_modified

    if age <= max_cache_age:
        if APP_STATE.is_up is False:
            WEBHOOK.content = f"Data is now up to date"
            WEBHOOK.execute()
            APP_STATE.is_up = True
        return int(max_cache_age - age + 1)

    if age > max_cache_age + 180:
        print("Data is stale")
        if APP_STATE.is_up:
            WEBHOOK.content = f"Data last updated {int(age)} seconds ago"
            WEBHOOK.execute()
            APP_STATE.is_up = False
    return 10
