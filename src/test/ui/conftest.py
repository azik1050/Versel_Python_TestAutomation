import pytest
import logging
import os
from src.applications.versel.data.page_factory import PageFactory
from src.core.config.settings import TestConfig
from src.core.driver.driver_manager import DriverManager
from src.core.utils.enums.Browser import Browser


@pytest.fixture(scope='session', autouse=True)
def driver():
    driver_manager = DriverManager(Browser(TestConfig.UI.BROWSER.lower()))
    driver_manager.driver.get(TestConfig.UI.BASE_UI_URL)

    yield driver_manager.driver

    driver_manager.tear_down()


@pytest.fixture(scope='session', autouse=True)
def pages(driver):
    return PageFactory(driver)


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    # root = os.path.dirname(os.path.abspath(__file__))
    root = TestConfig.BASE_DIR
    while not os.path.exists(os.path.join(root, "pytest.ini")) and not os.path.exists(os.path.join(root, ".git")):
        parent = os.path.dirname(root)
        if parent == root:
            break
        root = parent

    log_path = os.path.join(root, "test_run.log")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    # configure before any test runs
    logging.basicConfig(
        filename=log_path,
        filemode="w",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.info("=== Logging initialized ===")
