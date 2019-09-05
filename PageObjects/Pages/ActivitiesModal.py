from selenium.webdriver.common.by import By


class ActivityModal(object):

    def __init__(self, driver):
        self.driver = driver

    def choose_activity(self):
        element = self.driver.find_element(*PageLocators.ASSIGNMENT)
        element


class PageLocators(object):
    ASSIGNMENT = (By.CSS_SELECTOR, '.snap-modchooser-addlink:first-child')
