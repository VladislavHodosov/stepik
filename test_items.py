from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_that_add_basket_button_present(browser):
    browser.get(link)
    WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[class*='add-to-basket']")))
    buttonAddToBasket = browser.find_element(By.CSS_SELECTOR, "button[class*='add-to-basket']")
    assert buttonAddToBasket.is_displayed() is True