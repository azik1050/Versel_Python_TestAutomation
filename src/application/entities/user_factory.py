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