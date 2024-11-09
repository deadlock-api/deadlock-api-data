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

    @classmethod
    def from_env(cls) -> "ClickhouseConfig":
        return cls(
            host=os.environ.get("CLICKHOUSE_HOST", "localhost"),
            port=int(os.environ.get("CLICKHOUSE_PORT", 9000)),
            user=os.environ.get("CLICKHOUSE_USER", "default"),
            password=os.environ.get("CLICKHOUSE_PASSWORD", ""),
            database_name=os.environ.get("CLICKHOUSE_DB", "default"),
        )


@dataclass
class RedisConfig:
    host: str
    password: str | None
    port: int

    @classmethod
    def from_env(cls) -> "RedisConfig":
        return cls(
            host=os.environ.get("REDIS_HOST", "redis"),
            password=os.environ.get("REDIS_PASS"),
            port=int(os.environ.get("REDIS_PORT", 6379)),
        )


@dataclass
class PostgresConfig:
    host: str
    password: str | None
    port: int

    @classmethod
    def from_env(cls) -> "PostgresConfig":
        return cls(
            host=os.environ.get("POSTGRES_HOST", "postgres"),
            password=os.environ.get("POSTGRES_PASS"),
            port=int(os.environ.get("POSTGRES_PORT", 5432)),
        )


@dataclass
class S3Config:
    region_name: str | None
    endpoint_url: str | None
    aws_access_key_id: str | None
    aws_secret_access_key: str | None

    meta_file_bucket_name: str
    """The bucket which contains .meta.bz2 files"""

    @classmethod
    def from_env(cls) -> "S3Config":
        return cls(
            region_name=os.environ.get("S3_REGION"),
            endpoint_url=os.environ.get("S3_ENDPOINT_URL_WITH_PROTOCOL"),
            aws_access_key_id=os.environ.get("S3_ACCESS_KEY_ID"),
            aws_secret_access_key=os.environ.get("S3_SECRET_ACCESS_KEY"),
            meta_file_bucket_name=os.environ.get("S3_BUCKET_NAME", "hexe"),
        )


@dataclass
class SteamProxyConfig:
    url: str
    api_token: str

    @classmethod
    def from_env(cls) -> "SteamProxyConfig":
        return cls(
            url=os.environ.get("STEAM_PROXY_URL"),
            api_token=os.environ.get("STEAM_PROXY_API_TOKEN"),
        )


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

    @classmethod
    def from_env(cls) -> "AppConfig":
        return cls(
            clickhouse=ClickhouseConfig.from_env(),
            redis=RedisConfig.from_env(),
            postgres=PostgresConfig.from_env(),
            s3=S3Config.from_env(),
            steam_proxy=SteamProxyConfig.from_env(),
            discord_webhook_url=os.environ.get("DISCORD_WEBHOOK_URL"),
            emergency_mode=os.environ.get("EMERGENCY_MODE") == "true",
            enforce_rate_limits=os.environ.get("ENFORCE_RATE_LIMITS") == "true",
            sentry_dsn=os.environ.get("SENTRY_DSN"),
        )


CONFIG = AppConfig.from_env()
