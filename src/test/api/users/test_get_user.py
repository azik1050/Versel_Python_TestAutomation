import allure
from src.application.models.response.user_service_responses import GetUserResponseModel, GetUserFailResponseModel
from src.application.utils.api_assertions import ApiAssertions


@allure.epic("User Service")
@allure.feature("Get user")
@allure.story("Get valid user")
def test_get_valid_user(user_api, created_user):
    with allure.step("Validation of successful GET /user/{username}"):
        response = user_api.get_user_by_username(created_user.username)
        ApiAssertions.assert_status_code(response, 200)
        ApiAssertions.validate_response_model(response, GetUserResponseModel)


@allure.epic("User Service")
@allure.feature("Get user")
@allure.story("Get not existing user")
def test_get_invalid_user(user_api):
    with allure.step("Validation of failed GET /user/{username}"):
        response = user_api.get_user_by_username("Not existing user")
        ApiAssertions.assert_status_code(response, 404)
        ApiAssertions.validate_response_model(response, GetUserFailResponseModel)


