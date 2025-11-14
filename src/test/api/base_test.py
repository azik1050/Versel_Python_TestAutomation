from src.applications.jira.utils.api_assertions import ApiAssertions
from pytest import mark


@mark.api
class BaseTest(ApiAssertions):
    pass