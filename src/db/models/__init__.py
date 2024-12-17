"""
Directory for describing models.

Import model here to enable alembic autogenerate.

Model example:
from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column


class SomeModel(BaseModel):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    some_field: Mapped[str] = mapped_column(String(length=255), nullable=False)

    def __str__(self) -> str:
        return f"Some model #{self.id}"
"""

__all__ = ("BaseModel",)


from db.models.base import BaseModel
