from pydantic import BaseModel, Field


class CreateCustomFieldRequestModel(BaseModel):
    description: str = Field(default=None)
    name: str
    searcher_key: str = Field(alias="searcherKey", default=None)
    type: str

    model_config = {
        "populate_by_name": True,
        "exclude_none": True
    }


class UpdateCustomFieldRequestModel(BaseModel):
    description: str = Field(default=None)
    name: str
    searcher_key: str = Field(alias="searcherKey", default=None)

