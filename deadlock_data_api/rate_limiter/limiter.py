import logging
import time

from cachetools.func import ttl_cache
from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import Response

from deadlock_data_api import utils
from deadlock_data_api.globs import ENFORCE_RATE_LIMITS, postgres_conn, redis_conn
from deadlock_data_api.rate_limiter.models import RateLimit, RateLimitStatus

LOGGER = logging.getLogger(__name__)

MAX_TTL_SECONDS = 60 * 60  # 1 hour


def apply_limits(
    request: Request,
    response: Response,
    key: str,
    ip_limits: list[RateLimit],
    key_default_limits: list[RateLimit] | None = None,
):
    ip = request.headers.get("CF-Connecting-IP", request.client.host)
    api_key = request.headers.get("X-API-Key", request.query_params.get("api_key"))
    api_key = (
        api_key.lstrip("HEXE-")
        if api_key is not None
        and utils.is_valid_uuid(api_key.lstrip("HEXE-"))
        and utils.is_valid_api_key(api_key.lstrip("HEXE-"))
        else None
    )
    limits = []
    prefix = ip
    if api_key:
        prefix = api_key
        limits = (
            get_extra_api_key_limits(api_key, request.url.path) or key_default_limits
        )
    if not limits:
        limits = ip_limits
    status = [limit_by_key(f"{prefix}:{key}", l) for l in limits]
    for s in status:
        LOGGER.info(
            f"count: {s.count}, "
            f"limit: {s.limit}, "
            f"period: {s.period}, "
            f"remaining: {s.remaining}, "
            f"next_request: {s.next_request_in}"
        )
        if ENFORCE_RATE_LIMITS:
            try:
                s.raise_for_limit()
            except HTTPException as e:
                LOGGER.warning(f"Rate limit exceeded: {e.headers} by {ip=} {api_key=}")
                raise e
    status = sorted(status, key=lambda x: x.remaining)[0]
    response.headers.update(status.headers)


@ttl_cache(ttl=60)
def get_extra_api_key_limits(api_key: str, path: str) -> list[RateLimit]:
    with postgres_conn().cursor() as cursor:
        cursor.execute(
            "SELECT rate_limit, rate_period, path FROM api_key_limits WHERE key = %s AND path = %s",
            (api_key, path),
        )
        return [
            RateLimit(limit=r[0], period=r[1].seconds, path=r[2])
            for r in cursor.fetchall()
        ]


def limit_by_key(key: str, rate_limit: RateLimit) -> RateLimitStatus:
    LOGGER.debug(f"Checking rate limit: {key=} {rate_limit=}")
    current_time = float(time.time())
    pipe = redis_conn().pipeline()
    pipe.zremrangebyscore(key, 0, current_time - MAX_TTL_SECONDS)
    pipe.zadd(key, {str(current_time): current_time})
    pipe.zrange(key, current_time - rate_limit.period, current_time, byscore=True)
    pipe.expire(key, MAX_TTL_SECONDS)
    result = pipe.execute()
    times = list(map(float, result[2]))
    filtered_times = sorted([t for t in times if t > current_time - rate_limit.period])
    assert len(times) == len(filtered_times)
    current_count = len(filtered_times)
    if current_count > rate_limit.limit:
        redis_conn().zrem(key, current_time)
    return RateLimitStatus(
        key=key,
        count=current_count,
        limit=rate_limit.limit,
        period=rate_limit.period,
        oldest_request_time=filtered_times[0] if filtered_times else 0,
    )


def test_rate_limiter():
    while True:
        status = limit_by_key("test", RateLimit(limit=20, period=10))
        assert status.is_limited is False
        print(
            f"count: {status.count}, "
            f"limit: {status.limit}, "
            f"period: {status.period}, "
            f"remaining: {status.remaining}, "
            f"next_request: {status.next_request_in}"
        )
        time.sleep(status.next_request_in)


if __name__ == "__main__":
    test_rate_limiter()
