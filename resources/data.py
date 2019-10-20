class GeneralData:
    ACCOUNT_URL = "https://accounts.google.com"
    SIGN_IN_PAGE_TITLE = "Вхід – облікові записи Google"
    CREATE_ACCOUNT_PAGE_TITLE = "Вхід – облікові записи Google"


class AccountTestData:
    InvalidUsernameData = dict(firstname="John", lastname="Doe", password="JohnDoe!1337!",
                               username=['a@a.a', 'a@@a.a', 'a@a', 'a@>a', 'a_@ab', 'k_@l<'],
                               error="Дозволені лише літери (a–z), числа (0–9) та крапки (.).")

    InvalidPasswordData = dict(firstname="John", lastname="Doe",
                               password=['a', 'a1'], username="python",
                               error="Пароль має містити щонайменше 8 символів")


