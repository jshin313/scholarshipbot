from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

username = ""
password = ""
firstname = ""
lastname = ""
studentid = ""
url = ""

def wait(driver, element):
    delay = 10 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, element)))
        except TimeoutException:
    	print("Loading took too much time!")

def login(driver):
    pass

def fill(driver):
    # Go to Google Form url
    driver.get(url)
    wait(driver, "headingText")

    # Fill out username
    loginuser = driver.find_element_by_id("identifierId")
    loginuser.send_keys(username)
    driver.find_element_by_id("identifierNext").click()

    # Fill out password
    wait(driver, "profileIdentifier")
    loginpass = driver.find_element_by_name("password")
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(loginpass).click(loginpass)

    # Click on next
    loginpass.send_keys(password)
    driver.find_element_by_id("passwordNext").click()

    wait(driver, "base-js")

    # Fill out Last Name
    elem = driver.find_element_by_name("entry.1472614698");
    elem.click()
    elem.send_keys(lastname)

    # Fill out First Name
    elem = driver.find_element_by_name("entry.1214905355");
    elem.click()
    elem.send_keys(firstname)

    # Fill out Student ID
    elem = driver.find_element_by_name("entry.2062280665");
    elem.click()
    elem.send_keys(studentid)

    elem = driver.find_element_by_class_name("appsMaterialWizButtonEl");
    elem.click()

    #driver.quit()



