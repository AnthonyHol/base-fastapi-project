import pytest

from schemas.career_history import CreateOrUpdateCareerHistorySchema
from schemas.resume import CreateOrUpdateResumeSchema
from services.resume import ResumeService
from tests.factories.career_history import CurrentCareerHistoryFactory, PastCareerHistoryFactory
from tests.factories.resume import ResumeFactory
from tests.factories.utils import get_random_relative, get_random_course


@pytest.fixture(scope="function")
def resume_with_career_histories_without_ids() -> CreateOrUpdateResumeSchema:
    resume_data = ResumeFactory.build(add_courses=True, add_relatives=True)

    current_career_history = CreateOrUpdateCareerHistorySchema.model_validate(
        CurrentCareerHistoryFactory.build(resume_user_kan_uid=resume_data.resume_user_kan_uid)
    )

    past_career_histories = [
        CreateOrUpdateCareerHistorySchema.model_validate(history)
        for history in PastCareerHistoryFactory.build_batch(
            resume_user_kan_uid=resume_data.resume_user_kan_uid,
            size=4,
        )
    ]

    data = CreateOrUpdateResumeSchema(
        **resume_data.__dict__,
        career_histories=[current_career_history] + past_career_histories,
    )

    for career_history in data.career_histories:
        career_history.id = None

    return data


@pytest.fixture(scope="function")
def mock_fetch_data_from_user_info_api(mocker) -> None:
    mocker.patch.object(
        ResumeService,
        "_ResumeService__fetch_data_from_user_info_api",
        side_effect=[
            [
                get_random_relative(),
            ],
            [
                get_random_course(),
            ],
        ],
    )


@pytest.fixture(scope="function")
def mock_fetch_no_relatives_data_from_user_info_api(mocker) -> None:
    mocker.patch.object(
        ResumeService,
        "_ResumeService__fetch_data_from_user_info_api",
        side_effect=[
            [],
            [
                get_random_course(),
            ],
        ],
    )


@pytest.fixture(scope="function")
def mock_fetch_no_courses_data_from_user_info_api(mocker) -> None:
    mocker.patch.object(
        ResumeService,
        "_ResumeService__fetch_data_from_user_info_api",
        side_effect=[
            [
                get_random_relative(),
            ],
            [],
        ],
    )
