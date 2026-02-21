from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_FIELD = ("xpath", "//input[@id='username']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit-login']")

    INVALID_USER_MESSAGE = ("xpath", "//b[contains(text(), 'Your username is invalid!')]")

    
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    def click_submit_button(self):
        self.wait.until(EC.visibility_of_element_located(self.SUBMIT_BUTTON)).click()

    def is_invalid_user_message_displayed(self):
        self.wait.until(EC.visibility_of_element_located(self.INVALID_USER_MESSAGE))