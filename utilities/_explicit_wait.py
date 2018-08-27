from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium.common.exceptions as excp
from utilities._getPageElement import GetPageElement as getElement

class ExplicitWait():

    def explicitly_wait(self, driver, pageName, pageElementKey, byType):
        #Explicit Wait implementation
        self.driver = driver
        wait = WebDriverWait(self.driver, 4, 1, ignored_exceptions=
                      [excp.ElementNotSelectableException,
                       excp.ElementNotInteractableException,
                       excp.ElementNotSelectableException])



        try:
           element = wait.until(EC.presence_of_element_located(
               (By.byType, getElement.get_page_element_locator(self, pageName, pageElementKey, byType)))
           )

        except:
            raise
            #log exception
        finally:
            return element
















        wait = WebDriverWait(self.driver, 10, poll_frequency=1,ignored_exceptions=
                                                [ElementNotVisibleException,
                                                 ElementNotSelectableException,
                                                NoSuchElementException])


        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'navbar-link') and contains(text(),'Login')]")))

        #Validate Login
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt = 'test@email.com']")))
        element.click()