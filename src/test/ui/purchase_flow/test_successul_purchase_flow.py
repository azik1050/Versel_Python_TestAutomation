from time import sleep

import allure
from src.application.pages.home_page import HomePage
from src.application.utils.enums.product_options import ProductColor, ProductSize
from src.test.ui.conftest import driver


def test_successful_purchase(driver):
    with allure.step("Navigate to product page"):
        product_page = HomePage(driver).click_main_section_product()
    with allure.step("Choose color"):
        product_page.select_color(ProductColor.BLACK)
    with allure.step("Choose size"):
        product_page.select_size(ProductSize.XS)
    with allure.step("Proceed"):
        product_page.click_add_to_cart_button()
    with allure.step("Choose amount"):
        product_page.click_stupid_button().click_checkout_button()