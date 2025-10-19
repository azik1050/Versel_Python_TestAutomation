from typing import Type

import allure
from pydantic import BaseModel, ValidationError
from requests import Response
import logging


# TODO replace print with logging

class ApiAssertions:
    @staticmethod
    def assert_status_code(response: Response, expected_code: int):
        error_message = f"Actual code: {response.status_code}; Expected: {expected_code}"
        try:
            with allure.step("Verify response code"):
                assert response.status_code == expected_code, error_message
        except AssertionError as e:
            print(response.json())
            raise AssertionError(f"Invalid response schema: {e}")

    @staticmethod
    def validate_response_model(response: Response, expected_model: Type):
        try:
            with allure.step("Verify response body model"):
                expected_model(**response.json())
        except ValidationError as e:
            print(e)
            print(response.json())
            raise AssertionError("Invalid response schema from API")


