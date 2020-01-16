from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_button_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_BASKET), "BUTTON ADD_BASKET is not presented"

    def click_button_add_basket(self):
        button_add_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        button_add_basket.click()

    def check_text(self):
        text_element = self.browser.find_element(*ProductPageLocators.TEXT_ELEMENT_AFTER_ADD_BASKET).text
        #print(text_element)
        assert (text_element=='Coders at Work has been added to your basket.', 'Некорректный текст сообщения о добавлении в корзину')
