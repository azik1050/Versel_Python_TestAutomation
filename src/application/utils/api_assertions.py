import allure
from requests import Response
import logging


class ApiAssertions:
    @staticmethod
    def assert_status_code(response: Response, expected_code: int):
        error_message = f"Actual code: {response.status_code}; Expected: {expected_code}"
        try:
            with allure.step("Verify response code"):
                assert response.status_code == expected_code, error_message
        except AssertionError:
            logging.error(error_message)

