import time
import random
import pytest
from base.base_test import BaseTest

class TestInputsPage(BaseTest):

    
    def test_number_input(self):
        self.host_page.open()
        self.inputs_page.open()
        self.inputs_page.enter_number("1999")
        self.inputs_page.click_display_inputs_button()
        self.inputs_page.get_output_number()
        assert self.inputs_page.get_output_number() == "1999"

    def test_text_input(self):
        self.host_page.open()
        self.inputs_page.open()
        self.inputs_page.enter_text("text")
        self.inputs_page.click_display_inputs_button()
        self.inputs_page.get_output_text()
        assert self.inputs_page.get_output_text() == "text"

    def test_password_input(self):
        self.host_page.open()
        self.inputs_page.open()
        self.inputs_page.enter_password("SecretPass123!")
        self.inputs_page.click_display_inputs_button()
        self.inputs_page.get_output_password()
        assert self.inputs_page.get_output_password() == "SecretPass123!"
