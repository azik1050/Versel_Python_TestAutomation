import pytest
from src.applications.jira.api.issue_service import IssueService
from src.core.clients.api_client import ApiClient
from src.core.clients.api_client.auth import BasicAuth
from src.core.config.settings import TestConfig


@pytest.fixture(scope="session")
def jira_api():
    return IssueService(
        ApiClient(
            base_url=TestConfig.API.BASE_JIRA_API_URL,
            auth=BasicAuth(TestConfig.API.JIRA_USER, TestConfig.API.JIRA_PASSWORD)
        )
    )