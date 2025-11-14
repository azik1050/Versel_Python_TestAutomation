import allure
from src.applications.petstore.models.response.store_service_responses import GetOrderByIdResponseModel
from src.applications.petstore.utils.allure.enums import Epic, Feature
from src.applications.jira.utils.api_assertions import ApiAssertions
from pytest import mark

from src.test.api.base_test import BaseTest


@allure.epic(Epic.STORE_SERVICE)
@allure.feature(Feature.GET_ORDER_BY_ID)
class TestGetOrderById(BaseTest):
    @allure.story("Get Order")
    @mark.smoke
    def test_get_order_by_id(self, store_api):
        response = store_api.get_order_by_id(1)
        self.assert_status_code(response, 200)
        self.validate_response_model(response, GetOrderByIdResponseModel)
