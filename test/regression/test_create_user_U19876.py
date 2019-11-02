import unittest

from lib.ui.addnewuserpage import AddNewUserPage
from lib.ui.homepage import HomePage
from lib.ui.loginpage import LoginPage
from lib.ui.userlistpage import UserListPage
from lib.util import create_driver


class TestCreateUser(unittest.TestCase):
    def setUp(self):
        self.driver = create_driver.get_driver_instance()
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.user_list = UserListPage(self.driver)
        self.add_new_user = AddNewUserPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_create_user_tc138796(self):
        self.login_page.wait_for_login_page_to_load()
        self.login_page.get_username_textbox().send_keys('admin')
        self.login_page.get_password_textbox().send_keys('manager')
        self.login_page.get_login_button().click()

        self.home_page.wait_for_home_page_to_load()
        self.home_page.get_users_tab().click()

        self.user_list.wait_for_user_list_page_to_load()
        self.user_list.get_add_new_user_button().click()

        self.add_new_user.wait_for_add_new_user_page_to_load()
        self.add_new_user.get_username_textbox().send_keys('User')
        self.add_new_user.get_password_textbox().send_keys('pass1')
        self.add_new_user.get_retype_password_textbox().send_keys('pass1')
        self.add_new_user.get_first_name_textbox().send_keys('First1')
        self.add_new_user.get_last_name_textbox().send_keys('Last1')
        self.add_new_user.get_create_user_button().click()

        self.user_list.wait_for_user_list_page_to_load()
        actual_text = self.user_list.get_add_user_success_msg().text
        expected_text = 'User has been successfully added.'
        assert actual_text == expected_text

        user_text = \
            self.user_list.get_user_from_list('Last1', 'First1', 'User').text

        assert 'Last1' in user_text
        assert 'First1' in user_text
        assert 'User' in user_text
