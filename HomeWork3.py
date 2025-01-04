from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()




# Create Account on Amazon.com
#Amazon logo

#Create account

#your name
driver.find_element(By.ID, "ap_customer_name")
#mobile number or email
driver.find_element(By.CSS_SELECTOR, "#.a-section.a-spacing-none.moa-single-claim-input-container")
#Password
driver.find_element(By.ID, "ap_password")
#Re-enterPassword
driver.find_element(By.CSS_SELECTOR, "#ap_password_check_context_message_section")
#Continue
driver.find_element(By.CSS_SELECTOR, "#continue")
#privacy-Notice
driver.find_element(By.CSS_SELECTOR, "")
# condition of use

#Create aa free business Account
driver.find_element(By.ID, "#ab-enhanced-registration-link")

#Sign in
driver.find_element(By.CSS_SELECTOR, "")


