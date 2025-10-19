import allure
import pytest

from src.application.entities.user_factory import UserFactory
from src.application.models.response.user_service_responses import CreateUserResponse
from src.application.utils.api_assertions import ApiAssertions


@allure.epic("User service")
@allure.feature("User creation")
@allure.story("Create user with all fields")
def test_create_user_success(user_api, random_user):
    with allure.step("Create a valid random user POST /user"):
        response = user_api.create_user(user=random_user)
        body = response.json()
        ApiAssertions.assert_status_code(response, 200)
        ApiAssertions.validate_response_model(response, CreateUserResponse)
        assert body["code"] == 200, "Invalid response body code"
        assert body["type"] == "unknown", "Invalid response body type"


@allure.epic("User service")
@allure.feature("User creation")
@allure.story("Create user with missing fields")
@pytest.mark.parametrize('field_name', [
    'id',
    'username',
    'password',
    'email'
])
def test_create_user_without_field_success(user_api, field_name):
    with allure.step("Create a valid random user without field POST /user"):
        response = user_api.create_user(user=UserFactory.create_invalid_user_missing_fields(field_name))
        body = response.json()
        ApiAssertions.assert_status_code(response, 200)
        ApiAssertions.validate_response_model(response, CreateUserResponse)
        assert body["code"] == 200, "Invalid response body code"
        assert body["type"] == "unknown", "Invalid response body type"


