from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LabelForm(object):

    def __init__(self, driver):
        self.driver = driver

    def create_label_image(self):
        self.upload_image()
        self.browse_repositories()
        self.choose_file()
        self.upload_file()
        self.overwrite_file()
        self.remove_description()
        self.save_image()
        self.save_and_return()

    def upload_image(self):
        element = WebDriverWait(self.driver, 10). \
            until(EC.element_to_be_clickable(PageLocators.ATTO_IMAGE_BUTTON))
        element.click()

    def browse_repositories(self):
        element = WebDriverWait(self.driver, 10). \
            until(EC.element_to_be_clickable(PageLocators.BROWSE_REPOSITORIES_BUTTON))
        element.click()

    def choose_file(self):
        element = WebDriverWait(self.driver, 10). \
            until(EC.element_to_be_clickable(PageLocators.CHOOSE_FILE_BUTTON))
        element.clear()
        element.send_keys('/Users/jleal/Documents/image.jpg')

    def upload_file(self):
        element = WebDriverWait(self.driver, 10). \
            until(EC.element_to_be_clickable(PageLocators.UPLOAD_THIS_FILE_BUTTON))
        element.click()

    def overwrite_file(self):
        try:
            element = WebDriverWait(self.driver, 2). \
                until(EC.element_to_be_clickable(PageLocators.OVERWRITE_BUTTON))
            element.click()
        except:
            pass

    def remove_description(self):
        element = WebDriverWait(self.driver, 10). \
            until(EC.element_to_be_clickable(PageLocators.DESCRIPTION_NOT_NECESSARY_CHECKBOX))
        element.click()

    def save_image(self):
        element = WebDriverWait(self.driver, 10). \
            until(EC.element_to_be_clickable(PageLocators.SAVE_IMAGE_BUTTON))
        element.click()

    def save_and_return(self):
        element = WebDriverWait(self.driver, 10). \
            until(EC.element_to_be_clickable(PageLocators.SAVE_AND_RETURN_BUTTON))
        element.click()


class PageLocators(object):
    ATTO_IMAGE_BUTTON = (By.CSS_SELECTOR, '.atto_image_button')
    BROWSE_REPOSITORIES_BUTTON = (By.CSS_SELECTOR, '.openimagebrowser')
    UPLOAD_THIS_FILE_BUTTON = (By.CSS_SELECTOR, '.fp-upload-btn')
    CHOOSE_FILE_BUTTON = (By.NAME, 'repo_upload_file')
    OVERWRITE_BUTTON = (By.CSS_SELECTOR, '.fp-dlg-butoverwrite')
    DESCRIPTION_NOT_NECESSARY_CHECKBOX = (By.ID, 'id_introeditor_atto_image_presentation')
    SAVE_IMAGE_BUTTON = (By.CSS_SELECTOR, '.atto_image_urlentrysubmit')
    SAVE_AND_RETURN_BUTTON = (By.ID, 'id_submitbutton2')
