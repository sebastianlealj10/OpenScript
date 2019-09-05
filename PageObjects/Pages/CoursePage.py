from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Course(object):

    def __init__(self, driver):
        self.driver = driver

    def change_cover(self):
        element = self.driver.find_element(*PageLocators.CHANGE_COVER_IMAGE)
        element.send_keys('/home/sebas/Documents/cover.jpg')
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PageLocators.SAVE_BUTTON))
        element.click()
        WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(PageLocators.ALERT_IMAGE)))

    def create_activity(self):
        element = self.driver.find_element(*PageLocators.CREATE_ACTIVITY)
        element.click()


class PageLocators(object):
    CHANGE_COVER_IMAGE = (By.ID, 'snap-coverfiles')
    SAVE_BUTTON = (By.CSS_SELECTOR, '.btn-success')
    ALERT_IMAGE = (By.ID, 'snap-alert-cover-image-size')
    CREATE_ACTIVITY = (By.CSS_SELECTOR, 'a[data-target="#snap-modchooser-modal"]')
