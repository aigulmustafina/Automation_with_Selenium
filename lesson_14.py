from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import time

try:
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get(" http://suninjuly.github.io/explicit_wait2.html")

    price = '$100'
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), price))

    print(button)

    book = browser.find_element(By.ID, 'book')
    book.click()

    x_el = browser.find_element(By.ID, 'input_value')
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_el)
    x = x_el.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    button = browser.find_element(By.ID, 'solve')
    button.click()

finally:
    time.sleep(5)
    browser.quit()