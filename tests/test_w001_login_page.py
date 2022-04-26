from pages.login_page import LoginPage
from pages.home_page import HomePage

import helpers as hp
import json

from tests import USERNAME, PASSWORD

with open('../tests_data/test_data_w001_login_page.json') as test_data_file:
    tdf = json.load(test_data_file)


def test_login_page(browser):

    login_page = LoginPage(browser)
    login_page.load()                                       # GIVEN BHRUT web application is connected AND the Login Page is displayed

    print(f"\n\nAW001_001 Check Login Page content")
    assert login_page.check_if_contains_all_elements()      # THEN Login Page contains all needed elements

    print(f"AW001_002 Login attempt with no data")
    login_page.login('', '')                                                                                                        # WHEN the user leaves 'Username' and 'Password' fields blank and clicks 'Login' button
    assert login_page.validate_input_error_messages(tdf['empty_username_field_error_msg'], tdf['empty_password_field_error_msg'])   # THEN an error message is being presented

    # """AW001_003 Login attempt with too short data ---> NOT DEPLOYED TO ENV"""
    # login_page.login(hp.generate_random_email(1), hp.generate_random_password(1))                                                 # WHEN the user types in 'Username' longer than 100  and 'Password' longer than 30 and clicks 'Login' button
    # assert login_page.validate_input_error_messages(tdf['too_short_username_error_msg'], tdf['too_short_password_error_msg'])     # THEN an error message is being presented

    print(f"AW001_004 Login attempt with too long data")
    login_page.login(hp.generate_random_email(tdf['username_max_length']+1), hp.generate_random_password(tdf['password_max_length']+1))     # WHEN the user types in 'Username' longer than 100  and 'Password' longer than 30 and clicks 'Login' button
    assert login_page.validate_input_error_messages(tdf['too_long_username_error_msg'], tdf['too_long_password_error_msg'])                 # THEN an error message is being presented

    print(f"AW001_005 Login attempt with min length of data")
    login_page.login(hp.generate_random_email(tdf['username_min_length']), hp.generate_random_password(tdf['password_min_length']))     # WHEN the user types in random 'Username' and random 'Password' with minimum accepted length and clicks 'Login' button
    assert login_page.validate_popup_error_message(tdf['non_existing_data_popup_error_msg'])                                            # THEN a popup error message is being presented

    print(f"AW001_006 Login attempt with max length of data")
    login_page.login(hp.generate_random_email(tdf['username_max_length']), hp.generate_random_password(tdf['password_max_length']))     # WHEN the user types in random 'Username' and random 'Password' with maximum accepted length and clicks 'Login' button
    assert login_page.validate_popup_error_message(tdf['non_existing_data_popup_error_msg'])                                            # THEN a popup error message is being presented

    # """AW001_007 Check invalid login attempts limit ---> NOT DEPLOYED TO ENV"""
    # login_page.login_x_times(hp.generate_random_email(tdf['username_min_length']), hp.generate_random_password(tdf['username_min_length']), tdf['invalid_login_limit_attempts'])  # WHEN the user types in random valid 'Username' and random 'Password' and clicks 'Login' button to reach 'login limit attempts'
    # assert login_page.validate_popup_error_message(tdf['invalid_login_limit_popup_error_msg'])                                                                                    # THEN a popup error message is being presented

    print(f"AW001_008 Login to BHR app with success")
    login_page.login(USERNAME, PASSWORD)                    # WHEN the user types in proper 'Username' and 'Password' and clicks 'Login' button
    assert HomePage(browser).is_welcome_screen_visible()    # THEN the Welcome Screen is displayed



