import pytest

from src.core.config.settings import TestConfig
from src.core.driver.driver_manager import DriverManager
from src.core.utils.enums.Browser import Browser


@pytest.fixture(scope='session', autouse=True)
def driver():
    driver_manager = DriverManager(Browser(TestConfig.BROWSER.lower()))
    driver_manager.driver.get(TestConfig.BASE_UI_URL)

    yield driver_manager.driver

    driver_manager.tear_down()


