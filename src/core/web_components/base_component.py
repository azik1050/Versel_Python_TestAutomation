from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from src.test.ui.conftest import driver


class BaseComponent:
    _locator: tuple

    def __init__(self, driver: WebDriver, *args):
        self._driver = driver
        self._locator = args

    @property
    def locator(self):
        return self._locator

    @property
    def element(self) -> WebElement:
        return self._driver.find_element(*self._locator)

    def click(self, time: float = 0.0):
        from src.core.utils.wait_utils import WaitUtils
        WaitUtils.until_clickable(driver=self._driver, element=self, timeout=time).click()
