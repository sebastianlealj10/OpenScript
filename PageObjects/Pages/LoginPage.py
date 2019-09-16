from selenium.webdriver.common.by import By


class Login(object):

    def __init__(self, driver):
        self.driver = driver

    def login_form(self):
        element = self.driver.find_element(*PageLocators.SNAP_BUTTON)
        element.click()
        element = self.driver.find_element(*PageLocators.USERNAME)
        element.clear()
        element.send_keys("sebas.admin")
        element = self.driver.find_element(*PageLocators.PASSWORD)
        element.clear()
        element.send_keys("password")
        element = self.driver.find_element(*PageLocators.LOG_IN)
        element.click()


class PageLocators(object):
    SNAP_BUTTON = (By.CSS_SELECTOR, '.snap-login-button')
    USERNAME    = (By.ID, 'username')
    PASSWORD    = (By.ID, 'password')
    LOG_IN      = (By.CSS_SELECTOR, '.btn-block')
