

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class HomePage():
    def __init__(self, driver):
        self.driver = driver

    def wait_for_home_page_to_load(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of(
            self.driver.find_element_by_id('container')))

    def get_users_tab(self):
        try:
            return self.driver.find_element_by_link_text("Users")
        except:
            return None

    def get_logout_button(self):
        try:
            return self.driver.find_element_by_xpath("//img[@alt='Logout']")
        except:
            return None
