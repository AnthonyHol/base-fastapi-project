from core.exceptions import career_history_not_found_exception
from schemas.career_history import GetCareerHistorySchema
from tests.career_history.test_integration.base import BaseTestCareerHistory
from tests.factories.career_history import CurrentCareerHistoryFactory, PastCareerHistoryFactory
from tests.factories.resume import ResumeFactory
from tests.factories.utils import get_random_int
import pytest
from httpx import AsyncClient

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status


class TestGetCareerHistory(BaseTestCareerHistory):
    @pytest.mark.asyncio
    async def test__get_career_history__success_case_for_current_job(
        self,
        async_db_session: AsyncSession,
        api_client: AsyncClient,
    ):
        resume = await ResumeFactory.create(session=async_db_session)
        current_career_history = await CurrentCareerHistoryFactory.create(
            session=async_db_session, resume_user_kan_uid=resume.resume_user_kan_uid
        )

        response = await api_client.get(f"{self.url}/{current_career_history.id}")
        response_json = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert GetCareerHistorySchema.model_validate(current_career_history).model_dump(mode="json") == response_json

    @pytest.mark.asyncio
    async def test__get_career_history__success_case_for_past_job(
        self,
        async_db_session: AsyncSession,
        api_client: AsyncClient,
    ):
        resume = await ResumeFactory.create(session=async_db_session)
        past_career_history = await PastCareerHistoryFactory.create(
            session=async_db_session, resume_user_kan_uid=resume.resume_user_kan_uid
        )

        response = await api_client.get(f"{self.url}/{past_career_history.id}")
        response_json = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert GetCareerHistorySchema.model_validate(past_career_history).model_dump(mode="json") == response_json

    @pytest.mark.asyncio
    async def test__get_career_history__not_found(
        self,
        api_client: AsyncClient,
    ):
        response = await api_client.get(f"{self.url}/{get_random_int()}")
        response_json = response.json()

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response_json["detail"] == career_history_not_found_exception.detail
