import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    submitButton = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submitButton.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element(By.ID, "input_value").text
    answerTextBox = browser.find_element(By.ID, "answer")
    y = calc(x)
    answerTextBox.send_keys(y)
    submitButton = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submitButton.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()