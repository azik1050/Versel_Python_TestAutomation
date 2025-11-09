from httpx import Response
from src.core.clients.api_client.api_client import ApiClient


class IssueService:
    def __init__(self, api_client: ApiClient):
        self._api = api_client

    def get_issue_fields(self) -> Response:
        return self._api.get('/field')
