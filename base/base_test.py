import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.host_page import HostPage
from pages.register_page import RegisterPage
from pages.secure_page import SecurePage


class BaseTest:

    data: Data

    host_page: HostPage
    login_page: LoginPage
    personal_page: RegisterPage
    secure_page: SecurePage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.host_page = HostPage(driver)
        request.cls.login_page = LoginPage(driver)
        request.cls.register_page = RegisterPage(driver)
        request.cls.secure_page = SecurePage(driver)