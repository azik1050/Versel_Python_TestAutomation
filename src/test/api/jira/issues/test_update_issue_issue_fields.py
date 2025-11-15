import string
import allure
from src.applications.jira.models.request.issues_requests import UpdateCustomFieldRequestModel
from src.applications.jira.utils.allure.enums import Epic, Feature
from src.test.api.base_test import BaseTest
from src.test.api.jira.conftest import issue_service
from pytest import mark


@allure.epic(Epic.ISSUES)
@allure.feature(Feature.UPDATE_CUSTOM_ISSUE_FIELDS)
class TestUpdateCustomFields(BaseTest):
    @mark.regression
    @allure.story("Update 'description' field")
    @mark.parametrize('description_field', [
        'q',
        string.digits,
        string.ascii_letters,
        '!@#$%^&*()/*-+'
    ])
    def test_update_customer_issue_description_field(self, issue_service, custom_issue_field, description_field):
        with self.step(f'Update issue description to: {description_field}'):
            response = issue_service.update_custom_field(
                UpdateCustomFieldRequestModel(
                    description=description_field,
                    name='New custom field',
                    searcherKey='com.atlassian.jira.plugin.system.customfieldtypes:grouppickersearcher'
                ),
                custom_issue_field.id
            )
            self.assert_status_code(response, 204)

    @mark.regression
    @allure.story("Update 'name' field")
    @mark.parametrize('name_field', [
        'q',
        string.digits,
        string.ascii_letters,
        '!@#$%^&*()/*-+'
    ])
    def test_update_customer_issue_name_field(self, issue_service, custom_issue_field, name_field):
        with self.step(f'Update issue description to: {name_field}'):
            response = issue_service.update_custom_field(
                UpdateCustomFieldRequestModel(
                    description='Some sort of description',
                    name=name_field,
                    searcherKey='com.atlassian.jira.plugin.system.customfieldtypes:grouppickersearcher'
                ),
                custom_issue_field.id
            )
            self.assert_status_code(response, 204)
