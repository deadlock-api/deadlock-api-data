import boto3
import psycopg2
import redis
from clickhouse_pool import ChPool

from deadlock_data_api.conf import CONFIG

CH_POOL = ChPool(
    host=CONFIG.clickhouse.host,
    port=CONFIG.clickhouse.port,
    user=CONFIG.clickhouse.user,
    password=CONFIG.clickhouse.password,
    database=CONFIG.clickhouse.database_name,
    connections_max=600,
)


def s3_conn():
    return boto3.client(
        service_name="s3",
        region_name=CONFIG.s3.region_name,
        endpoint_url=CONFIG.s3.endpoint_url,
        aws_access_key_id=CONFIG.s3.aws_access_key_id,
        aws_secret_access_key=CONFIG.s3.aws_secret_access_key,
    )


def redis_conn():
    return redis.Redis(
        host=CONFIG.redis.host,
        port=CONFIG.redis.port,
        password=CONFIG.redis.password,
        db=0,
        decode_responses=True,
    )


def postgres_conn():
    return psycopg2.connect(
        host=CONFIG.postgres.host,
        port=CONFIG.postgres.port,
        user="postgres",
        password=CONFIG.postgres.password,
    )
