from httpx import Response
from pydantic import BaseModel

from src.application.models.request.user_service_requests import CreateUserRequestModel, UpdateUserRequestModel
from src.core.clients.api_client import ApiClient


class UserService(ApiClient):
    def __init__(self, base_url: str):
        super().__init__(base_url)

    def get_user_by_username(self, username: str) -> Response:
        return self._get(path=f'/user/{username}')

    def create_user(self, user: CreateUserRequestModel) -> Response:
        if isinstance(user, CreateUserRequestModel):
            return self._post(path=f'/user', json=user.model_dump())
        elif isinstance(user, dict):
            return self._post(path=f'/user', json=user)

    def create_users(self, users: list[dict]) -> Response:
        return self._post(path=f'/user/createWithList', json=users)

    def update_user(self, username: str, user: UpdateUserRequestModel) -> Response:
        return self._put(path=f'/user/{username}', json=user.model_dump())

    def delete_user(self, username: str) -> Response:
        return self._delete(path=f'/user/{username}')

