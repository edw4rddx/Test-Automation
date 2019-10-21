from selenium.webdriver.common.by import By


class SignInPageLocators:
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//*[text()='Створити обліковий запис']")
    FOR_MYSELF_BUTTON = (By.XPATH, "//*[text()='Для себе']")


class CreateAccountPageLocators:
    FIRST_NAME_TEXTBOX = (By.ID, "firstName")
    LAST_NAME_TEXTBOX = (By.ID, "lastName")
    USERNAME_TEXTBOX = (By.ID, "username")
    PASSWORD_TEXTBOX = (By.NAME, "Passwd")
    CONFIRM_TEXTBOX = (By.NAME, "ConfirmPasswd")
    NEXT_BUTTON = (By.ID, "accountDetailsNext")
