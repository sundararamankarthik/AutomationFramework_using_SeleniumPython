
from base.pagebase import PageBase
import time


class LoginPage(PageBase):

    def __init__(self, driver):
        self.driver = driver


    def login(self, username, password):
        login_link = self.get_page_element(self.driver, "LOGINPAGE", "login_link", "XPATH")
        print("Success!!")
        time.sleep(3)
        login_link.click()

        time.sleep(5)
        username_textbox = self.get_page_element(self.driver, "LOGINPAGE", "username_textbox", "ID")
        username_textbox.send_keys(username)

        password_textbox = self.get_page_element(self.driver, "LOGINPAGE", "password_textbox", "ID")
        password_textbox.send_keys(password)

        submit_button = self.get_page_element(self.driver, "LOGINPAGE", "submit_button", "XPATH")
        submit_button.click()

        return self.driver

    def logout(self, username, password):
        self.my_driver = self.login(username, password)
        # Wait for application to login
        time.sleep(5)
        # Do logout
        profile_image = self.get_page_element(self.my_driver, "HOMEPAGE", "profile_image", "XPATH")
        profile_image.click()


        signout_link = self.get_page_element(self.my_driver, "HOMEPAGE", "signout_link", "XPATH")
        signout_link.click()

        # Verify if login page is seen
        login_link = self.get_page_element(self.my_driver, "LOGINPAGE", "login_link", "XPATH")
        return login_link




