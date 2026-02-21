import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class HostPage(BasePage):

    PAGE_URL = Links.HOST_PAGE

    MY_INFO_BUTTON = ("xpath", "//span[text()='My Info']")

    def click_my_info_link(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()