from pages.xpath_locators import HomePageLocators

import time


class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def is_welcome_screen_visible(self):
        time.sleep(1)
        return self.browser.find_element(*HomePageLocators.MAIN_BODY), \
               self.browser.find_element(*HomePageLocators.WELCOME_MESSAGE_BOX)

    def check_if_contains_all_elements(self):
        time.sleep(1)
        return self.is_welcome_screen_visible(), \
               self.browser.find_element(*HomePageLocators.SEARCH_INPUT)

    def is_search_input_visible(self):
        return self.browser.find_element(*HomePageLocators.SEARCH_INPUT)

    def is_home_page_visible(self):
        return True
