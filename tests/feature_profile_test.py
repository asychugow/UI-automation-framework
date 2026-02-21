import time

import random
import pytest
from base.base_test import BaseTest

class TestOpenLoginPage(BaseTest):

    
    def test_open_login_page(self):
        self.host_page.open()
        self.login_page.open()

class TestOpenRegisterPage(BaseTest):

    def test_open_register_page(self):
        self.host_page.open()
        self.register_page.open()
