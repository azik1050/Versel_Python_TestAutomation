from requests import Response
from src.application.models.request.user_service_requests import CreateUserRequestModel
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
