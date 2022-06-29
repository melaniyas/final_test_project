from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        #проверка текущей ссылки
        assert True = self.current_url(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_login_form(self):
        #проверка, что есть форма входа
        assert True = self.is_element_present(*MainPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        #проверка, что есть форма регистрации на странице
        assert True = self.is_element_present(*MainPageLocators.REGISTRATION_FORM), "Registration form is not presented"