import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_view():
   
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
	
    service = Service()
    
    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = "https://ak1t3r.github.io/"
    driver.get(url=url)
	
    element = driver.find_element(by=By.CSS_SELECTOR, value="[class*='linsk__link']")
    element.click()

    driver.back()
    

	