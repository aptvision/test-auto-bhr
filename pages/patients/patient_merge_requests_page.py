from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PatientMergeRequestPage:

    # URL = 'https://ris-bhr-test.aptvision.com/patient/patient_merge_requests/5fa6563171e4904a43503c490bb98f5e'
    # WELCOME_TEXT = (By.__text_signature__, 'Welcome!')
    MAIN_BODY = (By.ID, 'home-home-app1')
    SEARCH_INPUT = (By.ID, 'txt-aptsearch')

    def __init__(self, browser):
        self.browser = browser

    def is_patient_merge_request_page_visible(self):
        return self.browser.find_element(*self.MAIN_BODY)
