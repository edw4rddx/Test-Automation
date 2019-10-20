from selenium.webdriver.common.by import By


class SignInPageLocators:
    """A class for main page locators. All main page locators should come here"""
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//*[text()='Створити обліковий запис']")
    FOR_MYSELF_BUTTON = (By.XPATH, "//*[text()='Для себе']")


class CreateAccountPageLocators:
    """A class for search results locators. All search results locators should come here"""
    FIRST_NAME_TEXTBOX = (By.ID, "firstName")
    LAST_NAME_TEXTBOX = (By.ID, "lastName")
    USERNAME_TEXTBOX = (By.ID, "username")
    PASSWORD_TEXTBOX = (By.NAME, "Passwd")
    CONFIRM_TEXTBOX = (By.NAME, "ConfirmPasswd")
    NEXT_BUTTON = (By.ID, "accountDetailsNext")
