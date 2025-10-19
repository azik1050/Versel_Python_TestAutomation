from selenium.webdriver.ie.webdriver import WebDriver

from src.core.driver.driver_factory import DriverFactory
from src.core.utils.enums.Browser import Browser


class Driver:
    __driver: WebDriver

    def __init__(self):
        raise Exception("This is singleton mothersucker")

    @classmethod
    def __create_driver(cls):
        if not cls.__driver:
            cls.__driver = DriverFactory.create_driver(Browser.CHROME)

    @classmethod
    def get_driver(cls) -> WebDriver:
        cls.__create_driver()

    @classmethod
    def tear_down(cls):
        if cls.__driver:
            cls.__driver = None
            cls.__driver.quit()
