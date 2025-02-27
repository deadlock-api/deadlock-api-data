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


# def s3_main_conn():
#     return boto3.client(
#         service_name="s3",
#         region_name=CONFIG.s3_main.region_name,
#         endpoint_url=CONFIG.s3_main.endpoint_url,
#         aws_access_key_id=CONFIG.s3_main.aws_access_key_id,
#         aws_secret_access_key=CONFIG.s3_main.aws_secret_access_key,
#     )


# def s3_cache_conn():
#     return boto3.client(
#         service_name="s3",
#         region_name=CONFIG.s3_cache.region_name,
#         endpoint_url=CONFIG.s3_cache.endpoint_url,
#         aws_access_key_id=CONFIG.s3_cache.aws_access_key_id,
#         aws_secret_access_key=CONFIG.s3_cache.aws_secret_access_key,
#         aws_session_token=None,
#         config=boto3.session.Config(signature_version="s3v4"),
#     )


def redis_conn(decode_responses: bool = True):
    return redis.Redis(
        host=CONFIG.redis.host,
        port=CONFIG.redis.port,
        password=CONFIG.redis.password,
        db=0,
        decode_responses=decode_responses,
    )


def postgres_conn():
    return psycopg2.connect(
        host=CONFIG.postgres.host,
        port=CONFIG.postgres.port,
        user="postgres",
        password=CONFIG.postgres.password,
    )
