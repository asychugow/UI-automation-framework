from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_BUTTON = ("xpath", "(//button[text()=' Save '])[1]")


    def change_first_name(self, new_first_name):
        first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
        first_name_field.clear()
        assert first_name_field.get_attribute("value") == "", "Поле не пустое!"
        first_name_field.send_keys(new_first_name)
        self.name = new_first_name

    def click_save(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    def is_changes_saved(self):
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))