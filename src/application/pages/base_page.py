from src.core.driver.driver import Driver
from abc import abstractmethod, ABC


class BasePage(ABC):
    _driver = Driver.get_driver()

    def navigate_to(self, url: str) -> None:
        self._driver.get(url)

