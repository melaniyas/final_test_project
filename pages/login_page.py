from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        #проверка текущей ссылки
        assert "login" in self.browser.current_url, "Login link is not presented"

    def should_be_login_form(self):
        #проверка, что есть форма входа
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        #проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION)
        password_input1 = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION1)
        password_input2 = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION2)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        email_input.send_keys(email)
        password_input1.send_keys(password)
        password_input2.send_keys(password)
        registration_button.click()
