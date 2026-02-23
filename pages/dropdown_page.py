from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select



class DropdownPage(BasePage):

    PAGE_URL = Links.DROPDOWN_PAGE

    SELECT_LOCATOR = ("xpath", "//select[@id='dropdown']")
    COUNTRY_SELECT_LOCATOR = ("xpath", "//select[@id='country']")


   
    def select_option(self, value):
        dropdown = Select(self.wait.until(EC.element_to_be_clickable(self.SELECT_LOCATOR)))
        dropdown.select_by_visible_text(value)

    def get_selected_option(self):
        dropdown = Select(self.wait.until(EC.element_to_be_clickable(self.SELECT_LOCATOR)))
        return dropdown.first_selected_option.text



    def select_country_option(self, value):
        dropdown = Select(self.wait.until(EC.element_to_be_clickable(self.COUNTRY_SELECT_LOCATOR)))
        dropdown.select_by_value(value)

    def get_selected_country_option(self):
        dropdown = Select(self.wait.until(EC.element_to_be_clickable(self.COUNTRY_SELECT_LOCATOR)))
        return dropdown.first_selected_option.text