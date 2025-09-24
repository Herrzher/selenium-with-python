from dotenv import load_dotenv
import os
from utils.driver_setup import create_driver
from pages.home_page import HomePage
from pages.login_pop import LoginPage
import time

# Load .env just once here
load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

driver = create_driver()
driver.get("https://www.tokopedia.com/")

home = HomePage(driver)
login = LoginPage(driver)

# Handle popup and go to login
home.close_popup_if_exists()
home.click_login()

# Now input email
login.input_email(EMAIL)
login.click_next_login()
login.uncheck_keep_login()
login.insert_password(PASSWORD)
login.real_login()

time.sleep(15)


driver.quit()
