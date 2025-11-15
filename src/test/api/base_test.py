import allure

from src.applications.jira.utils.api_assertions import ApiAssertions
from pytest import mark


@mark.api
class BaseTest(ApiAssertions):
    def step(self, message: str):
        return allure.step(message)