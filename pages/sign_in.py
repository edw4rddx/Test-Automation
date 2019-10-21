from pages.base_page import BasePage
from resources.data import GeneralData
from resources.locators import SignInPageLocators


class SignInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(GeneralData.ACCOUNT_URL)
        self.wait(seconds=2)

    def click_create_account_button(self):
        self.click(SignInPageLocators.CREATE_ACCOUNT_BUTTON)
        self.wait(seconds=1)

    def click_for_myself_button(self):
        self.click(SignInPageLocators.FOR_MYSELF_BUTTON)
        self.wait(seconds=2)
