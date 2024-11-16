from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By

options = Options()

options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/travel/flights")
sleep(3)

# Get page title
title = driver.title

print(title)

# get element Google
element = driver.find_element(By.XPATH, "//button[@aria-label='Rechazar todo']")
element.click()

#element.send_keys("teste")

element = driver.find_element(By.CLASS_NAME, "B4XJjd")
element.click()