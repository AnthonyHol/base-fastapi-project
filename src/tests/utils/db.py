from sqlalchemy import text
from sqlalchemy.engine import make_url
from sqlalchemy.exc import OperationalError, ProgrammingError


from db.session import get_engine


async def create_database(url: str) -> None:
    url_object = make_url(url)
    database = url_object.database
    url_object = url_object.set(database="postgres")

    engine = get_engine(url=url_object, isolation_level="AUTOCOMMIT")
    async with engine.begin() as conn:
        await conn.execute(text(f'CREATE DATABASE "{database}" ENCODING "utf8"'))

    await engine.dispose()


async def database_exists(url: str) -> bool:
    url_object = make_url(url)
    database = url_object.database
    url_object = url_object.set(database="postgres")

    engine = None
    try:
        engine = get_engine(url=url_object, isolation_level="AUTOCOMMIT")
        async with engine.begin() as conn:
            try:
                datname_exists = await conn.scalar(text(f"SELECT 1 FROM pg_database WHERE datname='{database}'"))

            except (ProgrammingError, OperationalError):
                datname_exists = 0

        return bool(datname_exists)

    finally:
        if engine:
            await engine.dispose()


async def drop_database(url: str) -> None:
    url_object = make_url(url)
    database = url_object.database
    url_object = url_object.set(database="postgres")

    engine = get_engine(url=url_object, isolation_level="AUTOCOMMIT")
    async with engine.begin() as conn:
        disc_users = f"""
            SELECT pg_terminate_backend(pg_stat_activity.pid)
            FROM pg_stat_activity
            WHERE pg_stat_activity.datname = '{database}' AND pid <> pg_backend_pid();
        """
        await conn.execute(text(disc_users))

        await conn.execute(text(f'DROP DATABASE "{database}"'))

    await engine.dispose()
