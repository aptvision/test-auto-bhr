from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PatientsPage:

    # URL = 'https://ris-bhr-test.aptvision.com/home/patient/d50d80c5b86d66c664a5d988a7b2529f'
    # WELCOME_TEXT = (By.__text_signature__, 'Welcome!')
    MAIN_BODY = (By.ID, 'home-home-app1')
    SEARCH_INPUT = (By.ID, 'txt-aptsearch')

    def __init__(self, browser):
        self.browser = browser

    def is_patients_page_visible(self):
        return self.browser.find_element(*self.MAIN_BODY)
