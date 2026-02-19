import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://practice.expandtesting.com/login")

username_form = driver.find_element(By.XPATH, "//input[@id='username']")

assert username_form.is_displayed()

time.sleep(3)
