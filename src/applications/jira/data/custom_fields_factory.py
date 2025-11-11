from faker import Faker
from pydantic import BaseModel

from src.applications.jira.models.request.issues_requests import CreateCustomFieldRequestModel


class CustomFieldsFactory:
    faker = Faker()

    @classmethod
    def create_custom_field(cls) -> CreateCustomFieldRequestModel:
        return CreateCustomFieldRequestModel(
            name=cls.faker.text(10),
            description=cls.faker.text(15),
            searcherKey='com.atlassian.jira.plugin.system.customfieldtypes:grouppickersearcher',
            type='com.atlassian.jira.plugin.system.customfieldtypes:grouppicker'
        )

    @classmethod
    def create_custom_field_with_specific_value(cls, custom_values: dict) -> dict:
        data = cls.create_custom_field().model_dump(by_alias=True)

        for key, value in custom_values.items():
            data[key] = value

        return data

    @classmethod
    def create_custom_field_without_fields(cls, excluded_fields: list[str]) -> CreateCustomFieldRequestModel:
        data = cls.create_custom_field().model_dump(by_alias=True)

        for field in excluded_fields:
            data.pop(field)

        return CreateCustomFieldRequestModel(**data)
