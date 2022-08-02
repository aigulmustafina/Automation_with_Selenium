from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import math
import time

try:
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button = browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_el = browser.find_element(By.ID, 'input_value')
    x = x_el.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    button.click()

finally:
    time.sleep(5)
    browser.quit()