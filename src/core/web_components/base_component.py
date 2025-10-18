from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.core.driver.driver import Driver
from src.core.utils.wait_utils import WaitUtils


class BaseComponent:
    _driver = Driver.get_driver()
    _locator: By

    def __init__(self, locator: By):
        self._locator = locator

    def get_element(self) -> WebElement:
        return self._driver.find_element(self._locator)

    def click(self, time: float = 0.0):
        WaitUtils.until_clickable(self).click()

    def get_locator(self):
        return self._locator