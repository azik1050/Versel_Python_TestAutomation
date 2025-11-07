from typing import Type
import allure
from pydantic import BaseModel, ValidationError
from requests import Response
from loguru import logger


class ApiAssertions:
    @staticmethod
    def assert_status_code(response: Response, expected_code: int):
        error_message = f"Actual code: {response.status_code}; Expected: {expected_code}"
        allure.attach(f'{response.status_code}', name="Response Code", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f'{response.text}', name="Response Body", attachment_type=allure.attachment_type.TEXT)
        try:
            with allure.step("Verify response code"):
                assert response.status_code == expected_code, error_message
                logger.debug(f"Valid response for {response.url}: {response.text}")
        except AssertionError as e:
            logger.error(f"Invalid response code: {response.status_code}. Response body: {response.text}")
            raise AssertionError(f"Invalid response code. Error message: {e}")

    @staticmethod
    def assert_field_value(actual_value: str | float, expected_value: str | float):
        try:
            with allure.step("Verify response field value"):
                assert actual_value == expected_value, f"Actual value: {actual_value}; Expected: {expected_value}"
        except AssertionError as e:
            logger.error(f"Invalid response value. Actual value: {actual_value}; Expected: {expected_value}")
            raise AssertionError(f"Invalid response schema: {e}")

    @staticmethod
    def validate_response_model(response: Response, expected_model: Type):
        allure.attach(f'{response.status_code}', name="Response Code", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f'{response.text}', name="Response Body", attachment_type=allure.attachment_type.TEXT)
        try:
            with allure.step("Verify response body model"):
                expected_model(**response.json())
                logger.debug(f"Valid response model for {response.url}: {response.text}")
        except ValidationError as e:
            logger.error(f"Invalid response body, response body: {response.text}. Error: {e}")
            raise AssertionError(f"Invalid response schema from API. Error: {e}")
