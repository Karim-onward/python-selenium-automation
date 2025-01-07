from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then



@then('Verify search result is shown')
def verify_search_results(context):
    expected_result = 'tea'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, ".h-text-bs")
    assert expected_result in actual_result, f'Expected text"{expected_result}" not in match'
    sleep(2)

@when('click on add to cart')
def add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="chooseOptionsButton"]').click()
    sleep(5)

@when('confirm add to cart button from side navigation')
def confirm_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="shippingButton"]').click()








