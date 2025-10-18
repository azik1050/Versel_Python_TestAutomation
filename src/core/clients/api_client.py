import requests
from requests import Response


class ApiClient:
    def __init__(self, base_url: str):
        self._base_url = base_url

    def _get(self, path: str, params=None) -> Response:
        return requests.get(
            url=self._base_url + path,
            params=params
        )

    def _post(self, path: str, json, params=None) -> Response:
        return requests.get(
            url=self._base_url + path,
            json=json,
            params=params
        )
