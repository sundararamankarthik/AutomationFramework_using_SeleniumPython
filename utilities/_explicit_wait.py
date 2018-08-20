# Explicit Wait implementation
# wait = WebDriverWait(self.driver, 10, poll_frequency=1,ignored_exceptions=
#                                         [ElementNotVisibleException,
#                                          ElementNotSelectableException,
#                                         NoSuchElementException])
#
#
# element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'navbar-link') and contains(text(),'Login')]")))

# Validate Login
# element = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt = 'test@email.com']")))
# element.click()