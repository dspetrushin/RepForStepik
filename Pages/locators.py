from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS = (By.CSS_SELECTOR, "#id_login-password")

    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASS = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_CONFIRM_PASS = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators():
    BUTTON_ADD_BASKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary")
    TEXT_ELEMENT_AFTER_ADD_BASKET = (By.CLASS_NAME, "alertinner")

