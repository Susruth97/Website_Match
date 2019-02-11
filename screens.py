import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_screenShots(url) :

    driver = webdriver.Chrome()
    driver.get(url)

    el = driver.find_element_by_tag_name('body')
    el.screenshot('ape.png')
    driver.quit()

url = "https://python.org"
get_screenShots(url)