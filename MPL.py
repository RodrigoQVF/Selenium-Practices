from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

login = "applebatata"
password = "22casa44"

driver.get("https://www.riotgames.com/pt-br")

Sandwich = driver.find_element(By.CSS_SELECTOR, "#riotbar-right-content > div.undefined.riotbar-mobile-nav-reset > div.TFqJpnsDlEvg2svwtFM2MQ\=\=.riotbar-menu-icon").click()
time.sleep(5)
buttonLogin = driver.find_element(By.CSS_SELECTOR, "#riotbar-mobile-menu > div._5Uh3QX6jG9kZGRoc2QzHFA\=\=.riotbar-mobile-menu-anonymous-link-wrapper > a").click()
time.sleep(5)

loginLabel = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > div > div > div.sc-bjMMwb.htfqug > div.sc-fmSAUk.hPebxe.sc-eIrltS.cwPKYC.auth-textfield > div > input[type=text]")
passwordLabel = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > div > div > div.sc-bjMMwb.htfqug > div.sc-fmSAUk.hPebxe.sc-hAYhfR.jtCnjz.auth-textfield > div > input[type=password]")
checkboxKeepLogin = driver.find_element(By.CSS_SELECTOR, "#rememberme")
loginLabel.send_keys(login)
time.sleep(3)
passwordLabel.send_keys(password)

checkboxKeepLogin.click()
# time.sleep(3)

time.sleep(120)











