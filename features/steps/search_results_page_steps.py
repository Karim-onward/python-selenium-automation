from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then

ADD_TO_CART_BTN = (By.CSS_SELECTOR,'[data-test="chooseOptionsButton"]')
ADD_TO_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR,'[data-test="shippingButton"]')



@then('Verify search result shown for {product}')
def verify_search_results(context, product):
    context.app.search_results_page.verify_search_results_is_shown()

@when('click on add to cart')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()



# @when('confirm add to cart button from side navigation')
# def side_nav_click_add_to_cart(context):