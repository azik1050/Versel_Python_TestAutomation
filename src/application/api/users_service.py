from requests import Response

from src.core.clients.api_client import ApiClient


class UserService(ApiClient):
    def __init__(self, base_url: str):
        super().__init__(base_url)

    def get_user_by_username(self, username: str) -> Response:
        return self._get(path=f'/user/{username}')

    def create_user(self, username: str) -> Response:
        return self._get(path=f'/user/{username}')