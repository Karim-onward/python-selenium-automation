from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@when('open cart page')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".sc-fe064f5c-0")



@then('Verify “Your cart is empty” is shown')
def verify_cart_is_empty(context):
    sleep(5)
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, 'h1').text

    assert expected_text == actual_text, f'Expected "{expected_text}" but got "{actual_text}"'


@then('Verify cart has 1 item(s)')
def verify_cart_has_1_items(context):
    context.driver.find_element(By.XPATH, '//span[@class="h-text-lg"]')
