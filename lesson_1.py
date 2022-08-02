import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
time.sleep(5)
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)
textarea = driver.find_element(By.CSS_SELECTOR, '.textarea')
textarea.send_keys('get()')
time.sleep(5)
submit_button = driver.find_element(By.CSS_SELECTOR, '.submit-submission')
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(2)
submit_button.click()
time.sleep(5)
driver.quit()