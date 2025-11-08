from faker import Faker
from src.application.models.request.store_service_requests import CreateOrderRequestModel


class OrderFactory:
    faker = Faker()

    def create_order(self) -> CreateOrderRequestModel:
        return CreateOrderRequestModel(
            id=self.faker.pyint(),
            petId=self.faker.pyint(),
            quantity=self.faker.pyint(min_value=1, max_value=100),
            shipDate=self.faker.date(),
            status=self.faker.pyint(min_value=1, max_value=100),
            complete=self.faker.boolean()
        )

