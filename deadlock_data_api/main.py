import logging
import os

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from pydantic import BaseModel, Field
from starlette.middleware.gzip import GZipMiddleware
from starlette.responses import PlainTextResponse, RedirectResponse

from deadlock_data_api import utils
from deadlock_data_api.conf import CONFIG
from deadlock_data_api.globs import postgres_conn
from deadlock_data_api.routers import base, live, v1, v2
from deadlock_data_api.utils import send_webhook_event

# Doesn't use AppConfig because logging is critical
logging.basicConfig(level=os.environ.get("LOG_LEVEL", "DEBUG"))

if CONFIG.sentry_dsn:
    import sentry_sdk

    sentry_sdk.init(
        dsn=CONFIG.sentry_dsn,
        traces_sample_rate=0.2,
        _experiments={
            "continuous_profiling_auto_start": True,
        },
    )

app = FastAPI(
    title="Data - Deadlock API",
    description="""
Part of the [https://deadlock-api.com](https://deadlock-api.com) project.

API for Deadlock game data, containing builds and active matches.

_deadlock-api.com is not endorsed by Valve and does not reflect the views or opinions of Valve or anyone officially involved in producing or managing Valve properties. Valve and all associated properties are trademarks or registered trademarks of Valve Corporation_
""",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=5)

instrumentator = Instrumentator(should_group_status_codes=False).instrument(app)


@app.on_event("startup")
async def _startup():
    instrumentator.expose(app, include_in_schema=False)


app.include_router(v2.router)
app.include_router(v1.router)
app.include_router(live.router)
app.include_router(base.router, include_in_schema=False)


@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse("/docs")


@app.get("/health", include_in_schema=False)
def get_health():
    return {"status": "ok"}


@app.head("/health", include_in_schema=False)
def head_health():
    return {"status": "ok"}


@app.get("/robots.txt", include_in_schema=False, response_class=PlainTextResponse)
def get_robots() -> str:
    return "User-Agent: *\nDisallow: /\nAllow: /docs\nAllow: /\n"


class ObjectUploadedEvent(BaseModel):
    key: str = Field(..., validation_alias="Key")


class MatchCreatedWebhookPayload(BaseModel):
    match_id: int
    metadata_url: str
    raw_metadata_url: str


@app.post("/matches/created", tags=["Webhooks"], include_in_schema=False)
def match_created_event(object_uploaded_event: ObjectUploadedEvent):
    match_id = int(object_uploaded_event.key.split("/")[-1].split(".")[0])
    payload = MatchCreatedWebhookPayload(
        match_id=match_id,
        metadata_url=f"https://data.deadlock-api.com/v1/matches/{match_id}/metadata",
        raw_metadata_url=f"https://data.deadlock-api.com/v1/matches/{match_id}/raw-metadata",
    )
    send_webhook_event("match.metadata.created", payload.model_dump_json())
    return {"status": "success"}


class WebhookSubscribeRequest(BaseModel):
    webhook_url: str


@app.post("/matches/webhook/subscribe", summary="1 Webhook per API-Key", tags=["Webhooks"])
def webhook_subscribe(
    webhook_config: WebhookSubscribeRequest,
    api_key=Depends(utils.get_api_key),
):
    print(f"Authenticated with API-Key: {api_key}")
    api_key = api_key.lstrip("HEXE-")
    with postgres_conn().cursor() as cursor:
        cursor.execute("SELECT 1 FROM webhooks WHERE api_key = %s", (api_key,))
        result = cursor.fetchone()
        if result is not None:
            raise HTTPException(status_code=400, detail="Webhook already exists")
        subscription = utils.subscribe_webhook(
            webhook_config.webhook_url, ["match.metadata.created"]
        )
        cursor.execute(
            "INSERT INTO webhooks (subscription_id, api_key, webhook_url) VALUES (%s, %s, %s)",
            (subscription["subscription_id"], api_key, webhook_config.webhook_url),
        )
        cursor.execute("COMMIT")
    return {
        "status": "success",
        "subscription_id": subscription["subscription_id"],
        "event_types": subscription["event_types"],
        "secret": subscription["secret"],
    }


@app.get(
    "/matches/webhook",
    tags=["Webhooks"],
)
def webhook_list(api_key=Depends(utils.get_api_key)):
    print(f"Authenticated with API-Key: {api_key}")
    api_key = api_key.lstrip("HEXE-")
    with postgres_conn().cursor() as cursor:
        cursor.execute(
            "SELECT subscription_id, webhook_url FROM webhooks WHERE api_key = %s", (api_key,)
        )
        result = cursor.fetchall()
    return [{"subscription_id": row[0], "webhook_url": row[1]} for row in result]


@app.delete(
    "/matches/webhook/{subscription_id}/unsubscribe",
    summary="1 Webhook per API-Key",
    tags=["Webhooks"],
)
def webhook_unsubscribe(subscription_id: str, api_key=Depends(utils.get_api_key)):
    print(f"Authenticated with API-Key: {api_key}")
    with postgres_conn().cursor() as cursor:
        cursor.execute(
            "SELECT 1 FROM webhooks WHERE api_key = %s AND subscription_id = %s",
            (api_key, subscription_id),
        )
        result = cursor.fetchone()
        if result is None:
            raise HTTPException(status_code=400, detail="Webhook does not exist")
        utils.unsubscribe_webhook(subscription_id)
        cursor.execute(
            "DELETE FROM webhooks WHERE api_key = %s AND subscription_id = %s",
            (api_key, subscription_id),
        )
        cursor.execute("COMMIT")
    return {"status": "success"}


@app.webhooks.post("match-metadata-created")
def match_metadata_created() -> MatchCreatedWebhookPayload:
    """
    Webhook for when a match metadata is created.

    To verify the webhook read this: https://documentation.hook0.com/docs/verifying-webhook-signatures
    """
    pass


if __name__ == "__main__":
    import granian
    from granian.constants import Interfaces
    from granian.log import LogLevels

    granian.Granian(
        "deadlock_data_api.main:app",
        address="0.0.0.0",
        port=8080,
        interface=Interfaces.ASGI,
        log_level=LogLevels.debug,
        websockets=True,
    ).serve()
