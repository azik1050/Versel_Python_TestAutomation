import allure
from src.applications.petstore.utils.allure.enums import Epic, Feature
from src.applications.jira.utils.api_assertions import ApiAssertions
from pytest import mark
from src.test.api.base_test import BaseTest


@allure.epic(Epic.USER_SERVICE)
@allure.feature(Feature.UPDATE_USER)
class TestUpdateUser(BaseTest):
    @mark.smoke
    @allure.story("Update valid user")
    def test_update_user(self, created_user, user_api):
        with allure.step("Update user"):
            response = user_api.update_user(created_user.username, created_user)
            self.assert_status_code(response, 200)


