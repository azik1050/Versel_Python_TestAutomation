from src.applications.petstore.api.store_service import StoreService
from src.applications.petstore.api.users_service import UserService
from src.core.clients.api_client import ApiClient
from src.core.config.settings import TestConfig
from src.applications.petstore.data.api_data.user_service_fixtures import *


@pytest.fixture(scope='session', autouse=True)
def api_client():
    return ApiClient(base_url=TestConfig.BASE_API_URL)


@pytest.fixture(scope='session')
def user_api():
    return UserService(api_client=ApiClient(base_url=TestConfig.BASE_API_URL))


@pytest.fixture(scope='session')
def store_api():
    return StoreService(api_client=ApiClient(base_url=TestConfig.BASE_API_URL))