import typing

from factory.base import Factory
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.base import BaseModel


class BaseFactory(Factory[typing.Any]):
    @classmethod
    def _create(cls, model_class, *args, **kwargs) -> typing.Coroutine[typing.Any, typing.Any, BaseModel]:
        async def create_coroutine(*args, **kwargs) -> BaseModel:
            session: AsyncSession = kwargs.pop('session')
            model = model_class(*args, **kwargs)
            session.add(model)
            await session.commit()
            await session.refresh(model)
            return model

        return create_coroutine(*args, **kwargs)

    @classmethod
    async def create_batch(cls, size: int, **kwargs: typing.Any) -> list[typing.Any]:  # type: ignore[override]
        return [await cls.create(**kwargs) for i in range(size)]
