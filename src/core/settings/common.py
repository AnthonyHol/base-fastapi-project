import pathlib

from pydantic import BaseModel

from core.enum import EnvironmentEnum


class CommonSettings(BaseModel):
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent.parent
    ENVIRONMENT: EnvironmentEnum = EnvironmentEnum.LOCAL

    CORS_ALLOW_ORIGIN_LIST: str = '*'

    SESSION_MIDDLEWARE_SECRET: str = 'secret'

    @property
    def cors_allow_origins(self) -> list[str]:
        return self.CORS_ALLOW_ORIGIN_LIST.split('&')
