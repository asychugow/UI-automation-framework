from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class HostPage(BasePage):

    PAGE_URL = Links.HOST_PAGE

    TEST_LOGIN_PAGE_LINK = ("xpath", "//a[text()='Test Login Page']")
    TEST_LOGIN_PAGE_LINK = ("xpath", "//a[text()='Test Register Page']")

    def click_test_login_page(self):
        self.wait.until(EC.element_to_be_clickable(self.TEST_LOGIN_PAGE_LINK)).click()

    def click_test_register_page(self):
        self.wait.until(EC.element_to_be_clickable(self.TEST_REGITER_PAGE_LINK)).click()
