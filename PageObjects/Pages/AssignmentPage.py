from selenium.webdriver.common.by import By


class AssignmentForm(object):

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self):
        element = self.driver.find_element(*PageLocators.ASSIGNMENT_NAME)
        element.sendkeys("Assignment1")


class PageLocators(object):
    ASSIGNMENT_NAME = (By.ID, 'id_name')
