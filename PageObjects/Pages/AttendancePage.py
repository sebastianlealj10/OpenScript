from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AttendanceForm(object):

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, number):
        self.fill_open_forum_name("Attendance" + str(number))
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


class PageLocators(object):
    ATTENDANCE_NAME = (By.CSS_SELECTOR, 'input[id="id_name"]')
    SAFE_AND_RETURN_TO_COURSE = (By.ID, 'id_submitbutton2')
