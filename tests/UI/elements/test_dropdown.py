import time

import random
import pytest
from base.base_test import BaseTest


class TestDropdownPage(BaseTest):

    
    def test_dropdown_select(self):
        self.dropdown_page.open()
        self.dropdown_page.select_option("Option 1")
        assert self.dropdown_page.get_selected_option() == "Option 1"

    def test_dropdown_change_select(self):
        self.dropdown_page.open()
        self.dropdown_page.select_option("Option 1")
        assert self.dropdown_page.get_selected_option() == "Option 1"
        self.dropdown_page.select_option("Option 2")
        assert self.dropdown_page.get_selected_option() == "Option 2"

        
    def test_dropdown_country_select(self):
        self.dropdown_page.open()
        self.dropdown_page.select_country_option("BY")
        assert self.dropdown_page.get_selected_country_option() == "Belarus"

    def test_dropdown_change_country_select(self):
        self.dropdown_page.open()
        self.dropdown_page.select_country_option("AR")
        assert self.dropdown_page.get_selected_country_option() == "Argentina"
        self.dropdown_page.select_country_option("BB")
        assert self.dropdown_page.get_selected_country_option() == "Barbados"