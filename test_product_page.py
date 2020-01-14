import time
from .Pages.product_page import ProductPage


def test_guest_can_go_to_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу

    page.should_be_button_add_basket()
    page.click_button_add_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)