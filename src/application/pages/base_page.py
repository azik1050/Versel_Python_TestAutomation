from selenium.webdriver.ie.webdriver import WebDriver
from abc import abstractmethod, ABC


class BasePage(ABC):
    _driver: WebDriver

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def navigate_to(self, url: str) -> None:
        self._driver.get(url)

