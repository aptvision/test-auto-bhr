import pytest
import selenium.webdriver

from tests import PROJECT_PATH, CHROME_WEBDRIVER_PATH
import helpers as hp


@pytest.fixture()
def browser():
    b = selenium.webdriver.Chrome(executable_path=str(PROJECT_PATH + CHROME_WEBDRIVER_PATH))
    b.implicitly_wait(10)
    b.maximize_window()
    yield b
    b.save_screenshot(str(PROJECT_PATH + "\\output\\output_" + hp.set_datetime_stamp() + ".png"))
    b.quit()