import functools
from collections.abc import AsyncGenerator

from redis.asyncio import Redis, from_url

from core.config import settings

type AsyncRedis = Redis


@functools.lru_cache
def get_redis_connection() -> AsyncRedis:
    return from_url(settings().REDIS_DSN, encoding='utf-8', decode_responses=True)


async def get_redis() -> AsyncGenerator[AsyncRedis]:
    async with get_redis_connection() as redis:
        yield redis
