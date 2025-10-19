import pytest
from src.application.api.users_service import UserService
from src.core.clients.api_client import ApiClient
from src.core.config.settings import TestConfig
from src.application.utils.api_data.user_service_fixtures import *


@pytest.fixture(scope='session', autouse=True)
def api_client():
    return ApiClient(base_url=TestConfig.BASE_API_URL)


@pytest.fixture(scope='session')
def user_api():
    return UserService(base_url=TestConfig.BASE_API_URL)