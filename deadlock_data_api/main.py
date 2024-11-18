import logging
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from starlette.middleware.gzip import GZipMiddleware
from starlette.responses import PlainTextResponse, RedirectResponse

from deadlock_data_api.conf import CONFIG
from deadlock_data_api.routers import base, live, v1, v2

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

Instrumentator(should_group_status_codes=False).instrument(app).expose(app, include_in_schema=False)

app.include_router(live.router)
app.include_router(v2.router)
app.include_router(v1.router)
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
