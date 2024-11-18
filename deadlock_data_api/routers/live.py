import logging

import requests
from confluent_kafka import Consumer
from fastapi import APIRouter, HTTPException
from starlette.requests import Request
from starlette.responses import Response, StreamingResponse
from starlette.websockets import WebSocket

from deadlock_data_api.conf import CONFIG
from deadlock_data_api.rate_limiter import limiter
from deadlock_data_api.rate_limiter.models import RateLimit

LOGGER = logging.getLogger(__name__)

router = APIRouter(prefix="/live", tags=["Live"])


@router.post(
    "/matches/{match_id}/start-stream", summary="Rate Limit 1req/min | API-Key Rate Limit 10req/min"
)
def start_stream(req: Request, res: Response, match_id: str):
    limiter.apply_limits(
        req,
        res,
        "/live/matches/{match_id}/start-stream",
        [RateLimit(limit=1, period=60)],
        [RateLimit(limit=10, period=60)],
    )
    LOGGER.info(f"Starting stream for match {match_id}")
    try:
        requests.post(
            f"https://broadcaster.deadlock-api.com/api/matches/{match_id}/start-stream"
        ).raise_for_status()
    except requests.HTTPError as e:
        LOGGER.error(f"Failed to start stream for match {match_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to get active streams")
    return {"status": "ok"}


@router.get("/matches/active-streams", summary="Rate Limit 100req/s")
def get_active_streams(req: Request, res: Response) -> list[int]:
    limiter.apply_limits(
        req,
        res,
        "/live/matches/{match_id}/start-stream",
        [RateLimit(limit=100, period=1)],
    )
    LOGGER.info("Getting active streams")
    try:
        return requests.get(
            "https://broadcaster.deadlock-api.com/api/matches/active-streams"
        ).json()
    except requests.HTTPError as e:
        LOGGER.error(f"Failed to get active streams: {e}")
        raise HTTPException(status_code=500, detail="Failed to get active streams")


@router.get("/matches/{match_id}/stream_sse", summary="Stream game events via Server-Sent Events")
def stream_sse(req: Request, match_id: str) -> StreamingResponse:
    LOGGER.info(f"Streaming match {match_id} via SSE")

    async def event_stream():
        consumer = Consumer(
            {
                "bootstrap.servers": CONFIG.kafka.bootstrap_servers(),
                "group.id": req.headers.get("CF-Connecting-IP", req.client.host),
                "auto.offset.reset": "earliest",
            }
        )
        consumer.subscribe([f"game-streams-{match_id}"])
        while True:
            message = consumer.poll(timeout=1.0)
            if message is None:
                continue
            if message.error():
                LOGGER.error(f"Consumer error: {message.error()}")
                continue
            LOGGER.debug(f"Sending message: {message.value().decode('utf-8')}")
            yield message.value() + b"\n"

    return StreamingResponse(event_stream())


@router.get(
    "/matches/{match_id}/stream_ws",
    summary="Stream game events via WebSockets",
    description="""
# Websocket streaming

This is just a placeholder to document the websocket streaming endpoint. It doesn't actually do anything.

You can connect to this endpoint using a websocket client.
""",
)
def stream_websocket_dummy(match_id: str) -> str:
    LOGGER.info(f"Streaming match {match_id} via websocket")
    return (
        "This is just a placeholder, you have to connect to this endpoint using a websocket client."
    )


@router.websocket("/matches/{match_id}/stream_ws")
async def stream_websocket(websocket: WebSocket, match_id: str):
    LOGGER.info(f"Streaming match {match_id} via websocket")

    await websocket.accept()

    consumer = Consumer(
        {
            "bootstrap.servers": CONFIG.kafka.bootstrap_servers(),
            "group.id": websocket.client.host,
            "auto.offset.reset": "earliest",
        }
    )
    consumer.subscribe([f"game-streams-{match_id}"])
    while True:
        message = consumer.poll(timeout=1.0)
        if message is None:
            continue
        if message.error():
            LOGGER.error(f"Consumer error: {message.error()}")
            continue
        LOGGER.debug(f"Sending message: {message.value().decode('utf-8')}")
        await websocket.send_bytes(message.value() + b"\n")
