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






