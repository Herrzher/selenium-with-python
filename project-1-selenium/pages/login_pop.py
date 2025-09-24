from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def input_email(self, email):
        if email is None:
            email = os.getenv("EMAIL") 
        email_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "email-phone"))
        )
        email_field.send_keys(email)

    def click_next_login(self):
        next_login_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="email-phone-submit"]'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", next_login_button)
        self.driver.execute_script("arguments[0].click();", next_login_button)

    def uncheck_keep_login(self):
        checkbox_area = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span.css-4iffx4-unf-checkbox__area"))
        )
        # check if checked (svg inside means "checked")
        is_checked = len(checkbox_area.find_elements(By.TAG_NAME, "svg")) > 0
        if is_checked:
            self.driver.execute_script("arguments[0].click();", checkbox_area)
    
    def insert_password(self, pwd):
        if pwd is None:
            pwd = os.getenv("PASSWORD")
        pass_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "password-input"))
        )
        pass_field.send_keys(pwd)

    def real_login(self):
        real_login_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span[aria-label='login-button']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", real_login_button)
        self.driver.execute_script("arguments[0].click();", real_login_button)
