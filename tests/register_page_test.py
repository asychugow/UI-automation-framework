import time

import random
import pytest
from base.base_test import BaseTest

class TestLoginPage(BaseTest):

    
    def test_successful_registration(self):
        self.host_page.open()
        self.register_page.open()
        self.register_page.enter_username(f"Testpractice{random.randint(1000,9999)}")
        self.register_page.enter_password("Password123!")
        self.register_page.confirm_password("Password123!")
        time.sleep(1)
        self.register_page.click_register_button()
        self.login_page.is_opened()
        self.login_page.is_succeful_registration_message_displayed()

