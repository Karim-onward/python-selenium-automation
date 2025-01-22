from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    SEARCH_RESULTS = (By.CSS_SELECTOR, By.CSS_SELECTOR, ".h-text-bs")

    def verify_search_results(self):
        actual_result = self.find_element(*self.SEARCH_RESULTS).text
        assert 'tea' in actual_result, f'Expected text tea not in actual {actual_result}'
