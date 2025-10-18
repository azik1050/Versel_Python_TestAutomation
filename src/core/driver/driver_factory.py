from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from src.core.utils.enums.Browser import Browser


class DriverFactory:
    @staticmethod
    def create_driver(browser: Browser) -> WebDriver:
        if browser == Browser.CHROME:
            return DriverFactory.create_chrome_driver()

    @staticmethod
    def create_chrome_driver() -> WebDriver:
        return webdriver.Chrome()
