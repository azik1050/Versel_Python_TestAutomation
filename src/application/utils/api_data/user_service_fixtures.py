import pytest
from src.application.entities.user_factory import UserFactory
from src.application.models.response.user_service_responses import CreateUserResponse
from src.application.utils.api_assertions import ApiAssertions


@pytest.fixture
def random_user():
    return UserFactory.create_random_user()


@pytest.fixture
def created_user(user_api, random_user):
    response = user_api.create_user(random_user)
    ApiAssertions.assert_status_code(response, 200)
    ApiAssertions.validate_response_model(response, CreateUserResponse)
    return random_user
