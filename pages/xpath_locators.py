from selenium.webdriver.common.by import By


class LoginPageLocators:
    URL = "https://ris-bhr-test.aptvision.com"
    APT_LOGO = (By.XPATH, "//img[@src='/img/aptvision/logo_full.png']")
    LOGIN_FORM = (By.XPATH, "//form[@data-vv-scope='login-form']")
    USERNAME_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, "//span[contains(text(), 'Login')]")
    USERNAME_INPUT_ERROR_MSG = (By.XPATH, "//input[@name='email']/../../..//*[@class='v-messages__message']")
    PASSWORD_INPUT_ERROR_MSG = (By.XPATH, "//input[@name='password']/../../..//*[@class='v-messages__message']")
    POPUP_ERROR_MSG = (By.XPATH, "//div[@class='alert']")

class HomePageLocators:
    URL = "https://ris-bhr-test.aptvision.com/home/home/"
    MAIN_BODY = (By.ID, 'home-home-app1')
    WELCOME_MESSAGE_BOX = (By.ID, 'helper')
    SHORTCUT_ICONS_BOX = (By.ID, 'shortcut-icons-container')
    MENU_HOME_ICON = (By.ID, 'div-icon-home')
    MENU_SEARCH_BOX = (By.ID, 'div-aptsearch')
    MENU_QUICK_ACCESS_BOX = (By.ID, 'div-quickaccess')
    SEARCH_INPUT = (By.ID, 'txt-aptsearch')