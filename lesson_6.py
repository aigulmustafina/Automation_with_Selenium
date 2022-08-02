from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

try:
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get("http://suninjuly.github.io/registration2.html")
    input_name = browser.find_element(By.XPATH, '//form/div[1]/div[1]/input')
    input_name.send_keys('Ivan')

    input_second = browser.find_element(By.XPATH, '//form/div[1]/div[2]/input')
    input_second.send_keys('Petrov')

    input_email = browser.find_element(By.XPATH, '//form/div[1]/div[3]/input')
    input_email.send_keys("ivan@mail.ru")

    button = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    button.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
