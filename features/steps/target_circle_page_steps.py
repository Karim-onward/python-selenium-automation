from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then


@given('open target circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/circle')

@then('Verify that there are at least 10 benefit cells')
def verify_cells(context):
    context.driver.find_elements(By.CSS_SELECTOR, ".cell-item-content")