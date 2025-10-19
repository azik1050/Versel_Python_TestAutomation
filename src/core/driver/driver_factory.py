from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from src.core.config.settings import TestConfig
from src.core.utils.enums.Browser import Browser


class DriverFactory:
    DEFAULT_AWAIT_TIME = TestConfig.IMPLICIT_DRIVER_WAIT

    @classmethod
    def create_driver(cls, browser: Browser) -> WebDriver:
        if browser == Browser.CHROME:
            return DriverFactory.create_chrome_driver()

    @classmethod
    def create_chrome_driver(cls) -> WebDriver:
        driver = webdriver.Chrome()
        driver.implicitly_wait(cls.DEFAULT_AWAIT_TIME)
        return driver
