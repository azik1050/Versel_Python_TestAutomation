import allure

from src.applications.jira.utils.api_assertions import ApiAssertions
from pytest import mark


@mark.api
class BaseTest(ApiAssertions):
    def __init__(self):
        self.__soft_asserts = []

    def soft_assert(self, condition: bool, message: str):
        if not condition:
            self.__soft_asserts.append(message)

    def step(self, message: str):
        return allure.step(message)