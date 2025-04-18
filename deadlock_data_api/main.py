import logging.config
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from starlette.responses import PlainTextResponse, RedirectResponse

from deadlock_data_api.routers import v1, v2

logging.basicConfig(level=os.environ.get("LOG_LEVEL", "DEBUG"))
logging.getLogger("urllib3").setLevel(logging.WARNING)

LOGGER = logging.getLogger(__name__)

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
instrumentator = Instrumentator(should_group_status_codes=False).instrument(app)


@app.on_event("startup")
async def _startup():
    instrumentator.expose(app, include_in_schema=False)


app.include_router(v2.router)
app.include_router(v1.router)


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
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
