from .base_page import BasePage
from  .locators import BusketPageLocators

class BusketPage(BasePage):
    def should_not_be_books_in_the_busket(self):
        assert self.is_not_element_present(*BusketPageLocators.BASKET_SUMMARY)

    def shoud_be_text_empty_busket(self):
        basket_is_empty_text = self.browser.find_element(*BusketPageLocators.BASKET_EMPTY_TEXT).text
        assert basket_is_empty_text == "Ваша корзина пуста Продолжить покупки"

