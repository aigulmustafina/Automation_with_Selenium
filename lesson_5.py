from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

try:
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get("http://suninjuly.github.io/find_xpath_form")

    input_name = browser.find_element(By.TAG_NAME, 'input')
    input_name.send_keys('Ivan')

    input_second = browser.find_element(By.NAME, 'last_name')
    input_second.send_keys('Petrov')

    input_city = browser.find_element(By.CLASS_NAME, 'form-control.city')
    input_city.send_keys("Smolensk")

    input_country = browser.find_element(By.ID, 'country')
    input_country.send_keys("Russia")



    button = browser.find_element(By.XPATH, '//form/div[6]/button[3]')
    button.click()

finally:
    time.sleep(40)
    browser.quit()