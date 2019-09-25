from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AssignmentForm(object):

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, number):
        self.fill_assignment_name("Assingment"+str(number))
        self.due_date_disable()
        self.save_and_return()

    def fill_assignment_name(self, name):
        element = WebDriverWait(self.driver, 10).\
            until(EC.element_to_be_clickable(PageLocators.ASSIGNMENT_NAME))
        element.clear()
        element.send_keys(name)

    def due_date_disable(self):
        element = WebDriverWait(self.driver, 10).\
            until(EC.element_to_be_clickable(PageLocators.DISABLE_DUE_DATE))
        element.click()

    def save_and_return(self):
        element = WebDriverWait(self.driver, 10).\
            until(EC.element_to_be_clickable(PageLocators.SAFE_AND_RETURN_TO_COURSE))
        element.click()

    def fill_description(self):
        element = self.driver.find_element(*PageLocators.DESCRIPTION_EDITOR)
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PageLocators.SAVE_BUTTON))


class PageLocators(object):
    ASSIGNMENT_NAME = (By.CSS_SELECTOR, 'input[id="id_name"]')
    DISABLE_DUE_DATE = (By.ID, 'id_duedate_enabled')
    SAFE_AND_RETURN_TO_COURSE = (By.ID, 'id_submitbutton2')
    DESCRIPTION_EDITOR = (By.ID, 'id_introeditoreditable')
