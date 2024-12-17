import functools
import os
import pathlib

from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="./core/.env")

    BASE_DIR: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent
    ENVIRONMENT: str = "local"

    CORS_ALLOW_ORIGIN_LIST: str = "*"

    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "base"

    REDIS_DSN: str = "redis://localhost:6379"

    S3_DSN: str = "http://localhost:9000"
    S3_ACCESS_KEY_ID: str = "base"
    S3_SECRET_ACCESS_KEY: str = "base"
    S3_REGION_NAME: str = "eu-central-1"
    S3_BUCKET_NAME: str = "base"
    STORAGE_FILE_PATH: str = "base/dir/"
    PRESIGNED_FILE_URL_EXPIRATION_TIME: int = 3600

    SESSION_MIDDLEWARE_SECRET: str = "secret"

    @property
    def cors_allow_origins(self) -> list[str]:
        return self.CORS_ALLOW_ORIGIN_LIST.split("&")

    @property
    def postgres_dsn(self) -> str:
        database = self.POSTGRES_DB if self.ENVIRONMENT != "test" else f"{self.POSTGRES_DB}_test"
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{database}"
        )


@functools.lru_cache
def settings() -> Settings:
    return Settings()


logger.add(
    os.path.join(settings().BASE_DIR.parent, "logs/errors/log_{time}.log"),
    level="ERROR",
    format="{time} {message}",
    rotation="1 day",
)
logger.add(
    os.path.join(settings().BASE_DIR.parent, "logs/info/log_{time}.log"),
    level="INFO",
    format="{time} {level} {message}",
    rotation="1 day",
)
