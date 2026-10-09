"""
Directory for describing pydantic schemas.

Schema example:
from pydantic import BaseModel, ConfigDict


class SomeSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    some_field: str
"""
