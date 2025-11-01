import allure
from src.application.utils.api_assertions import ApiAssertions
from pytest import mark


@mark.smoke
@allure.epic("User Service")
@allure.feature("Delete user")
@allure.story("Delete valid user")
def test_delete_user(created_user, user_api):
    with allure.step("Delete user"):
        response = user_api.delete_user(created_user)
        ApiAssertions.assert_status_code(response, 200)


