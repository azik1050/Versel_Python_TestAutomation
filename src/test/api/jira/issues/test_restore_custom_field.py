import allure

from src.applications.jira.models.response.issues_responses import DeleteCustomFailedFiledResponseModel
from src.applications.jira.utils.allure.enums import Epic, Feature
from src.applications.jira.utils.api_assertions import ApiAssertions
from src.test.api.base_test import BaseTest
from src.test.api.jira.conftest import issue_service
from pytest import mark


@allure.epic(Epic.ISSUES)
@allure.feature(Feature.RESTORE_CUSTOM_ISSUE_FIELD)
class TestRestoreCustomFields(BaseTest):
    @mark.regression
    @allure.story("Restore issue field")
    def test_restore_custom_issue_field(self, issue_service, deleted_custom_field):
        with allure.step(f'Restore issue field, ID: {deleted_custom_field.id}'):
            response = issue_service.restore_custom_field_from_trash(deleted_custom_field.id)
            self.assert_status_code(response, 200)



