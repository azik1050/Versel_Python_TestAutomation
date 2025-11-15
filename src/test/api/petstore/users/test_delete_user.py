import allure
from src.applications.petstore.utils.allure.enums import Epic, Feature
from src.applications.jira.utils.api_assertions import ApiAssertions
from pytest import mark

from src.test.api.base_test import BaseTest


@allure.epic(Epic.USER_SERVICE)
@allure.feature(Feature.DELETE_USER)
class TestDeleteUser(BaseTest):
    @mark.smoke
    @allure.story("Delete valid user")
    def test_delete_user(self, created_user, user_api):
        with self.step("Delete user"):
            response = user_api.delete_user(created_user.username)
            self.assert_status_code(response, 200)

    @mark.regression
    @allure.story("Delete not existing user")
    def test_delete_not_existing_user(self, user_api):
        with self.step("Delete not existing user"):
            response = user_api.delete_user('Noname')
            self.assert_status_code(response, 404)

