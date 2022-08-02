from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get("http://suninjuly.github.io/selects1.html")
    val1 = browser.find_element(By.ID, 'num1').text
    val2 = browser.find_element(By.ID, 'num2').text
    num = str(int(val1) + int(val2))
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(num)

    submit = browser.find_element(By.XPATH, "/html/body/div/form/button")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
