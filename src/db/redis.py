import functools
import typing

from redis.asyncio import Redis, from_url

from core.config import settings

if typing.TYPE_CHECKING:
    AsyncRedis: typing.TypeAlias = Redis[typing.Any]
else:
    AsyncRedis: typing.TypeAlias = Redis


@functools.lru_cache
def get_redis_connection() -> AsyncRedis:
    return from_url(settings().REDIS_DSN, encoding="utf-8", decode_responses=True)


async def get_redis() -> typing.AsyncGenerator[AsyncRedis, None]:
    async with get_redis_connection() as redis:
        yield redis
