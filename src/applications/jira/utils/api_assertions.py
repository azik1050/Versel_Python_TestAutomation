from typing import Type
import allure
from pydantic import BaseModel, ValidationError
from requests import Response
from loguru import logger

from src.core.utils.allure import attach_api_call


class ApiAssertions:
    @staticmethod
    def _attach_response(response: Response):
        allure.attach(
            str(response.status_code),
            name="Response Code",
            attachment_type=allure.attachment_type.TEXT
        )
        allure.attach(
            str(response.text),
            name="Response Body",
            attachment_type=allure.attachment_type.TEXT
        )

    @staticmethod
    def assert_status_code(response: Response, expected_code: int):
        error_message = f"Actual code: {response.status_code}; Expected: {expected_code}"
        ApiAssertions._attach_response(response)
        try:
            with allure.step("Verify response code"):
                assert response.status_code == expected_code, error_message
                logger.debug(f"Valid received response for {response.url}: {response.text}")
        except AssertionError as e:
            logger.error(f"Invalid response code: {response.status_code}. Response body: {response.text}")
            attach_api_call(response)
            raise AssertionError(f"Invalid response code. Error message: {e}")

    @staticmethod
    def validate_response_model(response: Response, expected_model: type[BaseModel]):
        # ApiAssertions._attach_response(response)
        try:
            with allure.step("Verify response body model"):
                expected_model.model_validate(response.json())
                logger.debug(f"Valid response model for {response.url}: {response.text}")
        except ValidationError as e:
            logger.error(f"Invalid response body, response body: {response.text}. Error: {e}")
            attach_api_call(response)
            raise AssertionError(f"Invalid response schema from API. Error: {e}")
