import pytest
from base.base_test import BaseTest


class TestHoversPage(BaseTest):

    def test_hover_element_1(self):
        self.hovers_page.open()
        self.hovers_page.hover_over_element(self.hovers_page.HOVER_ELEMENT_1)
        assert self.hovers_page.is_tooltip_visible(self.hovers_page.TOOLTIP_1)
        assert self.hovers_page.get_tooltip_text(self.hovers_page.TOOLTIP_1) == "name: user1"

    def test_hover_element_2(self):
        self.hovers_page.open()
        self.hovers_page.hover_over_element(self.hovers_page.HOVER_ELEMENT_2)
        assert self.hovers_page.is_tooltip_visible(self.hovers_page.TOOLTIP_2)
        assert self.hovers_page.get_tooltip_text(self.hovers_page.TOOLTIP_2) == "name: user2"
          
    def test_hover_element_3(self):
        self.hovers_page.open()
        self.hovers_page.hover_over_element(self.hovers_page.HOVER_ELEMENT_3)
        assert self.hovers_page.is_tooltip_visible(self.hovers_page.TOOLTIP_3)
        assert self.hovers_page.get_tooltip_text(self.hovers_page.TOOLTIP_3) == "name: user3"