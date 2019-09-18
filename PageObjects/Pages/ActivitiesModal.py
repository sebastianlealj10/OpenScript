from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ActivityModal(object):

    def __init__(self, driver):
        self.driver = driver

    def create_assignment(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PageLocators.ASSIGNMENT))
        element.click()

    def create_label(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PageLocators.RESOURCES_TAB))
        element.click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PageLocators.LABEL))
        element.click()


class PageLocators(object):
    ASSIGNMENT = (By.CSS_SELECTOR, 'img[src*="assign"][role="presentation"]')
    RESOURCES_TAB = (By.ID, 'resources-tab')
    LABEL = (By.CSS_SELECTOR, 'img[src*="label"][role="presentation"]')
