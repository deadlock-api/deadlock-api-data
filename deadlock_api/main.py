import logging
import os
import time

from discord_webhook import DiscordWebhook
from fastapi import FastAPI, HTTPException
from pydantic import TypeAdapter
from starlette.responses import RedirectResponse, Response

from deadlock_api.models.active_match import ActiveMatch, APIActiveMatch
from deadlock_api.models.build import Build

WEBHOOK_URL = "https://discord.com/api/webhooks/1286415194427363380/Bb5mGAqn1yicXzRigxOkyYxZiGsL1AXI-PqxMf7Z7oxqTh4wBsN1oGHThbDGhKNZ9NAC"
WEBHOOK = DiscordWebhook(url=WEBHOOK_URL)


class State:
    is_up: bool = True


APP_STATE = State()

logging.basicConfig(level=logging.INFO)

CACHE_AGE_ACTIVE_MATCHES = 30
CACHE_AGE_BUILDS = CACHE_AGE_ACTIVE_MATCHES * 12

app = FastAPI()


@app.get("/")
def redirect_to_docs():
    return RedirectResponse("/docs")


@app.get("/builds")
def get_builds(response: Response) -> dict[str, list[Build]]:
    last_modified = os.path.getmtime("builds.json")
    cache_time = dynamic_cache_time(last_modified, CACHE_AGE_BUILDS)
    response.headers["Cache-Control"] = f"public, max-age={cache_time}"
    response.headers["Last-Updated"] = str(int(last_modified))
    ta = TypeAdapter(dict[str, list[Build]])
    with open("builds.json") as f:
        return ta.validate_json(f.read())


@app.get("/builds/{build_id}")
def get_build(response: Response, build_id: int) -> Build:
    builds = get_builds(response)
    build = next(
        (
            b
            for bs in builds.values()
            for b in bs
            if b.hero_build.hero_build_id == build_id
        ),
        None,
    )
    if build is None:
        raise HTTPException(status_code=404, detail="Build not found")
    return build


@app.get("/builds/by-hero-id/{hero_id}")
def get_builds_by_hero_id(response: Response, hero_id: int) -> list[Build]:
    builds = get_builds(response)
    filtered = {
        k: [h for h in v if h.hero_build.hero_id == hero_id] for k, v in builds.items()
    }
    filtered = {k: v for k, v in filtered.items() if len(v) > 0}
    if len(filtered) == 0:
        raise HTTPException(status_code=404, detail="Hero not found")
    return next(v for k, v in builds.items())


@app.get("/builds/by-hero-name/{hero_name}")
def get_builds_by_hero_name(response: Response, hero_name: str) -> list[Build]:
    builds = get_builds(response)
    filtered = next(
        (v for k, v in builds.items() if k.lower() == hero_name.lower()),
        None,
    )
    if filtered is None:
        raise HTTPException(status_code=404, detail="Hero not found")
    return filtered


@app.get("/active-matches")
def get_active_matches(response: Response) -> list[ActiveMatch]:
    last_modified = os.path.getmtime("active_matches.json")
    cache_time = dynamic_cache_time(last_modified, CACHE_AGE_ACTIVE_MATCHES)
    response.headers["Cache-Control"] = f"public, max-age={cache_time}"
    response.headers["Last-Updated"] = str(int(last_modified))
    with open("active_matches.json") as f:
        return APIActiveMatch.model_validate_json(f.read()).active_matches


def dynamic_cache_time(last_modified: float, max_cache_age: int) -> int:
    age = time.time() - last_modified

    if age < max_cache_age:
        if APP_STATE.is_up is False:
            WEBHOOK.content = f"Data is now up to date"
            WEBHOOK.execute()
            APP_STATE.is_up = True
        return int(max_cache_age - age)

    if age > 2 * max_cache_age:
        print("Data is stale")
        if APP_STATE.is_up:
            WEBHOOK.content = f"Data last updated {int(age)} seconds ago"
            WEBHOOK.execute()
            APP_STATE.is_up = False
    return 10


@app.get("/health", include_in_schema=False)
def get_health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
