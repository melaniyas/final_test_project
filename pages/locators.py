from selenium.webdriver.common.by import By


# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_CHECK_BASKET = (By.CSS_SELECTOR, ".basket-mini :nth-child(2) a.btn-default")

class ProductPageLocators():
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    BASKET_STRONG_NAMES = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_ADD_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alert-success')

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")