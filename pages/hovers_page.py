from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class HoversPage(BasePage):

    PAGE_URL = Links.HOVERS_PAGE

    HOVER_ELEMENT_1 = ("xpath", "//div[@data-testid='user-1']")
    HOVER_ELEMENT_2 = ("xpath", "//div[@data-testid='user-2']")
    HOVER_ELEMENT_3 = ("xpath", "//div[@data-testid='user-3']")

    TOOLTIP_1 = ("xpath", "//div[@data-testid='user-1']//h5")
    TOOLTIP_2 = ("xpath", "//div[@data-testid='user-2']//h5")
    TOOLTIP_3 = ("xpath", "//div[@data-testid='user-3']//h5")

    PROFILE_LINK_1 = ("xpath", "//div[@data-testid='user-1']//a")
    PROFILE_LINK_2 = ("xpath", "//div[@data-testid='user-2']//a")
    PROFILE_LINK_3 = ("xpath", "//div[@data-testid='user-3']//a")

    def __init__(self, driver):
        super().__init__(driver)
        self.actions = ActionChains(driver)

    def hover_over_element(self, element_locator):
        element = self.wait.until(EC.presence_of_element_located(element_locator))
        self.actions.move_to_element(element).perform()

    def is_tooltip_visible(self, tooltip_locator):
        tooltip = self.wait.until(EC.presence_of_element_located(tooltip_locator))
        return tooltip.is_displayed()
    
    def get_tooltip_text(self, tooltip_locator):
        tooltip = self.wait.until(EC.visibility_of_element_located(tooltip_locator))
        return tooltip.text