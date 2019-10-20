import unittest
import HtmlTestRunner
from pages.sign_in import SignInPage
from pages.create_account import CreateAccountPage
from resources.data import GeneralData, AccountTestData
from tests.base_test import BaseGoogleAccountCreation


class TestAccountCreation(BaseGoogleAccountCreation):
    def setUp(self):
        super().setUp()

    def test_1_sign_in_page_title(self):
        self.sign_in_page = SignInPage(self.driver)
        self.sign_in_page.wait(1)
        self.sign_in_page.assert_in_title(GeneralData.SIGN_IN_PAGE_TITLE)

    def test_2_create_account_for_myself(self):
        self.sign_in_page = SignInPage(self.driver)
        self.sign_in_page.click_create_account_button()
        self.sign_in_page.wait(1)
        self.sign_in_page.click_for_myself_button()

        self.create_account_page = CreateAccountPage(self.driver)
        self.create_account_page.assert_in_title(GeneralData.CREATE_ACCOUNT_PAGE_TITLE)

    def test_3_invalid_username_data(self):
        self.sign_in_page = SignInPage(self.driver)
        self.sign_in_page.click_create_account_button()
        self.sign_in_page.wait(1)
        self.sign_in_page.click_for_myself_button()

        self.create_account_page = CreateAccountPage(self.driver)
        data = AccountTestData.InvalidUsernameData
        for username in data['username']:
            self.create_account_page.populate_all_fields(first_name=data['firstname'],
                                                         last_name=data['lastname'],
                                                         username=username,
                                                         password=data['password'],
                                                         confirm=data['password'])

            self.create_account_page.click_next_button()
            self.create_account_page.wait(2)
            self.create_account_page.assert_in_source(data['error'])

    def test_4_invalid_password_data(self):
        self.sign_in_page = SignInPage(self.driver)
        self.sign_in_page.click_create_account_button()
        self.sign_in_page.wait(1)
        self.sign_in_page.click_for_myself_button()

        self.create_account_page = CreateAccountPage(self.driver)
        data = AccountTestData.InvalidPasswordData
        for password in data['password']:
            self.create_account_page.populate_all_fields(first_name=data['firstname'],
                                                         last_name=data['lastname'],
                                                         username=data['username'],
                                                         password=password,
                                                         confirm=password)

            self.create_account_page.click_next_button()
            self.create_account_page.wait(2)
            self.create_account_page.assert_in_source(data['error'])


if __name__ == '__main__':
    report_title = "Test Google Account Creation - Username and Password fields validation"
    test_runner = HtmlTestRunner.HTMLTestRunner(report_title=report_title, open_in_browser=True)
    unittest.main(testRunner=test_runner)

