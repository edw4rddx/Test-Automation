import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Parent BasePage class"""

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)).click()

    def clear_textbox(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)).clear()

    def enter_text(self, locator, text):
        self.clear_textbox(locator)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)).send_keys(text)

    def assert_in_title(self, text):
        WebDriverWait(self.driver, 10).until(
            EC.title_contains(text),
            f"Actual title: {self.driver.title} is not equal to expected: {text}")

    def assert_in_source(self, text):
        assert text in self.driver.page_source

    @staticmethod
    def wait(seconds):
        time.sleep(seconds)

