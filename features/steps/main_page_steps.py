from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open target page')
def open_target_page(context):
    context.driver.get('https://www.target.com/')

@when('search for tea')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.CSS_SELECTOR, 'button[data-test="@web/Search/SearchButton"]').click()


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]').click()






