from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, 'div[data-test="boxEmptyMsg"]')

    def verify_cart_empty(self):
        expected_result = 'Your cart is empty'
        actual_result = self.driver.find_element(*self.CART_EMPTY_MSG).text
        assert expected_result == actual_result, f'{expected_result} did not match {actual_result}'
