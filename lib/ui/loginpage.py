
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_login_page_to_load(self):
            wait = WebDriverWait(self.driver, 30)
            wait.until(expected_conditions.visibility_of(self.driver.find_element_by_name("LoginForm")))

    def get_username_textbox(self):
        try:
            element = self.driver.find_element_by_name('username')
            return element
        except:
            return None

    def get_password_textbox(self):
        try:
            element = self.driver.find_element_by_name('pwd')
            return element
        except:
            return None

    def get_login_button(self):
        try:
            return self.driver.find_element_by_id("loginButton")
        except:
            return None

    def get_login_error_msg(self):
        try:
            return self.driver.find_element_by_xpath("//span[contains(text(),'Password')]")
        except:
            return None
