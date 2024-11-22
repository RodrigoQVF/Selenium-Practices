from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time
import os


driver = uc.Chrome()
driver.get("https://www.tiktok.com/pt-BR")
loggingButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#header-login-button")))
loggingButton.click()
divLogging = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#login-modal > div.css-1e4hvda-DivModalContent.eg439om2")))
googleLogging = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginContainer > div > div > div > div:nth-child(4) > div.css-1jvzvb2-DivBoxContainer.e1cgu1qo0")))
defaultWindow = driver.current_window_handle
googleLogging.click()
for newTab in driver.window_handles:
    if newTab != defaultWindow:
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(newTab)

inputGmail = driver.find_element(By.CSS_SELECTOR, "#identifierId")
inputGmail.send_keys("henriquelucassouza0@gmail.com")
inputGmail.send_keys(Keys.ENTER)

inputGmailPassword = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")))
inputGmailPassword.send_keys("Facebook111603")
inputGmailPassword.send_keys(Keys.ENTER)

continueGmail = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#yDmH0d > c-wiz > div > div.JYXaTc.F8PBrb > div > div > div:nth-child(2) > div > div > button")))
continueGmail.click()


driver.switch_to.window(defaultWindow)
WebDriverWait(driver, 20).until(EC.number_of_windows_to_be(1))

loadVideoProfile = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#app-header > div > div.css-q8q040-DivHeaderRightContainer.e13wiwn60 > div.css-szsi1x-DivUploadContainer.e18d3d940 > a")))
loadVideoProfile.click()

loadVideo = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div > div.css-11nu78w.eosfqul1 > div.css-17xtaid.eyoaol20 > div > div > div > div > div.jsx-3600237669.upload-container.flow-opt-ui > div.jsx-3600237669.uploader > div > div > div.jsx-3444615393.upload-card.before-upload-new-stage.full-screen > div")))
loadVideo.click()



#Fazer a parte de upload do video de um diretorio especifico


time.sleep(50)

