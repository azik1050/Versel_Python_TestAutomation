import allure
from src.applications.petstore.models.response.user_service_responses import GetUserResponseModel, GetUserFailResponseModel
from src.applications.petstore.utils.allure.enums import Epic, Feature
from src.applications.jira.utils.api_assertions import ApiAssertions
from pytest import mark


@allure.epic(Epic.USER_SERVICE)
@allure.feature(Feature.GET_USER)
class TestGetUser:
    @mark.smoke
    @allure.story("Get valid user")
    def test_get_valid_user(self, user_api, created_user):
        with allure.step("Validation of successful GET /user/{username}"):
            response = user_api.get_user_by_username(created_user.username)
            ApiAssertions.assert_status_code(response, 200)
            ApiAssertions.validate_response_model(response, GetUserResponseModel)


    @mark.regression
    @allure.story("Get not existing user")
    def test_get_invalid_user(self, user_api):
        with allure.step("Validation of failed GET /user/{username}"):
            response = user_api.get_user_by_username("Not existing user")
            ApiAssertions.assert_status_code(response, 404)
            ApiAssertions.validate_response_model(response, GetUserFailResponseModel)


