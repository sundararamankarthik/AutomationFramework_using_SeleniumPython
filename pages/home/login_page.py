from selenium.webdriver.common.by import By
import time
class LoginPage():

    def __init__(self, driver):
        self.driver = driver


    def login(self, username, password):

        login_link = self.driver.find_element(By.XPATH, "//a[contains(@class,'navbar-link') and contains(text(),'Login')]")
        login_link.click()
        time.sleep(3)
        username_textbox = self.driver.find_element(By.ID, "user_email")
        username_textbox.send_keys(username)

        password_textbox = self.driver.find_element(By.ID, "user_password")
        password_textbox.send_keys(password)

        submit_button = self.driver.find_element(By.XPATH, "//input[@name='commit']")
        submit_button.click()
        return self.driver

    def logout(self, username, password):
        self.my_driver = self.login(username, password)
        # Wait for application to login
        time.sleep(5)
        # Do logout
        profile_image = self.my_driver.find_element_by_xpath("//img[@class='gravatar' and @alt='test@email.com']")
        profile_image.click()
        signout_link = self.my_driver.find_element_by_xpath("//li[@class='user-signout']")
        signout_link.click()

        # Verify if login page is seen
        element = self.my_driver.find_element_by_xpath(
            "//a[contains(@class,'navbar-link') and contains(text(),'Login')]")
        return element






