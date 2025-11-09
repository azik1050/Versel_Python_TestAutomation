import pytest
from src.applications.jira.api.issue_service import IssueService
from src.core.clients.api_client import ApiClient
from src.core.clients.api_client.auth import BasicAuth
from src.core.config.settings import JiraAuth, TestConfig


@pytest.fixture(scope="session")
def jira_api():
    return IssueService(
        ApiClient(
            base_url=TestConfig.BASE_JIRA_API_URL,
            auth=BasicAuth(JiraAuth.JIRA_USER, JiraAuth.JIRA_PASSWORD)
        )
    )