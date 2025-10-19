from pydantic import BaseModel, Field


class CreateUserRequestModel(BaseModel):
    id: int
    username: str
    firstname: str = Field(alias="firstName")
    lastname: str = Field(alias="lastName")
    email: str
    password: str
    phone: str
    user_status: int = Field(alias="userStatus")
