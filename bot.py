from selenium import webdriver
from discover import fill

if __name__ == "__main__":
   # Set up browser
   driver = webdriver.Chrome()
   fill(driver)
