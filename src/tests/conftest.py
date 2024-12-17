import asyncio
import os
import typing

import alembic.command
import pytest
import pytest_asyncio
from alembic.config import Config
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from httpx._transports.asgi import ASGITransport

from core.config import settings
from db import session
from db.session import get_engine
from main import app
from tests.utils.db import create_database, database_exists, drop_database

__all__ = (
    "resume_with_career_histories_without_ids",
    "mock_fetch_data_from_user_info_api",
    "mock_fetch_no_relatives_data_from_user_info_api",
    "mock_fetch_no_courses_data_from_user_info_api",
)

pytestmark = pytest.mark.asyncio


@pytest.fixture(scope="session")
def mock_settings() -> None:
    settings.cache_clear()
    os.environ["ENVIRONMENT"] = "test"


@pytest.fixture(scope="session")
def event_loop() -> typing.Generator[asyncio.AbstractEventLoop, None, None]:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    yield loop

    loop.close()


@pytest_asyncio.fixture(scope="session")
async def async_db_engine(mock_settings) -> typing.AsyncGenerator[AsyncEngine, None]:
    if await database_exists(settings().postgres_dsn):
        await drop_database(settings().postgres_dsn)

    await create_database(settings().postgres_dsn)

    engine = get_engine()
    await engine.dispose()

    yield engine

    await engine.dispose()
    await drop_database(settings().postgres_dsn)


@pytest.fixture(scope="session")
def apply_migrations() -> typing.Generator[None, None, None]:
    config = Config(os.path.join(settings().BASE_DIR, "alembic.ini"))
    config.set_main_option("script_location", os.path.join(settings().BASE_DIR, "db/migrations"))
    alembic.command.upgrade(config, "head")
    yield
    alembic.command.downgrade(config, "base")


@pytest_asyncio.fixture(scope="function")
async def async_db_session(async_db_engine: AsyncEngine, apply_migrations) -> typing.AsyncGenerator[AsyncSession, None]:
    async with async_db_engine.connect() as conn:
        async with conn.begin() as transaction:
            session = AsyncSession(bind=conn, expire_on_commit=False)

            yield session

            await transaction.rollback()


@pytest_asyncio.fixture(scope="function")
async def api_client(async_db_session: AsyncSession) -> typing.AsyncGenerator[AsyncClient, None]:
    app.dependency_overrides[session.get_session] = lambda: async_db_session

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:  # type: ignore
        yield client
