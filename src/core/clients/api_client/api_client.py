import functools
from types import NoneType
from loguru import logger
import allure
from httpx import Client, Response, Auth
from pydantic import BaseModel

from src.core.utils.allure import attach_api_call


class ApiClient:
    def __init__(
            self,
            base_url: str,
            headers: dict = None,
            timeout: float = 10.0,
            auth: Auth = None
    ):
        self.__base_url = base_url
        self.__client = Client(
            headers=headers,
            timeout=timeout,
            auth=auth
        )

    @staticmethod
    def __serialize(json) -> dict | list[dict] | NoneType:
        if isinstance(json, dict) or isinstance(json, list) or isinstance(json, NoneType):
            return json
        elif isinstance(json, BaseModel):
            return json.model_dump(by_alias=True)
        else:
            raise NotImplementedError(f"Provided request body type is not supported: {type(json)}")

    def _request(
            self,
            path: str,
            method: str,
            json: dict | list[dict] | BaseModel | type[BaseModel] = None,
            headers: dict = None, params: dict = None
    ) -> Response:
        url = f"{self.__base_url}{path}"
        body = self.__serialize(json)

        logger.debug(f"\nRequest {method} {url}\nBody: {body}\nHeaders: {headers}\nParams: {params}")

        response = self.__client.request(
            method=method,
            url=f"{self.__base_url}{path}",
            json=self.__serialize(json),
            headers=headers,
            params=params
        )

        logger.debug(f"\nResponse {method} {url}\nStatus: {response.status_code}\nBody: {response.text}")

        return response


    def get(self, path: str, **kwargs) -> Response:
        return self._request(path=path, method="GET", **kwargs)


    def post(self, path: str, json: dict | BaseModel | type[BaseModel] | list[dict], **kwargs) -> Response:
        return self._request(path=path, method="POST", json=json, **kwargs)


    def put(self, path: str, json: dict | BaseModel | list[BaseModel], **kwargs) -> Response:
        return self._request(path=path, method="PUT", json=json, **kwargs)


    def delete(self, path: str, **kwargs) -> Response:
        return self._request(path=path, method="DELETE", **kwargs)
