import logging

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from starlette.responses import RedirectResponse

from deadlock_api.routers import base, v1

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Deadlock Data API",
    description="API for Deadlock game data, containing builds and active matches",
)

Instrumentator().instrument(app).expose(app, include_in_schema=False)

app.include_router(base.router, include_in_schema=False)
app.include_router(v1.router)


@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse("/docs")


@app.get("/health", include_in_schema=False)
def get_health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
