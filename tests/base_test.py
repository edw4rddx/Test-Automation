import unittest
from selenium import webdriver


class BaseGoogleAccountCreation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
