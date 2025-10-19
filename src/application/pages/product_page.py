from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from src.application.pages.base_page import BasePage
from src.application.utils.enums.product_options import ProductColor, ProductSize
from src.core.web_components.button import Button


class ProductPage(BasePage):
    def __init__(self, driver: WebDriver):
        self.selected_color: Button | None = None
        self.selected_size: Button | None = None
        self.__proceed_to_checkout_button: Button = Button(driver, By.XPATH, "//form/button[text()='Proceed to Checkout']")
        self.__add_to_cart_button: Button = Button(driver, By.XPATH, "//button[@aria-label='Add to cart']")
        self.__stupid_button: Button = Button(driver, By.XPATH, "//button[@aria-label='Close toast']")
        super().__init__(driver)


    def select_color(self, color: ProductColor):
        self.selected_color = Button(self._driver,By.XPATH, f"//button[normalize-space(text())='{color.value}']")
        self.selected_color.click()
        return self

    def select_size(self, size: ProductSize):
        self.selected_size = Button(self._driver,By.XPATH, f"//button[normalize-space(text())='{size.value}']")
        self.selected_size.click()
        return self

    def click_add_to_cart_button(self):
        self.__add_to_cart_button.click()
        return self

    def click_checkout_button(self):
        self.__proceed_to_checkout_button.click()

    def click_stupid_button(self):
        self.__stupid_button.click()
        return self
