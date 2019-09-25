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
        self.resources_tab()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PageLocators.LABEL))
        element.click()

    def create_open_forum(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PageLocators.OPEN_FORUM))
        element.click()

    def create_quiz(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PageLocators.QUIZ))
        element.click()

    def create_attendance(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PageLocators.QUIZ))
        element.click()

    def resources_tab(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PageLocators.RESOURCES_TAB))
        element.click()


class PageLocators(object):
    ASSIGNMENT = (By.CSS_SELECTOR, 'img[src*="assign"][role="presentation"]')
    RESOURCES_TAB = (By.ID, 'resources-tab')
    LABEL = (By.CSS_SELECTOR, 'img[src*="label"][role="presentation"]')
    OPEN_FORUM = (By.CSS_SELECTOR, 'img[src*="hsuforum"][role="presentation"]')
    QUIZ = (By.CSS_SELECTOR, 'img[src*="quiz"][role="presentation"]')
    ATTENDANCE = (By.CSS_SELECTOR, 'img[src*="attendance"][role="presentation"]')
