from typing import Type
import allure
from pydantic import BaseModel, ValidationError
from requests import Response
from loguru import logger

from src.core.utils.allure import attach_api_call


class ApiAssertions:
    @staticmethod
    def _attach_and_raise(error_text: str, response: Response, e: Exception) -> None:
        logger.error(f"{error_text}. Response code: {response.status_code}. Response body: {response.text}")
        attach_api_call(response)
        raise AssertionError(f"Invalid response code. Error message: {e}")

    @staticmethod
    def assert_status_code(response: Response, expected_code: int):
        try:
            with allure.step("Verify response code"):
                assert response.status_code == expected_code, f"Actual code: {response.status_code}; Expected: {expected_code}"
                allure.attach(
                    str(response.status_code),
                    name="Response Code",
                    attachment_type=allure.attachment_type.TEXT
                )
                logger.debug(f"Valid response code for: {response.url} | {response.status_code}")
        except AssertionError as e:
            ApiAssertions._attach_and_raise("Invalid Response Code", response, e)

    @staticmethod
    def validate_response_model(response: Response, expected_model: type[BaseModel]):
        try:
            with allure.step("Verify response body model"):
                expected_model.model_validate(response.json())
                allure.attach(
                    response.text,
                    name="Response Body",
                    attachment_type=allure.attachment_type.JSON
                )
                logger.debug(f"Valid response model for {response.url} | {response.text}")
        except ValidationError as e:
            ApiAssertions._attach_and_raise("Invalid Response Body", response, e)
