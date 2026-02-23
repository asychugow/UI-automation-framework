import time

import random
import pytest
from base.base_test import BaseTest


class TestCheckboxesPage(BaseTest):

    
    def test_checkbox_1_select(self):
        self.checkboxes_page.open()
        self.checkboxes_page.select_checkbox(self.checkboxes_page.CHECKBOX_1)
        self.checkboxes_page.is_checkbox_selected(self.checkboxes_page.CHECKBOX_1)

    def test_checkbox_2_deselect(self):
        self.checkboxes_page.open()
        self.checkboxes_page.select_checkbox(self.checkboxes_page.CHECKBOX_2)
        assert not self.checkboxes_page.is_checkbox_selected(self.checkboxes_page.CHECKBOX_2)

    def test_checkbox_2_select(self):
        self.checkboxes_page.open()
        self.checkboxes_page.select_checkbox(self.checkboxes_page.CHECKBOX_2)
        assert not self.checkboxes_page.is_checkbox_selected(self.checkboxes_page.CHECKBOX_2)
        self.checkboxes_page.select_checkbox(self.checkboxes_page.CHECKBOX_2)
        assert self.checkboxes_page.is_checkbox_selected(self.checkboxes_page.CHECKBOX_2)
        