from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class InputsPage(BasePage):

    PAGE_URL = Links.INPUTS_PAGE

    DISPLAY_INPUTS_BUTTON = ("xpath", "//button[@id='btn-display-inputs']")
    CLEAR_INPUTS_BUTTON = ("xpath", "//button[@id='btn-clear-inputs']")
    
    NUMBER_INPUT_FIELD = ("xpath", "//input[@id='input-number']")
    TEXT_INPUT_FIELD = ("xpath", "//input[@id='input-text']")
    PASSWORD_INPUT_FIELD = ("xpath", "//input[@id='input-password']")
    DATE_INPUT_FIELD = ("xpath", "//input[@id='input-date']")

    NUMBER_OTPUT_FIELD = ("id", "output-number")
    TEXT_OTPUT_FIELD = ("id", "output-text")
    PASSWORD_OTPUT_FIELD = ("id", "output-password")
    DATE_OTPUT_FIELD = ("id", "output-date")



    def click_display_inputs_button(self):
        self.wait.until(EC.element_to_be_clickable(self.DISPLAY_INPUTS_BUTTON)).click()

    def click_clear_inputs_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CLEAR_INPUTS_BUTTON)).click()   



    def enter_number(self, number):
        self.wait.until(EC.element_to_be_clickable(self.NUMBER_INPUT_FIELD)).send_keys(number)

    def enter_text(self, text):
        self.wait.until(EC.element_to_be_clickable(self.TEXT_INPUT_FIELD)).send_keys(text)
    
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT_FIELD)).send_keys(password)





    def get_output_number(self):
        return self.wait.until(EC.visibility_of_element_located(self.NUMBER_OTPUT_FIELD)).text

    def get_output_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.TEXT_OTPUT_FIELD)).text
    
    def get_output_password(self):
        return self.wait.until(EC.visibility_of_element_located(self.PASSWORD_OTPUT_FIELD)).text



    