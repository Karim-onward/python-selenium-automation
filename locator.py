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
driver.get('https://www.amazon.co.uk/')
#locate element:
#driver.find_element() # By. / value
#locate by ID:

#Amazon logo
driver.find_element(By.ID, 'a-icon a-icon-logo' )
#Continue Button
driver.find_element(By.ID, 'continue')
#forgot password
driver.find_element(By.ID, 'auth-fpp-link-bottom')
#create your amazon account button
driver.find_element(By.ID, 'createAccountSubmit')


#locate element By Xpath
driver.find_element(By.XPATH, "//span[@class='Need help']")
driver.find_element(By.XPATH, "//a[@href='Privacy Notice']")
driver.find_element(By.XPATH, "//input['@type=email']")