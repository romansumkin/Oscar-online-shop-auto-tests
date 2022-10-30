from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    WATCH_BASKET = (By.CSS_SELECTOR, ".btn-group a")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LiginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner > strong")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner > p > strong")

class BusketPageLocators():
    BASKET_SUMMARY = (By.CSS_SELECTOR, ".basket_summary")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")

