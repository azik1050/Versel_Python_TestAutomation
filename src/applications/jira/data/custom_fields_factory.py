from pydantic import BaseModel
from src.applications.jira.models.request.issues_requests import CreateCustomFieldRequestModel
from src.core.utils.base_api_factory import BaseJSONFactory


class CustomFieldsFactory(BaseJSONFactory):
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

        return cls._change_json_values(data, custom_values)

    @classmethod
    def create_custom_field_without_fields(cls, excluded_fields: list[str]) -> CreateCustomFieldRequestModel:
        data = cls.create_custom_field().model_dump(by_alias=True)

        return CreateCustomFieldRequestModel(**cls._exclude_json_values(data, excluded_fields))
