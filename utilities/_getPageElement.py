"""
This class is used to get a page element that is stored in the page_elements.yml config file


"""
import yaml
from selenium.webdriver.common.by import By


class GetPageElement():


    def get_page_element_locator(self, pageName, pageElementKey, byType):
        file = open('C:\\Users\\sunda\\PycharmProjects\\AutomationFramework\\configurationfiles\\page_elements.yml', 'r')
        config = yaml.load(file)

        elementlocator = config[pageName][pageElementKey][byType]
        file.close()
        return elementlocator

    def get_page_element(self, driver, pageName, pageElementKey, byType):
        #self.driver = driver
        #elementLocator = self.get_page_element_locator(pageName, pageElementKey, byType)
        file = open('C:\\Users\\sunda\\PycharmProjects\\AutomationFramework\\configurationfiles\\page_elements.yml',
                    'r')
        config = yaml.load(file)

        elementLocator = config[pageName][pageElementKey][byType]
        file.close()
        try:
            driver.find_element(By.byType, elementLocator).click()
            # login_link = self.driver.find_element(By.XPATH, "//a[contains(@class,'navbar-link') and contains(text(),'Login')]")
        except:
            print('Exception happened')
                #Logging exception into log file

gpe = GetPageElement()
print(gpe.get_page_element_locator("LOGINPAGE", "login_link", "XPATH"))

