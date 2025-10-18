from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.core.web_components.base_component import BaseComponent
from src.core.driver.driver import Driver


class WaitUtils:
    __DEFAULT_TIMEOUT = 10
    __driver = Driver.get_driver()

    @classmethod
    def until_clickable(cls, element: BaseComponent, timeout=None) -> WebElement:
        if not timeout:
            timeout = cls.__DEFAULT_TIMEOUT
        wait = WebDriverWait(driver=cls.__driver, timeout=timeout)
        return wait.until(EC.element_to_be_clickable(element.get_element()))
