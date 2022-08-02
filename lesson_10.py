from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get("http://suninjuly.github.io/execute_script.html")
    x = browser.find_element(By.ID, 'input_value').text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    answer = calc(x)
    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(answer)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    check = browser.find_element(By.ID, 'robotCheckbox')
    check.click()

    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()

    button.click()
finally:
    time.sleep(5)
    browser.quit()