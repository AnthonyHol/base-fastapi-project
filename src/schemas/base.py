from datetime import datetime

from pydantic import ConfigDict, BaseModel, field_validator

from core.constants import moscow_timezone


class BaseOrmSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class CreatedAtMixin(BaseModel):
    created_at: datetime

    @field_validator("created_at")
    def format_created_at(cls, v):
        return v.astimezone(moscow_timezone)



class UpdatedAtMixin(BaseModel):
    updated_at: datetime

    @field_validator("updated_at")
    def format_updated_at(cls, v):
        return v.astimezone(moscow_timezone)
