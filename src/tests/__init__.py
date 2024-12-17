"""
Directory for unit and integration tests.

Test example:
/src/tests/users/test_integration/test_get_all_users.py

import pytest
import random
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from httpx import AsyncClient

from db.models import User
from tests.factories.user import UserFactory


@pytest.mark.asyncio
async def test__get_all_users__success_case(async_db_session: AsyncSession, api_client: AsyncClient) -> None:
    users_from_db: list[User] = await UserFactory.create_batch(
        size=random.randint(5, 10),
        is_active=True,
        session=async_db_session,
    )

    response = await api_client.get("/api/v1/users")
    response_data = response.json()

    assert len(users_from_db) == len(response_data)
    and more asserts...
"""
