from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

url = "https://scholarship.collegecovered.com/"
persontype = "senior"
first_name = "John"
last_name = "Smith"
state = "US-PA"
school = "21st Century"

def wait(driver, element):
    delay = 10 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, element)))
    except TimeoutException:
        print("Loading took too much time!")

def fill(driver):
    # Go to the sweepstake url
    driver.get(url)
    wait(driver, "content")

    driver.find_element_by_name("about_you").click()

    driver.find_element_by_xpath("//option[@value='" + persontype + "']").click();
    driver.find_element_by_xpath("//button[@type='submit']").click();

    wait(driver, "first_name")
    driver.find_element_by_id("first_name").send_keys(first_name)

    driver.find_element_by_id("last_name").send_keys(last_name)
    driver.find_element_by_xpath("//button[@type='submit']").click();

    wait(driver, "app")

    driver.find_element_by_xpath("//select[@class='school-select--state']").click()

    wait(driver, "app")


    driver.find_element_by_xpath("//option[@value='" + state + "']").click()

    wait(driver, "app")

    driver.find_element_by_xpath("//input[@class='school-select--text-input']").send_keys(school)

    driver.find_element_by_xpath("//i[@class='fa']")[0].click()

    #driver.quit()