from pydantic import BaseModel, RootModel


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
