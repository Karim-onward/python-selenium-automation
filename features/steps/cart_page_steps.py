from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC




@when('open cart page')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".sc-fe064f5c-0")



@then('Verify “Your cart is empty” is shown')
def verify_cart_is_empty(context):
    context.app.cart_page.verify_cart_empty()
    #expected_text = 'Your cart is empty'
    #actual_text = context.driver.find_element(By.CSS_SELECTOR, 'h1').text

    #assert expected_text == actual_text, f'Expected "{expected_text}" but got "{actual_text}"'


@then('Verify cart has 1 items')
def verify_cart_has_1_items(context):
    #context.driver.find_element(By.XPATH, '//span[@class="h-text-lg"]')
    context.driver.wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="h-text-lg"]')))
