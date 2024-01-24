from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import time

# Create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # installs chrome driver if it can't find one

url = 'https://cryptocurrencyjobs.co/?query=marketing'

# wait_driver = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
#    (By.CSS_SELECTOR, "ais-Hits-item")))

# wait_driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

print(soup)

# jobs = soup.find_all('li', class_="ais-Hits-item")

# for job in jobs:
#     print(job.getText())

# time.sleep(10)

# driver.quit()