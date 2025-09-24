from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def clickRegister(self,):
        register_button = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Daftar"))
        )
        register_button.click()

        self.wait.until(EC.url_contains("register"))

    def register_email(self, email):
        register_email_field = self.wait.until(
        EC.visibility_of_element_located((By.ID, "input-phone-email"))
    )
        register_email_field.send_keys(email)

