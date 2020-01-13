from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "'login' not in current url"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Нет поля Email на форме Log In"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS), "Нет поля Password на форме Log In"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Нет поля Email на форме Register"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASS), "Нет поля Password на форме Register"
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PASS), "Нет поля Confirm password на форме Register"