import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.host_page import HostPage
from pages.register_page import RegisterPage
from pages.secure_page import SecurePage
from pages.inputs_page import InputsPage
from pages.dropdown_page import DropdownPage
from pages.checkboxes_page import CheckboxesPage



class BaseTest:

    data: Data

    host_page: HostPage
    login_page: LoginPage
    register_page: RegisterPage
    secure_page: SecurePage
    inputs_page: InputsPage
    dropdown_page: DropdownPage
    checkboxes_page: CheckboxesPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.host_page = HostPage(driver)
        request.cls.login_page = LoginPage(driver)
        request.cls.register_page = RegisterPage(driver)
        request.cls.secure_page = SecurePage(driver)
        request.cls.inputs_page = InputsPage(driver)
        request.cls.dropdown_page = DropdownPage(driver)
        request.cls.checkboxes_page = CheckboxesPage(driver)