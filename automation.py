from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service1 = Service(executable_path='./chromedriver.exe')
chrome = webdriver.Chrome(service=service1)
chrome.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
chrome.maximize_window()
button = chrome.find_element(By.CLASS_NAME, 'btn-default')
# assert ('show message' in chrome.page_source)

sample=chrome.find_element(By.ID,'user-message')
sample.clear()
sample.send_keys('Anoynomous')

button.click()
output=chrome.find_element(By.ID,'display')
assert 'Anoynomous' in output.text
time.sleep(10)
chrome.quit()