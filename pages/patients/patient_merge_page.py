from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PatientMergePage:

    # URL = 'https://ris-bhr-test.aptvision.com/patient/patient_merge/31028fe6201e002f8b31a8f3c9ac0732'
    # WELCOME_TEXT = (By.__text_signature__, 'Welcome!')
    MAIN_BODY = (By.ID, 'home-home-app1')
    SEARCH_INPUT = (By.ID, 'txt-aptsearch')

    def __init__(self, browser):
        self.browser = browser

    def is_patient_merge_page_visible(self):
        return self.browser.find_element(*self.MAIN_BODY)
