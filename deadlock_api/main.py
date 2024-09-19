import logging

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import RedirectResponse

from deadlock_api.models.active_match import ActiveMatch, APIActiveMatch
from deadlock_api.models.build import APIBuild, Build

logging.basicConfig(level=logging.INFO)

app = FastAPI()


@app.middleware("http")
async def add_cache_headers(request: Request, call_next):
    response = await call_next(request)
    is_success = 200 <= response.status_code < 300
    is_docs = request.url.path.replace("/", "").startswith("docs")
    if is_success and not is_docs:
        response.headers["Cache-Control"] = "public, max-age=10"
    return response


@app.get("/")
def redirect_to_docs():
    return RedirectResponse("/docs")


@app.get("/builds", response_model_exclude_none=True)
def get_builds() -> list[Build]:
    with open("builds.json") as f:
        return APIBuild.model_validate_json(f.read()).results


@app.get("/active-matches", response_model_exclude_none=True)
def get_active_matches() -> list[ActiveMatch]:
    with open("active_matches.json") as f:
        return APIActiveMatch.model_validate_json(f.read()).active_matches


@app.get("/health", include_in_schema=False)
def get_health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
