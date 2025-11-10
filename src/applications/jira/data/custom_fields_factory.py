from faker import Faker
from pydantic import BaseModel

from src.applications.jira.models.request.issues_requests import CreateCustomFieldRequestModel


class CustomFieldsFactory:
    faker = Faker()

    @classmethod
    def create_custom_field(cls) -> CreateCustomFieldRequestModel:
        return CreateCustomFieldRequestModel(
            # name=cls.faker.text(10),
            # description=cls.faker.text(15),
            name='New custom field',
            description='Custom field for picking groups',
            searchKey='com.atlassian.jira.plugin.system.customfieldtypes:grouppickersearcher',
            type='com.atlassian.jira.plugin.system.customfieldtypes:grouppicker'
        )

    @classmethod
    def create_custom_field_without_properties(cls, properties: list) -> CreateCustomFieldRequestModel:
        field = cls.create_custom_field()
        try:
            for property in properties:
                field.pop(property)
        except Exception as e:
            raise Exception(f"Such field is not supported by API, error: {e}")
        return field

    @classmethod
    def create_custom_field_with_defined_properties(cls, properties: list) -> dict:
        pass