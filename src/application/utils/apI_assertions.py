import allure
from requests import Response


class ApiAssertions:
    def assert_status_code(self, response: Response, expected_code: int):
        with allure.step("Verify response code"):
            assert response.status_code == expected_code, f"Actual code: {response.status_code}; Expected: {expected_code}"
