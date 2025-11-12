from typing import Type
import allure
from pydantic import BaseModel, ValidationError
from requests import Response
from loguru import logger
from src.core.utils.allure import attach_api_call
from src.core.utils.data_utils import get_json_value
from src.core.utils.general_utils import to_json_index_str


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

    @staticmethod
    def assert_key_value(response: Response, key: str | list, value: str):
        try:
            with allure.step("Assert response field value"):
                actual_value = get_json_value(key, response)

                assert actual_value == value, f"Key {key} is not equal to value {value}"

                allure.attach(
                    f"JSON{to_json_index_str(key)} = {value}",
                    name="Response JSON value",
                    attachment_type=allure.attachment_type.TEXT
                )
                logger.debug(f"Valid key | value assertion for {response.url} | {response.text}")
        except Exception as e:
            ApiAssertions._attach_and_raise("Field Value Mismatch", response, e)
