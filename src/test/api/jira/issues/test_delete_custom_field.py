import allure

from src.applications.jira.models.response.issues_responses import DeleteCustomFailedFiledResponseModel
from src.applications.jira.utils.allure.enums import Epic, Feature
from src.applications.jira.utils.api_assertions import ApiAssertions
from src.test.api.jira.conftest import issue_service
from pytest import mark


@allure.epic(Epic.ISSUES)
@allure.feature(Feature.DELETE_CUSTOM_ISSUE_FIELD)
class TestDeleteCustomFields:
    @mark.regression
    @allure.story("Delete issue field")
    def test_delete_custom_issue_field(self, issue_service, custom_issue_field):
        with allure.step(f'Delete issue field, ID: {custom_issue_field.id}'):
            response = issue_service.delete_custom_field(custom_issue_field.id)
            ApiAssertions.assert_status_code(response, 303)

    @mark.regression
    @allure.story("Delete not existing custom issue field")
    def test_delete_not_existing_custom_issue_field(self, issue_service,):
        with allure.step(f'Delete not existing field'):
            response = issue_service.delete_custom_field('customfield_1')
            ApiAssertions.assert_status_code(response, 404)
            ApiAssertions.validate_response_model(response, DeleteCustomFailedFiledResponseModel)
            ApiAssertions.assert_key_value(response, ['errorMessages', 0], 'Field not found.')

    @mark.regression
    @allure.story("Delete custom issue field with invalid prefix")
    def test_delete_custom_issue_field_with_invalid_prefix(self, issue_service,):
        with allure.step(f'Delete field with invalid prefix'):
            response = issue_service.delete_custom_field('invalid_prefix')
            ApiAssertions.assert_status_code(response, 400)
            ApiAssertions.validate_response_model(response, DeleteCustomFailedFiledResponseModel)
            ApiAssertions.assert_key_value(response, ['errorMessages', 0], "Field id has to be prefixed with 'customfield_'")



