from selenium import webdriver
# PATH = "C:\Program Files (x86)\chromedriver\chromedriver.exe"
# need path to file so we can run it
driver = webdriver.Chrome()

driver.get("https://crypto.jobs/")
print(driver.title) # print driver title