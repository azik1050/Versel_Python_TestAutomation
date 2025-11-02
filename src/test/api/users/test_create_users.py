import allure
from pytest import mark

from src.application.data.user_factory import UserFactory
from src.application.models.response.user_service_responses import CreateUsersResponse
from src.application.utils.api_assertions import ApiAssertions


@mark.smoke
@allure.epic("User Service")
@allure.feature("Create user")
@allure.story("Create several users")
@mark.parametrize('users_count', [1, 2, 10])
def test_create_users(user_api, users_count):
    with allure.step(f'Create users. Number of users: {users_count}'):
        users = UserFactory.create_random_users(users_count)
        response = user_api.create_users(users)
        ApiAssertions.assert_status_code(response, 200)
        ApiAssertions.validate_response_model(response, CreateUsersResponse)

