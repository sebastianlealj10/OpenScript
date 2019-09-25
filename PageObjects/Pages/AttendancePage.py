from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils import get_description


class AttendanceForm(object):

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, number, description):
        self.fill_open_forum_name("Attendance" + str(number))
        self.fill_description(description)
        self.show_description()
        self.save_and_return()

    def fill_open_forum_name(self, name):
        element = WebDriverWait(self.driver, 10). \
            until(EC.element_to_be_clickable(PageLocators.ATTENDANCE_NAME))
        element.clear()
        element.send_keys(name)

    def save_and_return(self):
        element = WebDriverWait(self.driver, 10). \
            until(EC.element_to_be_clickable(PageLocators.SAFE_AND_RETURN_TO_COURSE))
        element.click()

    def fill_description(self, description):
        element = WebDriverWait(self.driver, 10). \
            until(EC.visibility_of_element_located(PageLocators.DESCRIPTION_EDITOR))
        element.clear()
        element.send_keys(description)

    def show_description(self):
        element = WebDriverWait(self.driver, 10). \
            until(EC.element_to_be_clickable(PageLocators.SHOW_DESCRIPTION_CHECK))
        element.click()


class PageLocators(object):
    ATTENDANCE_NAME = (By.CSS_SELECTOR, 'input[id="id_name"]')
    SAFE_AND_RETURN_TO_COURSE = (By.ID, 'id_submitbutton2')
    DESCRIPTION_EDITOR = (By.ID, 'id_introeditoreditable')
    SHOW_DESCRIPTION_CHECK = (By.ID, 'id_showdescription')
