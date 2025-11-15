import allure
from httpx import Response
from loguru import logger


def attach_api_call(response: Response) -> None:
    request = response.request
    with allure.step(f"{request.method} {request.url}"):
        allure.attach(
            f"Payload: {request.content}; \nHeaders: {request.headers};",
            name="API Request",
            attachment_type=allure.attachment_type.TEXT
        )
        allure.attach(
            f"Status code: {response.status_code}; Response body: {response.text}",
            name="API Response",
            attachment_type=allure.attachment_type.TEXT
        )


def attach_and_raise_api_exception(error_text: str, response: Response, e: Exception):
    logger.error(f"{error_text}. Response code: {response.status_code}. Response body: {response.text}")
    attach_api_call(response)
    raise AssertionError(f"Invalid response code. Error message: {e}")
