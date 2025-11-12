import allure
from src.applications.jira.models.response.issues_responses import CreateCustomFieldResponseModel, CreateCustomFailedFiledResponseModel
from src.applications.jira.utils.allure.enums import Epic, Feature
from src.applications.jira.utils.api_assertions import ApiAssertions
from src.test.api.jira.conftest import issue_service
from pytest import mark


@allure.epic(Epic.ISSUES)
@allure.feature(Feature.UPDATE_CUSTOM_ISSUE_FIELDS)
@mark.skip
class TestUpdateCustomFields:
    @mark.regression
    @allure.story("Create custom issue fields")
    def test_update_customer_issue_field_name(self, issue_service, custom_issue_field):
        with allure.step('Get list available of issue fields'):
            response = issue_service.create_custom_field(custom_issue_field.id)
            ApiAssertions.assert_status_code(response, 204)
            ApiAssertions.validate_response_model(response, CreateCustomFieldResponseModel)


