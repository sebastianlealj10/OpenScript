from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Course(object):

    def __init__(self, driver):
        self.driver = driver

    def get_course(self, url, section):
        self.driver.get(url + '#section-' + str(section))
        self.load_toc()

    def change_cover(self):
        element = self.driver.find_element(*PageLocators.CHANGE_COVER_IMAGE)
        element.send_keys('/home/sebas/Documents/cover.jpg')
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PageLocators.SAVE_BUTTON))
        element.click()
        WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(PageLocators.ALERT_IMAGE)))

    def create_activity(self, section):
        print(section)
        element = self.driver.find_element_by_css_selector \
            ('a[data-target="#snap-modchooser-modal"][data-section="' + section + '"]')
        element.click()

    def load_toc(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PageLocators.LOAD_TOC))


class PageLocators(object):
    CHANGE_COVER_IMAGE = (By.ID, 'snap-coverfiles')
    SAVE_BUTTON = (By.CSS_SELECTOR, '.btn-success')
    ALERT_IMAGE = (By.ID, 'snap-alert-cover-image-size')
    CREATE_ACTIVITY_SECTION0 = (By.CSS_SELECTOR, 'a[data-target="#snap-modchooser-modal"][data-section="0"]')
    CREATE_ACTIVITY_SECTION1 = (By.CSS_SELECTOR, 'a[data-target="#snap-modchooser-modal"][data-section="1"]')
    LOAD_TOC = (By.ID, 'course-toc')
