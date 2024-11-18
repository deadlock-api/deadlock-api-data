import logging
import uuid

import requests
from aiokafka import AIOKafkaConsumer
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
def stream_sse(match_id: str) -> StreamingResponse:
    LOGGER.info(f"Streaming match {match_id} via SSE")

    async def event_stream():
        consumer = AIOKafkaConsumer(
            f"game-streams-{match_id}",
            bootstrap_servers=CONFIG.kafka.bootstrap_servers(),
            group_id=str(uuid.uuid4()),
            auto_offset_reset="earliest",
        )
        await consumer.start()
        try:
            async for msg in consumer:
                LOGGER.debug(f"Sending message: {msg.value.decode('utf-8')}")
                yield msg.value + b"\n"
        finally:
            await consumer.stop()

    return StreamingResponse(event_stream())


@router.get(
    "/matches/{match_id}/stream_ws_",
    summary="Stream game events via WebSockets",
    description="""
# Websocket streaming

This is just a placeholder to document the websocket streaming endpoint. It doesn't actually do anything.

You can connect to this endpoint using a websocket client.
""",
)
def stream_websocket_dummy(match_id: str) -> dict[str, str]:
    return {"websocket_url": f"wss://data.deadlock-api.com/live/matches/{match_id}/stream_ws"}


@router.websocket("/matches/{match_id}/stream_ws")
async def stream_websocket(websocket: WebSocket, match_id: str):
    await websocket.accept()

    LOGGER.info(f"Streaming match {match_id} via websocket")

    consumer = AIOKafkaConsumer(
        f"game-streams-{match_id}",
        bootstrap_servers=CONFIG.kafka.bootstrap_servers(),
        group_id=websocket.client.host,
        auto_offset_reset="earliest",
    )
    await consumer.start()
    try:
        async for msg in consumer:
            LOGGER.debug(f"Sending message: {msg.value.decode('utf-8')}")
            await websocket.send_bytes(msg.value + b"\n")
    finally:
        await consumer.stop()
