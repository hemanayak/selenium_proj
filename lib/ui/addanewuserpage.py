from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class AddNewUserPage():
    def __init__(self, driver):
        self.driver = driver

    def wait_for_add_new_user_page_to_load(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of(
            self.driver.find_element_by_id('container')))

    def get_username_textbox(self):
        try:
            return self.driver.find_element_by_name("username")
        except:
            return None

    def get_password_textbox(self):
        try:
            return self.driver.find_element_by_name("passwordText")
        except:
            return None

    def get_retype_password_textbox(self):
        try:
            return self.driver.find_element_by_name("passwordTextRetype")
        except:
            return None

    def get_first_name_textbox(self):
        try:
            return self.driver.find_element_by_name("firstName")
        except:
            return None

    def get_last_name_textbox(self):
        try:
            return self.driver.find_element_by_name("lastName")
        except:
            return None

    def get_create_user_button(self):
        try:
            return self.driver.find_element_by_xpath("//input[@type='submit']")
        except:
            return None
