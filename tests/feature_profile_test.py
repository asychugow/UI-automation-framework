from base.base_test import BaseTest


class ProfileFeatureTests(BaseTest):

    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login()
        self.login_page.enter_password()
        self.login_page.click_submit_button()

        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()

        self.my_info_page.is_opened()
        self.my_info_page.change_first_name()

