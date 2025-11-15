import pytest
from src.applications.jira.data.custom_fields_factory import CustomFieldsFactory
from src.applications.jira.models.response.issues_responses import CreateCustomFieldResponseModel
from src.applications.jira.utils.api_assertions import ApiAssertions


@pytest.fixture(scope='function')
def custom_issue_field(issue_service) -> CreateCustomFieldResponseModel:
    response = issue_service.create_custom_field(CustomFieldsFactory.create_custom_field())
    ApiAssertions.assert_status_code(response, 201)
    ApiAssertions.validate_response_model(response, CreateCustomFieldResponseModel)
    return CreateCustomFieldResponseModel(**response.json())


@pytest.fixture(scope='function')
def deleted_custom_field(issue_service, custom_issue_field) -> CreateCustomFieldResponseModel:
    response = issue_service.move_custom_field_to_trash(custom_issue_field.id)
    ApiAssertions.assert_status_code(response, 200)
    return custom_issue_field