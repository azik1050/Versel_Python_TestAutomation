import pytest
from src.core.logger.logger import logger
import sys


@pytest.fixture(scope="session", autouse=True)
def setup_logger():
    return logger

