from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PatientExternalMergeRequestPage:

    # URL = 'https://ris-bhr-test.aptvision.com/admin/merge_request/8716050c75638c883fbd1abc4b5d9079'
    # WELCOME_TEXT = (By.__text_signature__, 'Welcome!')
    MAIN_BODY = (By.ID, 'home-home-app1')
    SEARCH_INPUT = (By.ID, 'txt-aptsearch')

    def __init__(self, browser):
        self.browser = browser

    def is_patient_external_merge_request_page_visible(self):
        return self.browser.find_element(*self.MAIN_BODY)
