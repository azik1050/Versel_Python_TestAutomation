import random

import faker
from faker import Faker

from src.application.models.request.user_service_requests import CreateUserRequestModel


class UserFactory:
    faker = Faker()

    @classmethod
    def create_random_user(cls) -> CreateUserRequestModel:
        return CreateUserRequestModel(
            id=cls.faker.random_number(),
            username=cls.faker.user_name(),
            firstName=cls.faker.first_name(),
            lastName=cls.faker.last_name(),
            email=cls.faker.email(),
            password=cls.faker.password(),
            phone=str(cls.faker.phone_number()),
            userStatus=random.randint(1, 5)
        )

    @classmethod
    def create_invalid_user_missing_fields(cls, field_name: str) -> dict:
        user = cls.create_random_user().__dict__
        user.pop(field_name)

        return user
