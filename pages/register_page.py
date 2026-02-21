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

    def enter_username(self, new_name):
            username_field = self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD))
            username_field.send_keys(new_name)
            self.name = new_name

    def enter_password(self, new_password):
            password_field = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD))
            password_field.send_keys(new_password)
            self.password = new_password
        
    def confirm_password(self, new_password):
            password_field = self.wait.until(EC.element_to_be_clickable(self.CONFIRM_PASSWORD_FIELD))
            password_field.send_keys(new_password)
            self.password = new_password

    def click_register_button(self):
        self.wait.until(EC.element_to_be_clickable(self.REGISTER_BUTTON)).click()

