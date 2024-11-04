import os

import boto3
import psycopg2
import redis
from clickhouse_pool import ChPool

CH_POOL = ChPool(
    host=os.getenv("CLICKHOUSE_HOST", "localhost"),
    port=int(os.getenv("CLICKHOUSE_PORT", 9000)),
    user=os.getenv("CLICKHOUSE_USER", "default"),
    password=os.getenv("CLICKHOUSE_PASSWORD", ""),
    database=os.getenv("CLICKHOUSE_DB", "default"),
    connections_max=600,
)

REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
REDIS_PASS = os.environ.get("REDIS_PASS")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "postgres")
POSTGRES_PASS = os.environ.get("POSTGRES_PASS")


def s3_conn():
    return boto3.client(
        service_name="s3",
        region_name=os.environ.get("S3_REGION"),
        endpoint_url=os.environ.get("S3_ENDPOINT_URL_WITH_PROTOCOL"),
        aws_access_key_id=os.environ.get("S3_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("S3_SECRET_ACCESS_KEY"),
    )


def redis_conn():
    return redis.Redis(
        host=REDIS_HOST, port=6379, password=REDIS_PASS, db=0, decode_responses=True
    )


def postgres_conn():
    return psycopg2.connect(
        host=POSTGRES_HOST, port=5432, user="postgres", password=POSTGRES_PASS
    )


ENFORCE_RATE_LIMITS: bool = bool(os.environ.get("ENFORCE_RATE_LIMITS", False))
