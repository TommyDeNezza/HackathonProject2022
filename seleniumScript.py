from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

import json
import time

userInfo = json.load(open("login.json"))
username = userInfo.get("user")
password = userInfo.get("password")

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)

#Registration Page 
def initialization():
    driver.get("https://login.bc.edu/nidp/idff/sso?id=19&sid=0&option=credential&sid=0&target=https%3A%2F%2Fservices.bc.edu%2Fcommoncore%2Fmyservices.do")
    ag_username = driver.find_element(By.ID, 'username')
    ag_username.send_keys(username)
    ag_password = driver.find_element(By.ID, 'password')
    ag_password.send_keys(password)
    ag_sign_in_button = driver.find_element(By.XPATH, '//*[@id="fm1"]/button')
    ag_sign_in_button.click()
    driver.implicitly_wait(10)
    driver.get("https://eaen.bc.edu/student-registration/#/")
    driver.implicitly_wait(30)
    term_pullup = driver.find_element(By.XPATH, '//*[@id="fddAtpSelectorInputTopDiv"]/div/div/div/span/i')
    term_pullup.click()
    spring = driver.find_element(By.XPATH, '//*[@id="ui-select-choices-row-0-0"]') #to be replaced
    fall = driver.find_element(By.XPATH, '//*[@id="ui-select-choices-row-0-1"]')
    spring.click()

def refresh():
    driver.implicitly_wait(60)
    dropper = driver.find_element(By.XPATH, '//*[@id="contextUserName"]/i')
    dropper.click()
    driver.implicitly_wait(30)
    refresher = driver.find_element(By.XPATH, '//*[@id="refreshSessionBtn"]')
    refresher.click()
    driver.implicitly_wait(45)

def enroll():
    first = '//*[@id="tabularCCRegistrationRequestItemSelectorCheckbox'
    for i in range(15):
        driver.implicitly_wait(20)
        id = first + str(i) + '"]'
        try:
            checkbox = driver.find_element(By.XPATH, id)
            checkbox.click()
            enroll = driver.find_element(By.XPATH, '//*[@id="register-button"]')
            enroll.click()
            driver.implicitly_wait(25000)
        except:
            break
#Main
def main():
    initialization()
    
    driver.implicitly_wait(60)
    print("\n\n",driver.find_element(By.XPATH, '//*[@id="tabularCCRegistrationRequestItemSelectorAutomaticRegistration"]'),"\n\n")
    #print("\n\n",driver.find_element(By.XPATH, '//*[@id="tabularCCRegistrationRequestItemSelectorRegistrationPlan1"]'),"\n\n")

    # while True:
    #     enroll()
    #     refresh()
    #     time.sleep(60)

main()