from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

fistNameForm = driver.find_element(By.CSS_SELECTOR, "#post-body-3077692503353518311 > div:nth-child(1) > div > div > h2:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > input").send_keys("Rodrigo")
lastNameForm = driver.find_element(By.CSS_SELECTOR, "#post-body-3077692503353518311 > div:nth-child(1) > div > div > h2:nth-child(2) > div:nth-child(1) > div > div:nth-child(5) > input").send_keys("Queiroz")

genderCheck = driver.find_element(By.CSS_SELECTOR, "#sex-0").click()

yearExperience = driver.find_element(By.CSS_SELECTOR, "#exp-6").click()

date = driver.find_element(By.CSS_SELECTOR, "#datepicker").send_keys("16/11/2003")

automationTester = driver.find_element(By.CSS_SELECTOR, "#profession-1").click()
automationTool = driver.find_element(By.CSS_SELECTOR, "#tool-0").click()

continents = driver.find_element(By.CSS_SELECTOR, "#continents")
selectContinents = Select(continents)
selectContinents.select_by_visible_text("South America")
time.sleep(5)




