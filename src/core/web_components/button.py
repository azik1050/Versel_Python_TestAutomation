from selenium.webdriver.ie.webdriver import WebDriver

from src.core.web_components.base_component import BaseComponent


class Button(BaseComponent):
    def __init__(self, driver: WebDriver, *args):
        super().__init__(driver, *args)

    @property
    def is_selected(self) -> bool:
        return self.element.is_selected()