import os
from collections.abc import AsyncGenerator, Generator

import alembic.command
import pytest
import pytest_asyncio
from alembic.config import Config
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from core.config import settings
from db import session
from db.session import get_engine
from main import app
from tests.utils.db import create_database, database_exists, drop_database


@pytest.fixture(scope="session")
def mock_settings() -> None:
    settings.cache_clear()
    os.environ["ENVIRONMENT"] = "test"


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def async_db_engine(mock_settings) -> AsyncGenerator[AsyncEngine]:
    if await database_exists(settings().postgres_dsn):
        await drop_database(settings().postgres_dsn)

    await create_database(settings().postgres_dsn)

    engine = get_engine()
    await engine.dispose()

    yield engine

    await engine.dispose()
    await drop_database(settings().postgres_dsn)


@pytest.fixture(scope="session")
def apply_migrations() -> Generator[None]:
    config = Config(os.path.join(settings().BASE_DIR, "alembic.ini"))
    config.set_main_option("script_location", os.path.join(settings().BASE_DIR, "db/migrations"))
    alembic.command.upgrade(config, "head")
    yield
    alembic.command.downgrade(config, "base")


@pytest_asyncio.fixture(scope="function", loop_scope="session")
async def async_db_session(async_db_engine: AsyncEngine, apply_migrations) -> AsyncGenerator[AsyncSession]:
    async with async_db_engine.connect() as conn, conn.begin() as transaction:
        session = AsyncSession(bind=conn, expire_on_commit=False)

        yield session

        await transaction.rollback()


@pytest_asyncio.fixture(scope="function", loop_scope="session")
async def api_client(async_db_session: AsyncSession) -> AsyncGenerator[AsyncClient]:
    app.dependency_overrides[session.get_session] = lambda: async_db_session

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client
