from pydantic import BaseModel, Field


class GetUserResponseModel(BaseModel):
    id: int
    username: str
    email: str
    password: str
    phone: str
    user_status: int = Field(alias="userStatus")

class GetUserFailResponseModel(BaseModel):
    code: int
    type: str
    message: str


class CreateUserResponse(BaseModel):
    code: int
    type: str
    message: str
