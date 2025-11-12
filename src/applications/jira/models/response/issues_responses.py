from pydantic import BaseModel, RootModel, Field


class IssueFields(BaseModel):
    id: str
    key: str
    name: str
    custom: bool
    orderable: bool
    navigable: bool
    searchable: bool
    clauseNames: list[str]
    schema: dict[str, str]


class GetIssuesFieldsResponseModel(RootModel[list]):
    pass



class CreateCustomFieldResponseModel(BaseModel):
    id: str
    key: str
    name: str
    custom: bool
    orderable: bool
    navigable: bool
    searchable: bool
    clauseNames: list
    schema: dict


class ErrorResponseModel(BaseModel):
    error_messages: list = Field(alias="errorMessages")
    errors: dict


class CreateCustomFailedFiledResponseModel(ErrorResponseModel):
    pass


class DeleteCustomFailedFiledResponseModel(ErrorResponseModel):
    pass