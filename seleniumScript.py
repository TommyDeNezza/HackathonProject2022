from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import json


driver = webdriver.Chrome()

userInfo = json.load(open("login.json"))
username = userInfo.get("user")
password = userInfo.get("password")

# Agora link
driver.get("https://login.bc.edu/nidp/idff/sso?id=19&sid=0&option=credential&sid=0&target=https%3A%2F%2Fservices.bc.edu%2Fcommoncore%2Fmyservices.do")
# registration page link
driver.get("https://eaen.bc.edu/student-registration/#/")
elem = driver.find_element(By.XPATH, '//*[@id="tabularCCRegistrationRequestItemSelectorCheckbox2"]')
elem.click()
elem = driver.find_element(By.XPATH, '//*[@id="register-button"]')
