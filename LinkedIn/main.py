from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import time




driver = uc.Chrome()

driver.get("https://www.linkedin.com/feed/")
loginInput = driver.find_element(By.CSS_SELECTOR, "#username")
passwordInput = driver.find_element(By.CSS_SELECTOR, "#password")
loginInput.send_keys("henriquelucassouza0@gmail.com")
passwordInput.send_keys("Facebook11")
time.sleep(2)
buttonLogin = driver.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button").click()

searchInput = driver.find_element(By.CSS_SELECTOR, "#global-nav-typeahead > input")
searchInput.send_keys("tech recruiter brazil")
searchInput.send_keys(Keys.ENTER)
time.sleep(5)
peopleButton = driver.find_element(By.CSS_SELECTOR, "#search-reusables__filters-bar > ul > li:nth-child(3) > button").click()

time.sleep(10)
mainPeople = driver.find_element(By.CSS_SELECTOR, "body > div.application-outlet > div.authentication-outlet > div.scaffold-layout.scaffold-layout--breakpoint-xl.scaffold-layout--main-aside.scaffold-layout--reflow.search__srp--has-right-rail-top-offset > div > div.scaffold-layout__row.scaffold-layout__content.scaffold-layout__content--main-aside.scaffold-layout__content--has-aside > main")


time.sleep(10)
connectPeople = mainPeople.find_elements(By.TAG_NAME, "button")



for i in connectPeople:
    if i.text == "Conectar" or i.text == "Seguir":
        i.click()
        time.sleep(5)
        divConnect = driver.find_element(By.ID, "artdeco-modal-outlet")
        buttonNote = divConnect.find_elements(By.TAG_NAME, "button")
        for j in buttonNote:
            if j.text == "Enviar sem nota":
                j.click()
                time.sleep(5)


time.sleep(500)