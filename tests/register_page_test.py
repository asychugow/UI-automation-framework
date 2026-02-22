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

    def test_missing_username_field(self):
        self.host_page.open()
        self.register_page.open()
        self.register_page.enter_password("Password123!")
        self.register_page.confirm_password("Password123!")
        time.sleep(1)
        self.register_page.click_register_button()
        self.register_page.is_all_fields_required_message_displayed()

    def test_missing_password_field(self):
        self.host_page.open()
        self.register_page.open()
        self.register_page.enter_username(f"Testpractice{random.randint(1000,9999)}")
        self.register_page.confirm_password("Password123!")
        time.sleep(1)
        self.register_page.click_register_button()
        self.register_page.is_all_fields_required_message_displayed()

    def test_nonmatching_password_fields(self):
        self.host_page.open()
        self.register_page.open()
        self.register_page.enter_username(f"Testpractice{random.randint(1000,9999)}")
        self.register_page.enter_password("Password123!")
        self.register_page.confirm_password("Password123!!")
        time.sleep(1)
        self.register_page.click_register_button()
        self.register_page.is_passwords_dont_match_message_displayed()



