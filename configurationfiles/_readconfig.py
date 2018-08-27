from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml
class ReadPageElement:
    def page_element_from_config(self, pageName, pageElementKey, byType):
        self.byType = byType
        testURL = "https://letskodeit.teachable.com/"
        file = open('page_elements.yml', 'r')
        config = yaml.load(file)

        element = config[pageName][pageElementKey][byType]
        file.close()

        driver = webdriver.Firefox()
        driver.get(testURL)
        driver.find_element(By.XPATH, element).click()


rpe = ReadPageElement()
locator = rpe.page_element_from_config("LOGINPAGE","login_link","XPATH")
print(locator)


