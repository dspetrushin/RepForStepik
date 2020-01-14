from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_button_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_BASKET), "BUTTON ADD_BASKET is not presented"

    def click_button_add_basket(self):
        button_add_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        button_add_basket.click()

