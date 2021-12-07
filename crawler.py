from selenium import webdriver
CRAWL_URL = 'https://www.apple.com/tw/macbook-pro/'

def init_driver():
    driver = webdriver.Chrome('./chromedriver')
    return driver

def crawl(driver):
    driver.get(CRAWL_URL)