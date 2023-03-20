from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    robotCheckBox = browser.find_element(By.ID, "robotCheckbox")
    robotsRule = browser.find_element(By.ID, "robotsRule")
    answerTextBox = browser.find_element(By.ID, "answer")
    submitButton = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

    x = x_element.get_attribute("valuex")
    y = calc(x)

    answerTextBox.send_keys(y)
    robotCheckBox.click()
    robotsRule.click()
    submitButton.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()