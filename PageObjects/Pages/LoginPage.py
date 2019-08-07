from selenium.webdriver.common.by import By


class Login(object):

    def __init__(self, driver):
        self.driver = driver

    def login_form(self):
        element = self.driver.find_element(*LoginPageLocators.USERNAME)
        element.clear()
        element.send_keys("sebas.admin")
        element = self.driver.find_element(*LoginPageLocators.PASSWORD)
        element.clear()
        element.send_keys("password")
        element = self.driver.find_element(*LoginPageLocators.LOG_IN)
        element.click()


class LoginPageLocators(object):
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOG_IN   = (By.ID, 'loginbtn')
