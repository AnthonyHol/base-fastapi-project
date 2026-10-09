import functools

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
    model_config = SettingsConfigDict(env_file='./core/.env', extra='ignore')


@functools.lru_cache
def settings() -> Settings:
    return Settings()
