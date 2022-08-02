from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
try:
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get("http://suninjuly.github.io/huge_form.html")

    elements = browser.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys('Secret')
    button = browser.find_element(By.CSS_SELECTOR, 'body > div > form > button')
    button.click()

finally:
    time.sleep(40)
    browser.quit()