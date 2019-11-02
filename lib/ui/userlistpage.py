

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class UserListPage():
    def __init__(self, driver):
        self.driver = driver

    def wait_for_user_list_page_to_load(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of(
            self.driver.find_element_by_id('container')))

    def get_add_new_user_button(self):
        try:
           return self.driver.find_element_by_xpath("//input[@value='Add New User']")
        except:
            return None

    def get_add_user_success_msg(self):
        try:
            return self.driver.find_element_by_xpath("//span[text()='User has been successfully added.']")
        except:
            return None

    def get_user_from_list(self, lastname, firstname, username):
        link_text = lastname+', '+firstname+' ('+username+')'
        try:
            return self.driver.find_element_by_link_text(link_text)
        except:
            return None

