from pydantic import BaseModel, Field


class CreateOrderRequestModel(BaseModel):
    id: int = Field(alias="id")
    pet_id: int = Field(alias="petId")
    quantity: int = Field(alias="quantity")
    ship_date: str = Field(alias="shipDate")
    status: int = Field(alias="status")
    complete: bool = Field(alias="complete")
