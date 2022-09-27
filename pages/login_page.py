from .base_page import BasePage
from  .locators import LiginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert current_url == self.url, "Url is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LiginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LiginPageLocators.REGISTER_FORM), "Register form is not presented"