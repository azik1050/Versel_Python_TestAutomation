import allure
import pytest
from pytest import mark
from src.applications.petstore.data.user_factory import UserFactory
from src.applications.petstore.models.response.user_service_responses import CreateUserResponse
from src.applications.petstore.utils.allure.enums import Epic, Feature
from src.test.api.base_test import BaseTest


@allure.epic(Epic.USER_SERVICE)
@allure.feature(Feature.CREATE_USER)
class TestCreateUser(BaseTest):
    @mark.smoke
    @allure.story("Create user with all fields")
    def test_create_user_success(self, user_api, random_user):
        with self.step("Create a valid random user POST /user"):
            response = user_api.create_user(user=random_user)
            self.assert_status_code(response, 200)
            self.validate_response_model(response, CreateUserResponse)


    @mark.regression
    @allure.story("Create user with missing fields")
    @pytest.mark.parametrize('field_name', [
        'id',
        'username',
        'password',
        'email'
    ])
    def test_create_user_without_field_success(self, user_api, field_name):
        with self.step("Create a valid random user without field POST /user"):
            response = user_api.create_user(user=UserFactory.create_invalid_user_missing_fields(field_name))
            self.assert_status_code(response, 200)
            self.validate_response_model(response, CreateUserResponse)


