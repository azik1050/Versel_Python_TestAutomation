from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from src.application.pages.base_page import BasePage
from src.application.pages.product_page import ProductPage
from src.core.web_components.base_component import BaseComponent


class HomePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._main_section_product = BaseComponent(driver, By.XPATH, "//main/section[1]/div[1]")

    def click_main_section_product(self) -> ProductPage:
        self._main_section_product.click()
        return ProductPage(self._driver)

