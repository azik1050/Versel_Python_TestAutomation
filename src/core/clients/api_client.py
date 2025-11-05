import functools
import logging

import allure
import requests
from requests import Response


class ApiClient:
    def __init__(self, base_url: str):
        self._base_url = base_url
        self.__session = requests.Session()

    @staticmethod
    def __request_logging():
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                path = kwargs.get('path', None)
                body = kwargs.get('json', None)
                params = kwargs.get('params', None)

                logging.debug(f"Request PATH: {path}. Request Body {body}. Params: {params}")
                try:
                    response = func(*args, **kwargs)
                    logging.debug(f"Response from {kwargs.get('path')}: {response.status_code} | {response.text}")
                    return response
                except Exception as e:
                    error = f"Request to {path} failed. Body {body}. Params: {params}. Exception: {e}"
                    logging.error(error)
                    allure.attach(error, name="Request payload", attachment_type=allure.attachment_type.TEXT)
                    raise Exception(e)
            return wrapper
        return decorator

    @__request_logging()
    def _get(self, path: str, headers: dict = None, params=None) -> Response:
        allure.attach(
            f"PUT {path}. Params : {params}",
            name="Request information",
            attachment_type=allure.attachment_type.TEXT
        )
        response = self.__session.get(
            url=self._base_url + path,
            headers=headers,
            params=params
        )
        return response

    @__request_logging()
    def _post(self, path: str, json, headers: dict = None, params=None) -> Response:
        allure.attach(
            f"POST {path}. JSON: {json}. Params : {params}",
            name="Request information",
            attachment_type=allure.attachment_type.TEXT
        )
        response = self.__session.post(
            url=self._base_url + path,
            json=json,
            headers=headers,
            params=params
        )
        return response

    @__request_logging()
    def _put(self, path: str, json, headers: dict = None, params=None) -> Response:
        allure.attach(
            f"PUT {path}. JSON: {json}. Params : {params}",
            name="Request information",
            attachment_type=allure.attachment_type.TEXT
        )
        return self.__session.put(
            url=self._base_url + path,
            json=json,
            headers=headers,
            params=params
        )

    @__request_logging()
    def _delete(self, path: str, headers: dict = None, params=None) -> Response:
        allure.attach(
            f"DELETE {path}. Params : {params}",
            name="Request information",
            attachment_type=allure.attachment_type.TEXT
        )
        response = self.__session.delete(
            url=self._base_url + path,
            headers=headers,
            params=params
        )
        return response
