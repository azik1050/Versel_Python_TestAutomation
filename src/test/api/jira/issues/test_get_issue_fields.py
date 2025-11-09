import allure

from src.applications.jira.utils.allure.enums import Epic, Feature
from src.applications.jira.utils.api_assertions import ApiAssertions
from src.test.api.jira.conftest import jira_api
from pytest import mark


@mark.smoke
@allure.epic(Epic.ISSUES)
@allure.feature(Feature.GET_ISSUE_FIELDS)
@allure.story("Get list available of issue fields")
def test_get_issue_fields(jira_api):
    response = jira_api.get_issue_fields()
    ApiAssertions.assert_status_code(response, 200)