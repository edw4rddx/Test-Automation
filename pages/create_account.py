from pages.base_page import BasePage
from resources.locators import CreateAccountPageLocators as Locators


class CreateAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_name(self, text):
        self.enter_text(Locators.FIRST_NAME_TEXTBOX, text)

    def enter_last_name(self, text):
        self.enter_text(Locators.LAST_NAME_TEXTBOX, text)

    def enter_username(self, text):
        self.enter_text(Locators.USERNAME_TEXTBOX, text)

    def enter_password(self, text):
        self.enter_text(Locators.PASSWORD_TEXTBOX, text)

    def enter_confirm(self, text):
        self.enter_text(Locators.CONFIRM_TEXTBOX, text)

    def click_next_button(self):
        self.click(Locators.NEXT_BUTTON)
        self.wait(seconds=2)

    def populate_all_fields(self, first_name, last_name, username, password, confirm):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_username(username)
        self.enter_password(password)
        self.enter_confirm(confirm)
