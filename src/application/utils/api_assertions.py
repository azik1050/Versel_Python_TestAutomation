from typing import Type
import allure
from pydantic import BaseModel, ValidationError
from requests import Response
import logging


class ApiAssertions:
    @staticmethod
    def assert_status_code(response: Response, expected_code: int):
        error_message = f"Actual code: {response.status_code}; Expected: {expected_code}"
        try:
            with allure.step("Verify response code"):
                assert response.status_code == expected_code, error_message
                logging.debug(f"Valid response for {response.url}: {response.text}")
        except AssertionError as e:
            logging.error(f"Invalid response code: {response.status_code}. Response body: {response.text}")
            allure.attach(response.text, name="Response body", attachment_type=allure.attachment_type.TEXT)
            raise AssertionError(f"Invalid response code. Error message: {e}")

    @staticmethod
    def assert_field_value(actual_value: str | float, expected_value: str | float):
        try:
            assert actual_value == expected_value, f"Actual value: {actual_value}; Expected: {expected_value}"
        except AssertionError as e:
            logging.error(f"Invalid response value. Actual value: {actual_value}; Expected: {expected_value}")
            raise AssertionError(f"Invalid response schema: {e}")

    @staticmethod
    def validate_response_model(response: Response, expected_model: Type):
        try:
            with allure.step("Verify response body model"):
                expected_model(**response.json())
        except ValidationError as e:
            logging.error(f"Invalid response body, response body: {response.text}. Error: {e}")
            allure.attach(response.text, name="Response body", attachment_type=allure.attachment_type.TEXT)
            raise AssertionError("Invalid response schema from API")
