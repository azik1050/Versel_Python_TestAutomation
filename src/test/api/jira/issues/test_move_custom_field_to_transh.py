import allure

from src.applications.jira.models.response.issues_responses import DeleteCustomFailedFiledResponseModel
from src.applications.jira.utils.allure.enums import Epic, Feature
from src.applications.jira.utils.api_assertions import ApiAssertions
from src.test.api.jira.conftest import issue_service
from pytest import mark


@allure.epic(Epic.ISSUES)
@allure.feature(Feature.TRASH_CUSTOM_ISSUE_FIELD)
class TestMoveCustomFieldToTrash:
    @mark.regression
    @allure.story("Move custom field to trash")
    def test_move_to_trash(self, issue_service, custom_issue_field):
        with allure.step(f'Move field to trash, ID: {custom_issue_field.id}'):
            response = issue_service.move_custom_field_to_trash(custom_issue_field.id)
            ApiAssertions.assert_status_code(response, 200)


