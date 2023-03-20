import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'review.py')  # добавляем к этому пути имя файла

    firstName = browser.find_element(By.NAME, "firstname")
    lastName = browser.find_element(By.NAME, "lastname")
    email = browser.find_element(By.NAME, "email")
    uploadButton = browser.find_element(By.ID, "file")
    submitButton = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

    firstName.send_keys("Vlad")
    lastName.send_keys("Vladik")
    email.send_keys("email")
    uploadButton.send_keys(file_path)
    submitButton.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()