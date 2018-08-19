from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from pages.home.login_page import LoginPage
import unittest

class LoginTests(unittest.TestCase):


    def test_valid_login(self):

        driver = webdriver.Firefox()
        testURL = "https://letskodeit.teachable.com/"
        driver.get(testURL)
        driver.maximize_window()
        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")
        


    def test_logout(self):

        self.driver.find_element_by_xpath("//li[@class='user-signout']").click()

        # Verify if login page is seen
        element = self.driver.find_element_by_xpath("//a[contains(@class,'navbar-link') and contains(text(),'Login')]")
        if element is not None:
            print('Logout successful')
        self.driver.quit()



