from selenium.webdriver.ie.webdriver import WebDriver
from src.application.pages.home_page import HomePage
from src.application.pages.product_page import ProductPage


class PageFactory:
    __home_page: HomePage | None
    __product_page: ProductPage | None

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def home_page(self) -> HomePage:
        if not self.__home_page:
            self.__home_page = HomePage(self._driver)
        return self.__home_page

    @property
    def product_page(self) -> ProductPage:
        if not self.__product_page:
            self.__product_page = ProductPage(self._driver)
        return self.__product_page

