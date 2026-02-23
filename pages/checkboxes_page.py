from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC



class CheckboxesPage(BasePage):

    PAGE_URL = Links.CHECKBOXES_PAGE

    CHECKBOX_1 = ("xpath", "//input[@id='checkbox1']")
    CHECKBOX_2 = ("xpath", "//input[@id='checkbox2']")


    def select_checkbox(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()


    def is_checkbox_selected(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator)).is_selected()