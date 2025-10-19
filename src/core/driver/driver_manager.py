from selenium.webdriver.ie.webdriver import WebDriver

from src.core.driver.driver_factory import DriverFactory
from src.core.utils.enums.Browser import Browser


class DriverManager:
    def __init__(self, browser: Browser):
        self.__browser: Browser = browser
        self.__driver: WebDriver | None = None

    def __create_driver(self):
        if not self.__driver:
            self.__driver = DriverFactory.create_driver(self.__browser)

    @property
    def driver(self) -> WebDriver:
        if not self.__driver:
            self.__create_driver()
        return self.__driver

    def tear_down(self):
        if self.__driver:
            self.__driver.quit()
            self.__driver = None
