from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Login(object):

    def __init__(self, driver):
        self.driver = driver

    def login_form(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PageLocators.SNAP_BUTTON))
        element.click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PageLocators.USERNAME))
        element.clear()
        element.send_keys("sebas.admin")
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PageLocators.PASSWORD))
        element.clear()
        element.send_keys("password")
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PageLocators.LOG_IN))
        element.click()


class PageLocators(object):
    SNAP_BUTTON = (By.CSS_SELECTOR, '.snap-login-button')
    USERNAME    = (By.ID, 'username')
    PASSWORD    = (By.ID, 'password')
    LOG_IN      = (By.CSS_SELECTOR, '.btn-block')
