import functools
import os

from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict

from core.settings import (
    CommonSettings,
    InfraSettings,
    StorageSettings,
)


class Settings(
    BaseSettings,
    CommonSettings,
    InfraSettings,
    StorageSettings,
):
    model_config = SettingsConfigDict(env_file="./core/.env", extra="ignore")


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
