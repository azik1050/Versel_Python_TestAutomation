import logging

import requests
from requests import Response


class ApiClient:
    def __init__(self, base_url: str):
        self._base_url = base_url

    def _get(self, path: str, params=None) -> Response:
        logging.debug(f"GET {self._base_url}/{path}. Params: {params}")
        return requests.get(
            url=self._base_url + path,
            params=params
        )

    def _post(self, path: str, json, params=None) -> Response:
        logging.debug(f"GET {self._base_url}/{path}. Body: {json}. Params: {params}")
        return requests.post(
            url=self._base_url + path,
            json=json,
            params=params
        )

    def _put(self, path: str, json, params=None) -> Response:
        logging.debug(f"GET {self._base_url}/{path}. Body: {json}. Params: {params}")
        return requests.put(
            url=self._base_url + path,
            json=json,
            params=params
        )

    def _delete(self, path: str, params=None) -> Response:
        logging.debug(f"DELETE {self._base_url}/{path}. Params: {params}")
        return requests.delete(
            url=self._base_url + path,
            params=params
        )
