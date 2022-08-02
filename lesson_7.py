from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import math
import time

try:
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get("http://suninjuly.github.io/math.html")
    x_el = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_el.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    check = browser.find_element(By.ID, 'robotCheckbox')
    check.click()

    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio.click()

    submit = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
