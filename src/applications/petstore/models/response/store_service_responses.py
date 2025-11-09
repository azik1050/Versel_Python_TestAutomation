from pydantic import BaseModel, Field


class GetOrderByIdResponseModel(BaseModel):
    id: int = Field(alias="id")
    pet_id: int = Field(alias="petId")
    quantity: int = Field(alias="quantity")
    ship_date: str = Field(alias="shipDate", default=None)
    status: str = Field(alias="status", default=None)
    complete: bool = Field(alias="complete")