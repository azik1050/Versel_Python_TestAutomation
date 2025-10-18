from pydantic import BaseModel, Field


class GetUserRequestModel(BaseModel):
    id: int
    username: int
    firstname: str = Field(alias="firstName")
    lastname: str = Field(alias="lastName")
    email: str
    password: str
    phone: str
    user_status: str = Field(alias="userStatus")
