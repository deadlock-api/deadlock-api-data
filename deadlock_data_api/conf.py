import os
from dataclasses import dataclass

"""
A basic place to centralize configuration, can be later made more sophisticated
"""


@dataclass
class ClickhouseConfig:
    host: str
    port: int
    user: str
    password: str
    database_name: str


@dataclass
class RedisConfig:
    host: str
    password: str | None
    port: int


@dataclass
class PostgresConfig:
    host: str
    password: str | None
    port: int


@dataclass
class S3Config:
    region_name: str | None
    endpoint_url: str | None
    aws_access_key_id: str | None
    aws_secret_access_key: str | None

    meta_file_bucket_name: str
    """The bucket which contains .meta.bz2 files"""


@dataclass
class SteamProxyConfig:
    url: str
    api_token: str


@dataclass
class AppConfig:
    clickhouse: ClickhouseConfig
    redis: RedisConfig
    postgres: PostgresConfig
    s3: S3Config
    steam_proxy: SteamProxyConfig | None
    discord_webhook_url: str | None
    emergency_mode: bool
    enforce_rate_limits: bool

    sentry_dsn: str | None


def make_app_config_from_env() -> AppConfig:
    """
    Initialize an AppConfig from environment variables
    """
    clickhouse_conf = ClickhouseConfig(
        host=os.environ.get("CLICKHOUSE_HOST", "localhost"),
        port=int(os.environ.get("CLICKHOUSE_PORT", 9000)),
        user=os.environ.get("CLICKHOUSE_USER", "default"),
        password=os.environ.get("CLICKHOUSE_PASSWORD", ""),
        database_name=os.environ.get("CLICKHOUSE_DB", "default"),
    )

    redis_conf = RedisConfig(
        host=os.environ.get("REDIS_HOST", "redis"),
        password=os.environ.get("REDIS_PASS"),
        port=6379,
    )

    postgres_conf = PostgresConfig(
        host=os.environ.get("POSTGRES_HOST", "postgres"),
        password=os.environ.get("POSTGRES_PASS"),
        port=5432,
    )

    s3_conf = S3Config(
        region_name=os.environ.get("S3_REGION"),
        endpoint_url=os.environ.get("S3_ENDPOINT_URL_WITH_PROTOCOL"),
        aws_access_key_id=os.environ.get("S3_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("S3_SECRET_ACCESS_KEY"),
        meta_file_bucket_name=os.environ.get("S3_BUCKET_NAME", "hexe"),
    )

    STEAM_PROXY_URL = os.environ.get("STEAM_PROXY_URL")
    STEAM_PROXY_API_TOKEN = os.environ.get("STEAM_PROXY_API_TOKEN")

    steam_proxy_conf = None
    if STEAM_PROXY_URL and STEAM_PROXY_API_TOKEN:
        steam_proxy_conf = SteamProxyConfig(
            url=STEAM_PROXY_URL, api_token=STEAM_PROXY_API_TOKEN
        )

    app_conf = AppConfig(
        clickhouse=clickhouse_conf,
        redis=redis_conf,
        postgres=postgres_conf,
        s3=s3_conf,
        steam_proxy=steam_proxy_conf,
        discord_webhook_url=os.environ.get("DISCORD_WEBHOOK_URL", None),
        emergency_mode=os.environ.get("EMERGENCY_MODE") == "true",
        enforce_rate_limits=os.environ.get("ENFORCE_RATE_LIMITS") == "true",
        sentry_dsn=os.environ.get("SENTRY_DSN"),
    )

    return app_conf


CONFIG = make_app_config_from_env()
