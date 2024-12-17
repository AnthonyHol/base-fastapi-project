"""
Directory for describing pydantic schemas.

Schema example:
from pydantic import BaseModel

from schemas.mixins import OrjsonConfigMixin

class SomeSchema(BaseModel):
    some_field: str

    class Config(OrjsonConfigMixin):
        pass
"""
