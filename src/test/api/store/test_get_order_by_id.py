import allure
import pytest

from src.application.models.response.store_service_responses import GetOrderByIdResponseModel
from src.application.utils.allure.enums import Epic, Feature
from src.application.utils.api_assertions import ApiAssertions
from pytest import mark


@allure.epic(Epic.STORE_SERVICE)
@allure.feature(Feature.GET_ORDER_BY_ID)
class TestGetOrderById:
    @allure.story("Get Order")
    @mark.smoke
    def test_get_order_by_id(self, store_api):
        response = store_api.get_order_by_id(1)
        ApiAssertions.assert_status_code(response, 200)
        ApiAssertions.validate_response_model(response, GetOrderByIdResponseModel)
