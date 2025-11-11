import allure

from src.applications.jira.data.custom_fields_factory import CustomFieldsFactory
from src.applications.jira.models.request.issues_requests import CreateCustomFieldRequestModel
from src.applications.jira.models.response.issues_responses import CreateCustomFieldResponseModel
from src.applications.jira.utils.allure.enums import Epic, Feature
from src.applications.jira.utils.api_assertions import ApiAssertions
from src.test.api.jira.conftest import issue_service
from pytest import mark


@allure.epic(Epic.ISSUES)
@allure.feature(Feature.CREATE_CUSTOM_ISSUE_FIELDS)
class TestCreateCustomFields:
    @mark.skip
    @mark.smoke
    @allure.story("Create custom issue fields")
    @mark.parametrize('field', [
        CustomFieldsFactory.create_custom_field()
    ])
    def test_create_valid_custom_issue_fields(self, issue_service, field):
        with allure.step('Get list available of issue fields'):
            response = issue_service.create_custom_field(field)
            ApiAssertions.assert_status_code(response, 201)
            ApiAssertions.validate_response_model(response, CreateCustomFieldResponseModel)
