import allure
from src.applications.versel.pages.home_page import HomePage
from src.applications.versel.utils.enums.product_options import ProductColor, ProductSize
from pytest import mark
from src.test.ui.conftest import driver


@mark.ui
def test_successful_purchase(driver):
    product_page = HomePage(driver).click_main_section_product()
    product_page.select_color(ProductColor.BLACK)
    product_page.select_size(ProductSize.XS)
    product_page.click_add_to_cart_button()
    product_page.click_stupid_button().click_checkout_button()
