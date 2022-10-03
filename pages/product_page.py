import time

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_the_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()

    def should_be_success_message(self):
        message_text = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert message_text == product_name

    def should_be_price_buscket(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_SUCCESS_MESSAGE).text
        assert price == price_in_message
