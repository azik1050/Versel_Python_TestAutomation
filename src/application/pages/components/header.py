from selenium.webdriver.common.by import By

from src.application.pages.base_page import BasePage
from src.core.web_components.base_component import BaseComponent


class Header(BasePage):
    allLink: BaseComponent
    shirtsLink: BaseComponent
    stickersLink: BaseComponent

    def __init__(self):
        self.allLink = BaseComponent(By.LINK_TEXT("All"))
        self.shirtsLink = BaseComponent(By.LINK_TEXT("Shirts"))
        self.stickersLink = BaseComponent(By.LINK_TEXT("Stickers"))

    def click_all_link(self) -> None:
        self.allLink.click()

    def click_shirts_link(self) -> None:
        self.shirtsLink.click()

    def click_stickers_link(self) -> None:
        self.stickersLink.click()