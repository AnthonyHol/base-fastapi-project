from datetime import datetime

from pydantic import BaseModel, ConfigDict, field_validator

from core.constants import moscow_timezone


class BaseOrmSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class CreatedAtMixin(BaseModel):
    created_at: datetime

    @field_validator('created_at')
    @classmethod
    def format_created_at(cls, v: datetime) -> datetime:
        return v.astimezone(moscow_timezone)


class UpdatedAtMixin(BaseModel):
    updated_at: datetime

    @field_validator('updated_at')
    @classmethod
    def format_updated_at(cls, v: datetime) -> datetime:
        return v.astimezone(moscow_timezone)
