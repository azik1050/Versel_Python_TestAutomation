from httpx import Response

from src.applications.petstore.models.request.user_service_requests import CreateUserRequestModel, UpdateUserRequestModel
from src.core.clients.api_client.api_client import ApiClient


class UserService:
    def __init__(self, api_client: ApiClient):
        self._api = api_client

    def get_user_by_username(self, username: str) -> Response:
        return self._api.get(path=f'/user/{username}')

    def create_user(self, user: CreateUserRequestModel) -> Response:
        return self._api.post(path=f'/user', json=user)

    def create_users(self, users: list[dict]) -> Response:
        return self._api.post(path=f'/user/createWithList', json=users)

    def update_user(self, username: str, user: UpdateUserRequestModel) -> Response:
        return self._api.put(path=f'/user/{username}', json=user)

    def delete_user(self, username: str) -> Response:
        return self._api.delete(path=f'/user/{username}')

