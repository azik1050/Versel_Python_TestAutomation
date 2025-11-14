import allure
from src.applications.jira.models.response.issues_responses import GetIssuesFieldsResponseModel
from src.applications.jira.utils.allure.enums import Epic, Feature
from src.applications.jira.utils.api_assertions import ApiAssertions
from src.test.api.base_test import BaseTest
from src.test.api.jira.conftest import issue_service
from pytest import mark


@allure.epic(Epic.ISSUES)
@allure.feature(Feature.GET_ISSUE_FIELDS)
class TestCreateIssueFields(BaseTest):
    @mark.smoke
    @allure.story("Create issue fields")
    def test_get_issue_fields(self, issue_service):
        with allure.step('Get list available of issue fields'):
            response = issue_service.get_issue_fields()
            self.assert_status_code(response, 200)
            self.validate_response_model(response, GetIssuesFieldsResponseModel)
