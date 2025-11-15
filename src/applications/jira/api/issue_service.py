from loguru import logger
from httpx import Response
from src.applications.jira.models.request.issues_requests import (
    CreateCustomFieldRequestModel,
    UpdateCustomFieldRequestModel
)
from src.core.clients.api_client.api_client import ApiClient


class IssueService:
    def __init__(self, api_client: ApiClient):
        self._api = api_client

    def get_issue_fields(self) -> Response:
        return self._api.get('/field')

    def create_custom_field(self, issue_field: CreateCustomFieldRequestModel) -> Response:
        return self._api.post('/field', issue_field)

    def update_custom_field(self, issue_field: UpdateCustomFieldRequestModel, field_id: str) -> Response:
        return self._api.put(f'/field/{field_id}', issue_field)

    def delete_custom_field(self, field_id: str) -> Response:
        return self._api.delete(f'/field/{field_id}')

    def move_custom_field_to_trash(self, field_id: str) -> Response:
        return self._api.post(f'/field/{field_id}/trash')

    def restore_custom_field_from_trash(self, field_id: str) -> Response:
        return self._api.post(f'/field/{field_id}/restore')

