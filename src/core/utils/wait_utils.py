from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from src.core.web_components.base_component import BaseComponent


class WaitUtils:
    __DEFAULT_TIMEOUT = 10

    @classmethod
    def until_clickable(cls, driver: WebDriver, element: BaseComponent, timeout=None) -> WebElement:
        if not timeout:
            timeout = cls.__DEFAULT_TIMEOUT
        wait = WebDriverWait(driver=driver, timeout=timeout)
        return wait.until(EC.element_to_be_clickable(element.element))
