from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()
#Create a new customer browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.target.com")

#Click signin button

sleep(7)
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
sleep(3)

#from the Account sign in tab click sign in
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
sleep(3)
#Verification
expected_text = 'Sign into your Target account'
actual_text = driver.find_element(By.XPATH, '//h1').text
assert expected_text in actual_text, f'Expected {expected_text} != {actual_text}'

driver.find_element(By.ID, 'login')

print('Test passed!')
driver.quit()
