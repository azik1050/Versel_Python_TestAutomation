import allure
import pytest
from pytest import mark
from src.application.data.user_factory import UserFactory
from src.application.models.response.user_service_responses import CreateUserResponse
from src.application.utils.api_assertions import ApiAssertions


@mark.smoke
@allure.epic("User service")
@allure.feature("User creation")
@allure.story("Create user with all fields")
def test_create_user_success(user_api, random_user):
    with allure.step("Create a valid random user POST /user"):
        response = user_api.create_user(user=random_user)
        ApiAssertions.assert_status_code(response, 200)
        ApiAssertions.validate_response_model(response, CreateUserResponse)


@mark.regression
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
        ApiAssertions.assert_status_code(response, 200)
        ApiAssertions.validate_response_model(response, CreateUserResponse)


