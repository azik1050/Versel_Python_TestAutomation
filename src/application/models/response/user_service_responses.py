from pydantic import BaseModel, Field


class GetUserResponseModel(BaseModel):
    id: int
    username: int
    firstname: str = Field(alias="firstName")
    lastname: str = Field(alias="lastName")
    email: str
    password: str
    phone: str
    user_status: str = Field(alias="userStatus")


class CreateUserResponse(BaseModel):
    code: int
    type: str
    message: str
