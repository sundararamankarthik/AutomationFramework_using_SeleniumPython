#
#
#
# Run using command:
# c:\..\AutomationFramework>python -m pytest -s -v C:\Users\sunda\PycharmProjects\AutomationFramework\tests\home\test_login.py
#https://github.com/pytest-dev/pytest/issues/2287
#
#pip3 install pytest-html
#--html=htmlreport.html

from selenium import webdriver
from pages.home.login_page import LoginPage
import pytest
import time

class TestLogin():
    my_driver = None

    @pytest.fixture(scope="module")
    def set_up(self):
        print("Starting test")
        self.my_driver = None
        yield
        print("Completing test")

    def test_logout(self, set_up):
        self.my_driver = webdriver.Firefox()
        testURL = "https://letskodeit.teachable.com/"
        # screenshot_dir = "C:\\Users\\sunda\\PycharmProjects\\AutomationFramework\\screenshots\\"
        # screenshot_filename = str(round(time.time())) + ".png"
        # #Save Screenshot
        # self.my_driver.save_screenshot(screenshot_dir + screenshot_filename)
        self.my_driver.get(testURL)
        self.my_driver.maximize_window()
        lp = LoginPage(self.my_driver)
        lp.logout("test@email.com", "abcabc")









