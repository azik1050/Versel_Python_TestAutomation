import functools
from types import NoneType

from loguru import logger
import allure
from httpx import Client, Response
from pydantic import BaseModel


class ApiClient:
    def __init__(
            self,
            base_url: str,
            timeout: float = 10.0,
    ):
        self.__base_url = base_url
        self.__client = Client(
            timeout=timeout
        )

    @staticmethod
    def __request_logging():
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                path = kwargs.get('path', None)
                body = kwargs.get('json', None)
                headers = kwargs.get('headers', None)
                params = kwargs.get('params', None)

                logger.debug(f"Request PATH: {path}. Body {body}. Header: {headers} Params: {params}")
                try:
                    response = func(*args, **kwargs)
                    logger.debug(f"Response from {kwargs.get('path')}: {response.status_code} | {response.text}")
                    return response
                except Exception as e:
                    error = f"Request to {path} failed. Body {body}. Params: {params}. Exception: {e}"
                    logger.error(error)
                    allure.attach(error, name="Request payload", attachment_type=allure.attachment_type.TEXT)
                    raise Exception(e)
            return wrapper
        return decorator

    @staticmethod
    def __serialize(json) -> dict | list[dict] | NoneType:
        if isinstance(json, dict) or isinstance(json, list) or isinstance(json, NoneType):
            return json
        elif isinstance(json, BaseModel):
            return json.model_dump()
        else:
            raise NotImplementedError(f"Provided request body type is not supported: {type(json)}")

    @__request_logging()
    def __request(self, path: str, method: str, json: dict | list[dict] | BaseModel = None, headers: dict = None, params: dict = None) -> Response:
        allure.attach(
            f"{method} {self.__base_url}{path}\n"
            f"Body {self.__serialize(json)}\n"
            f"Headers: {headers}\n"
            f"Params: {params}",
            name="Request Information",
            attachment_type=allure.attachment_type.TEXT
        )
        return self.__client.request(
            method=method,
            url=f"{self.__base_url}{path}",
            json=self.__serialize(json),
            headers=headers,
            params=params
        )

    def _get(self, path: str, **kwargs) -> Response:
        return self.__request(path=path, method="GET", **kwargs)

    def _post(self, path: str, json: dict | BaseModel | list[dict], **kwargs) -> Response:
        return self.__request(path=path, method="POST", json=json, **kwargs)

    def _put(self, path: str, json: dict | BaseModel | list[BaseModel], **kwargs) -> Response:
        return self.__request(path=path, method="PUT", json=json, **kwargs)

    def _delete(self, path: str, **kwargs) -> Response:
        return self.__request(path=path, method="DELETE", **kwargs)


