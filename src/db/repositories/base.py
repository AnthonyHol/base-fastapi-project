from abc import ABC
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_session


class BaseDatabaseRepository(ABC):
    _session: AsyncSession

    def __init__(self, session: Annotated[AsyncSession, Depends(get_session)]) -> None:
        self._session = session
