import allure
from src.applications.jira.data.custom_fields_factory import CustomFieldsFactory
from src.applications.jira.models.response.issues_responses import CreateCustomFieldResponseModel, CreateCustomFailedFiledResponseModel
from src.applications.jira.utils.allure.enums import Epic, Feature
from src.applications.jira.utils.api_assertions import ApiAssertions
from src.test.api.jira.conftest import issue_service
from pytest import mark


@allure.epic(Epic.ISSUES)
@allure.feature(Feature.CREATE_CUSTOM_ISSUE_FIELDS)
class TestCreateCustomFields:
    @mark.regression
    @allure.story("Create custom issue fields")
    @mark.parametrize('field', [
        CustomFieldsFactory.create_custom_field(),
        CustomFieldsFactory.create_custom_field_with_specific_value({
            'searcherKey': None
        })
    ])
    def test_create_valid_custom_issue_fields(self, issue_service, field):
        with allure.step('Get list available of issue fields'):
            response = issue_service.create_custom_field(field)
            ApiAssertions.assert_status_code(response, 201)
            ApiAssertions.validate_response_model(response, CreateCustomFieldResponseModel)

    @mark.regression
    @allure.story("Create customer field with unknown searcherKey")
    @mark.parametrize('field', [
        CustomFieldsFactory.create_custom_field_with_specific_value({
            'searcherKey': 'invalidKey'
        }),
        CustomFieldsFactory.create_custom_field_with_specific_value({
            'searcherKey': 1
        })
    ])
    def test_create_custom_field_with_invalid_searcher_ley(self, issue_service, field):
        with allure.step(f'Create issue with invalid "searcherKey": {field['searcherKey']}'):
            response = issue_service.create_custom_field(field)
            ApiAssertions.assert_status_code(response, 400)
            ApiAssertions.validate_response_model(response, CreateCustomFailedFiledResponseModel)
            ApiAssertions.assert_key_value(response, ['errors', 'searcher'], 'Unknown searcher chosen')
