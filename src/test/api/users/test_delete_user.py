import allure

from src.application.utils.allure.enums import Epic, Feature
from src.application.utils.api_assertions import ApiAssertions
from pytest import mark


@allure.epic(Epic.USER_SERVICE)
@allure.feature(Feature.DELETE_USER)
class TestDeleteUser:
    @mark.smoke
    @allure.story("Delete valid user")
    def test_delete_user(self, created_user, user_api):
        with allure.step("Delete user"):
            response = user_api.delete_user(created_user.username)
            ApiAssertions.assert_status_code(response, 200)

    @mark.regression
    @allure.story("Delete not existing user")
    def test_delete_not_existing_user(self, user_api):
        with allure.step("Delete not existing user"):
            response = user_api.delete_user('Noname')
            ApiAssertions.assert_status_code(response, 404)

