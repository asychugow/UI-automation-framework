import time

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class RegisterPage(BasePage):

    PAGE_URL = Links.REGISTER_PAGE

    USERNAME_FIELD = ("xpath", "//input[@id='username']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    CONFIRM_PASSWORD_FIELD = ("xpath", "//input[@id='confirmPassword']")
    REGISTER_BUTTON = ("xpath", "//button[text()='Register']")

    ALL_FIELDS_REQUiRED_MESSAGE = ("xpath", "//b[contains(text(), 'All fields are required.')]")
    PASSWORDS_DONT_MATCH_MESSAGE = ("xpath", "//b[contains(text(), 'Passwords do not match.')]")



    def enter_username(self, name):
            username_field = self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD))
            username_field.send_keys(name)

    def enter_password(self, password):
            password_field = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD))
            password_field.send_keys(password)
        
    def confirm_password(self, password):
            password_field = self.wait.until(EC.element_to_be_clickable(self.CONFIRM_PASSWORD_FIELD))
            password_field.send_keys(password)

    def click_register_button(self):
        self.wait.until(EC.element_to_be_clickable(self.REGISTER_BUTTON)).click()

    def is_all_fields_required_message_displayed(self):
        self.wait.until(EC.visibility_of_element_located(self.ALL_FIELDS_REQUiRED_MESSAGE))

    def is_passwords_dont_match_message_displayed(self):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORDS_DONT_MATCH_MESSAGE))

