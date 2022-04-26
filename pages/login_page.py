from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.xpath_locators import LoginPageLocators
from pages import ENV_URL

import time
import helpers as hp


class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        # self.browser.get(LoginPageLocators.URL)
        self.browser.get(ENV_URL)

    def check_if_contains_all_elements(self):
        time.sleep(1)
        return self.browser.find_element(*LoginPageLocators.APT_LOGO), \
               self.browser.find_element(*LoginPageLocators.LOGIN_FORM),\
               self.browser.find_element(*LoginPageLocators.USERNAME_INPUT),\
               self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT),\
               self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)

    def clear_login_form(self):
        time.sleep(1)
        a = ActionChains(self.browser)
        a.move_to_element(self.browser.find_element(*LoginPageLocators.USERNAME_INPUT)).double_click().click().send_keys(Keys.BACKSPACE).perform()
        a.move_to_element(self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)).double_click().click().send_keys(Keys.BACKSPACE).perform()

    def login(self, email, password):
        self.clear_login_form()
        self.browser.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def login_x_times(self, email, password, x):
        for i in range(x):
            self.login(email, password)

    def validate_input_error_messages(self, login_input_error_msg, password_input_error_msg):
        time.sleep(1)
        # print(f"\n Login error:", self.browser.find_element(*LoginPageLocators.USERNAME_INPUT_ERROR_MSG).text)
        # print(f"\n Password error:", self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_ERROR_MSG).text)
        return ((hp.check_if_contains_all(login_input_error_msg, self.browser.find_element(*LoginPageLocators.USERNAME_INPUT_ERROR_MSG).text))
            and (hp.check_if_contains_all(password_input_error_msg, self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_ERROR_MSG).text)))

    def validate_popup_error_message(self, popup_error_msg):
        time.sleep(1)
        # print(f"\n Popup error:", self.browser.find_element(*LoginPageLocators.POPUP_ERROR_MSG).text)
        return hp.check_if_contains_all(popup_error_msg, self.browser.find_element(*LoginPageLocators.POPUP_ERROR_MSG).text)







