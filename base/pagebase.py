"""
Page base class
"""

import yaml
from selenium.webdriver.common.by import By


class PageBase():


    def get_page_element_locator(self, pageName, pageElementKey, byType):
        file = open('C:\\Users\\sunda\\PycharmProjects\\AutomationFramework\\configurationfiles\\page_elements.yml', 'r')
        config = yaml.load(file)

        elementlocator = config[pageName][pageElementKey][byType]
        file.close()
        return elementlocator

    def get_page_element(self, driver, pageName, pageElementKey, byType):

        elementLocator = self.get_page_element_locator(pageName, pageElementKey, byType)
        try:
            if byType == "XPATH":
               return driver.find_element(By.XPATH, elementLocator)
            elif byType == "ID":
                return driver.find_element(By.ID, elementLocator)


        except:
            print('Exception happened')
                #Logging exception into log file

# gpe = PageBase()
# print(gpe.get_page_element_locator("LOGINPAGE", "login_link", "xpath"))