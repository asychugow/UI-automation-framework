import random
import allure
from base.base_test import BaseTest


@allure.feature("Profile functionality")
class ProfileFeatureTests(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()

        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()

        self.my_info_page.is_opened()
        self.my_info_page.change_first_name(f"Test {random.randint(1,50)}")
        self.my_info_page.click_save()
        self.my_info_page.is_changes_saved()

