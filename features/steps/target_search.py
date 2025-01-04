from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then



@given('Open target page')
def open_target_page(context):
    context.driver.get('https://www.target.com/')


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]').click()



@then('Verify “Your cart is empty” text is shown')
def verify_cart_is_empty(context):
    sleep(5)
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, 'h1').text

    assert expected_text == actual_text, f'Expected "{expected_text}" but got "{actual_text}"'


#Question 3 sign in page
@given('Open target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')


@when('from right side navigation menu, click Sign In')
def navigate_to_sign_in_page(context):
        context.driver.find_element(By.ID, '(account-sign-in').click()
        sleep(5)

@when('click sign in from the main page')
def navigate_to_sign_in_page(context):
        context.driver.find_element(By.ID, 'account-sign-in').click()


@when('click sign in')
def click_sign_in_(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button[data-test="accountNav-signIn"]').click()
    sleep(2)


@then('verify sign In form open')
def verify_sign_in_form(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, ".sc-fe064f5c-0").text

    assert expected_text == actual_text, f'Expected "{expected_text}" but got "{actual_text}"'
