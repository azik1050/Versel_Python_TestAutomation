import allure
from pytest import mark
from src.applications.petstore.data.user_factory import UserFactory
from src.applications.petstore.models.response.user_service_responses import CreateUsersResponse
from src.applications.petstore.utils.allure.enums import Epic, Feature
from src.applications.jira.utils.api_assertions import ApiAssertions
from src.test.api.base_test import BaseTest


@allure.epic(Epic.USER_SERVICE)
@allure.feature(Feature.CREATE_USERS)
class TestCreateUsers(BaseTest):
    @mark.smoke
    @allure.story("Create several users")
    @mark.parametrize('users_count', [1, 2, 10])
    def test_create_users(self, user_api, users_count):
        with allure.step(f'Create users. Number of users: {users_count}'):
            users = UserFactory.create_random_users(users_count)
            response = user_api.create_users(users)
            self.assert_status_code(response, 200)
            self.validate_response_model(response, CreateUsersResponse)

