from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage

class Header(BasePage):
    Search_field = (By.ID, 'search')
    Search_Btn = (By.CSS_SELECTOR, 'button[data-test="@web/Search/SearchButton"]')
    Cart_icon = (By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]')

    def search_product(self):
        self.input_text('tea', *self.Search_field)
        self.click(*self.Search_Btn)
        sleep(10)

    def click_cart(self):
        self.click(*self.Cart_icon)
