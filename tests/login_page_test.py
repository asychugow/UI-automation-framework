import time

import random
import pytest
from base.base_test import BaseTest

class TestLoginPage(BaseTest):

    
    def test_valid_login(self):
        self.host_page.open()
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        time.sleep(2)
        self.login_page.click_submit_button()
        self.secure_page.is_opened()
        self.secure_page.is_success_message_displayed()
        self.secure_page.is_logout_button_displayed()

    def test_invalid_login(self):
        self.host_page.open()
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_login("practicepractice")
        self.login_page.enter_password(self.data.PASSWORD)
        time.sleep(2)
        self.login_page.click_submit_button()
        self.login_page.is_invalid_user_message_displayed()
        self.login_page.is_opened()

