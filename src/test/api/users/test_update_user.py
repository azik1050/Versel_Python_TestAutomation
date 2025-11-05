import allure

from src.application.utils.allure.enums import Epic, Feature
from src.application.utils.api_assertions import ApiAssertions
from pytest import mark


@allure.epic(Epic.USER_SERVICE)
@allure.feature(Feature.UPDATE_USER)
class TestUpdateUser:
    @mark.smoke
    @allure.story("Update valid user")
    def test_update_user(self, created_user, user_api):
        with allure.step("Update user"):
            response = user_api.update_user(created_user)
            ApiAssertions.assert_status_code(response, 200)


