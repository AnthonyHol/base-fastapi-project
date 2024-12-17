"""
Directory for describing repositories for work with database.

Repository example:
from sqlalchemy import select

from db.repositories.base import BaseDatabaseRepository


class SomeModelDatabaseRepository(BaseDatabaseRepository):
    async def get_by_id(id: int) -> SomeModel:
        query = select(SomeModel).filter(SomeModel.id == id)
        query_result = await self._session.scalars(query)

        return query_result.scalars().first()

"""
