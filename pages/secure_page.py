from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class SecurePage(BasePage):

    PAGE_URL = Links.SECURE_PAGE

    SUCCESS_MESSAGE = ("xpath", "//b[contains(text(), 'You logged into a secure area!')]")
    LOGOUT_BUTTON = ("xpath", "//i[normalize-space(text())='Logout']")
    

    def is_success_message_displayed(self):
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))

    def is_logout_button_displayed(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON))