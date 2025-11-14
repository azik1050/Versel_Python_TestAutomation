import allure
from pytest import mark
from src.applications.petstore.utils.allure.enums import Epic, Feature
from src.applications.jira.utils.api_assertions import ApiAssertions
from src.test.api.base_test import BaseTest


@allure.epic(Epic.STORE_SERVICE)
@allure.feature(Feature.GET_INVENTORY)
class TestGetInventory(BaseTest):
    @allure.story("Get inventory")
    @mark.smoke
    def test_get_inventory(self, store_api):
        with allure.step("Get Inventory"):
            response = store_api.get_inventory()
            self.assert_status_code(response, 200)

