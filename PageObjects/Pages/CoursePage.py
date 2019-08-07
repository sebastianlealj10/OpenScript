from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Course(object):

    def __init__(self, driver):
        self.driver = driver

    def change_cover(self):
        element = self.driver.find_element(*CoursePageLocators.CHANGE_COVER_IMAGE)
        element.send_keys('/home/sebas/Documents/cover.jpg')
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((CoursePageLocators.SAVE_BUTTON)))
        element.click()
        WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(CoursePageLocators.ALERT_IMAGE)))


class CoursePageLocators(object):
    CHANGE_COVER_IMAGE = (By.ID, 'snap-coverfiles')
    SAVE_BUTTON = (By.CSS_SELECTOR, '.btn-success')
    ALERT_IMAGE = (By.ID, 'snap-alert-cover-image-size')
