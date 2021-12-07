from selenium import webdriver
import time
CRAWL_URL = 'https://www.apple.com/tw/macbook-pro/'
TARGET_CLASS_NAME   = 'bottom-intro'

def init_driver():
    driver = webdriver.Chrome('./chromedriver')
    return driver

def crawler_helper(driver):
    if driver is not None:
        driver.get(CRAWL_URL)
    es = driver.find_elements_by_class_name(TARGET_CLASS_NAME)  
    for e in es:
        print(e.get_attribute("data-analytics-title"))

def crawl(driver, duration=5):
    while(True):
        crawler_helper(driver)
        time.sleep(duration)
        