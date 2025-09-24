# pages/home_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def close_popup_if_exists(self):
        popup = self.driver.find_elements(By.CSS_SELECTOR, 'div.css-11hzwo5 > button')
        if popup:
            self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.css-11hzwo5 > button'))
            ).click()

    def click_login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="btnHeaderLogin"]'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
        self.driver.execute_script("arguments[0].click();", login_button)
