from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
username = "montessm"
password = "Shak1r81"
# Agora link
driver.get("https://login.bc.edu/nidp/idff/sso?id=19&sid=0&option=credential&sid=0&target=https%3A%2F%2Fservices.bc.edu%2Fcommoncore%2Fmyservices.do")
# find username/email field and send the username itself to the input field
driver.find_element(By.ID, "username").send_keys(username)
# find password input field and insert password as well
driver.find_element(By.ID, "password").send_keys(password)
# click login button
driver.find_element(By.XPATH, '//*[@id="fm1"]/button').click()
# registration page link
driver.get("https://eaen.bc.edu/student-registration/#/")
# driver.find_element(By.XPATH, '//*[@id="fddAtpSelectorInputItemCode-0"]/p')
# elem = driver.find_element(By.XPATH, '//*[@id="tabularCCRegistrationRequestItemSelectorCheckbox2"]')
# elem.click()
# elem = driver.find_element(By.XPATH, '//*[@id="register-button"]')
time.sleep(10000)
