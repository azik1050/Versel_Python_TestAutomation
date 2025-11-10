from pydantic import BaseModel, Field


class CreateCustomFieldRequestModel(BaseModel):
    description: str = Field(default=None)
    name: str
    search_key: str = Field(alias="searchKey", default=None)
    type: str

    model_config = {
        "populate_by_name": True,
        "exclude_none": True
    }