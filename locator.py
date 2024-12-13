from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#from time import sleep

#get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()
#Create a new customer browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#opent the Url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
#locate element:
#driver.find_element() # By. / value
#locate by ID:
sleep(5)
#Amazon logo
driver.find_element(By.XPATH, '//i[@class="a-icon a-icon-logo"]' )
#Continue Button
driver.find_element(By.ID, 'continue')
#forgot password
driver.find_element(By.ID, 'auth-fpp-link-bottom')
#create your amazon account button
driver.find_element(By.ID, 'createAccountSubmit')


#locate element By Xpath
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_privacy_notice')]")
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')]")

#Create your Amazon acct
# driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")
driver.find_element(By.ID, 'createAccountSubmit')


driver.quit()