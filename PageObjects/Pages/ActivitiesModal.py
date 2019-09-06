from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ActivityModal(object):

    def __init__(self, driver):
        self.driver = driver

    def choose_activity(self):
        element = self.driver.find_element(*PageLocators.ASSIGNMENT)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PageLocators.ASSIGNMENT))
        element.click()


class PageLocators(object):

    ASSIGNMENT = (By.CSS_SELECTOR, '.snap-modchooser-addlink:first-child')
