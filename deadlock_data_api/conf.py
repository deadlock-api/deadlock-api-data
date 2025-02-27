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
class KafkaConfig:
    host: str
    port: int

    def bootstrap_servers(self) -> str:
        return f"{self.host}:{self.port}"

    @classmethod
    def from_env(cls) -> "KafkaConfig":
        return cls(
            host=os.environ.get("KAFKA_HOST", "kafka"),
            port=int(os.environ.get("KAFKA_PORT", 9092)),
        )


# @dataclass
# class S3Config:
#     region_name: str | None
#     endpoint_url: str | None
#     aws_access_key_id: str | None
#     aws_secret_access_key: str | None
#
#     meta_file_bucket_name: str
#     """The bucket which contains .meta.bz2 files"""
#
#     @classmethod
#     def from_env(cls, s3_name: str) -> "S3Config":
#         return cls(
#             region_name=os.environ.get(f"S3_{s3_name}_REGION"),
#             endpoint_url=os.environ.get(f"S3_{s3_name}_ENDPOINT_URL_WITH_PROTOCOL"),
#             aws_access_key_id=os.environ.get(f"S3_{s3_name}_ACCESS_KEY_ID"),
#             aws_secret_access_key=os.environ.get(f"S3_{s3_name}_SECRET_ACCESS_KEY"),
#             meta_file_bucket_name=os.environ.get(f"S3_{s3_name}_BUCKET_NAME", "hexe"),
#         )


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
class HOOK0Config:
    api_url: str
    application_id: str
    api_key: str

    @classmethod
    def from_env(cls) -> "HOOK0Config":
        return cls(
            api_url=os.environ.get("HOOK0_API_URL", "https://webhook-api.deadlock-api.com/api/v1"),
            application_id=os.environ.get("HOOK0_APPLICATION_ID"),
            api_key=os.environ.get("HOOK0_API_KEY"),
        )


@dataclass
class AppConfig:
    clickhouse: ClickhouseConfig
    redis: RedisConfig
    postgres: PostgresConfig
    # s3_main: S3Config
    # s3_cache: S3Config
    kafka: KafkaConfig
    hook0: HOOK0Config
    steam_proxy: SteamProxyConfig | None
    steam_api_key: str
    emergency_mode: bool
    enforce_rate_limits: bool
    # demo_retention_days: int
    sentry_dsn: str | None
    deactivate_match_history: bool = False
    # deactivate_match_metadata: bool = False
    deactivate_live_endpoints: bool = False

    @classmethod
    def from_env(cls) -> "AppConfig":
        return cls(
            clickhouse=ClickhouseConfig.from_env(),
            redis=RedisConfig.from_env(),
            postgres=PostgresConfig.from_env(),
            # s3_main=S3Config.from_env("MAIN"),
            # s3_cache=S3Config.from_env("CACHE"),
            kafka=KafkaConfig.from_env(),
            hook0=HOOK0Config.from_env(),
            steam_proxy=SteamProxyConfig.from_env(),
            steam_api_key=os.environ.get("STEAM_API_KEY"),
            emergency_mode=os.environ.get("EMERGENCY_MODE") == "true",
            enforce_rate_limits=os.environ.get("ENFORCE_RATE_LIMITS") == "true",
            # demo_retention_days=int(os.environ.get("DEMO_RETENTION_DAYS", 21)),
            sentry_dsn=os.environ.get("SENTRY_DSN"),
            deactivate_match_history=os.environ.get("DEACTIVATE_MATCH_HISTORY") == "true",
            # deactivate_match_metadata=os.environ.get("DEACTIVATE_MATCH_METADATA") == "true",
            deactivate_live_endpoints=os.environ.get("DEACTIVATE_LIVE_ENDPOINTS") == "true",
        )


CONFIG = AppConfig.from_env()
