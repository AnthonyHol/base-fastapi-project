"""
Directory for service-based business-logic layer.

Service Example:
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.some_model_repository import SomeModelRepository
from db.session import get_session
from db.redis import get_redis, AsyncRedis
from schemas.some_model import SomeModelSchema


class SomeService:
    def __init__(
        self,
        session: AsyncSession = Depends(get_session),
        redis: AsyncRedis = Depends(get_redis),
    ) -> None:
        self.redis = redis
        self.some_model_repository = SomeModelRepository(session=session)

    async def get_instances() -> list[SomeModel]:
        return await self.some_model_repository.get_instances()

    async def get_cached_instance(instance_id: int) -> SomeModelSchema:
        raw_instance = await self.redis.get(f"some-model-key:{instance_id}")
        return SomeModelSchema.parse_raw(raw_instance)
"""
