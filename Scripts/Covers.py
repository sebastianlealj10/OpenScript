import sys
import time
import unittest

from selenium import webdriver

sys.path.extend(['/home/sebas/PycharmProjects/OpenScript', '/home/sebas/PycharmProjects/OpenScript/.idea',
                 '/home/sebas/PycharmProjects/OpenScript/.idea/inspectionProfiles',
                 '/home/sebas/PycharmProjects/OpenScript/PageObjects',
                 '/home/sebas/PycharmProjects/OpenScript/PageObjects/Pages'])

from LoginPage import Login
from CoursePage import Course


class SeleniumWrapper:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SeleniumWrapper, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def connect(self):
        self.driver = webdriver.Chrome()
        return self.driver


class TestChangeCovers(unittest.TestCase):
    Start_course = 20

    def setUp(self):
        # create a new Firefox session
        self.driver = SeleniumWrapper.connect(self)
        self.driver.implicitly_wait(30)
        self.driver.get('https://snap2perf-sandbox.mrooms.net/course/view.php?id=' + str(self.Start_course))

    def test_changeCovers(self):
        login_page = Login(self.driver)
        login_page.login_form()
        Course(self.driver).change_cover()
        course_number = self.Start_course
        for x in range(0, 300):
            self.driver.get('https://snap2perf-sandbox.mrooms.net/course/view.php?id=' + str(course_number))
            try:
                Course(self.driver).change_cover()
            except Exception as e:
                print("Course number" + str(course_number) + "failed".format(e))
                pass
            course_number += 1

    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestChangeCovers)
    # suite = unittest.TestSuite()
    # suite.addTest(ChangeCovers('changeCover'))
    unittest.TextTestRunner(verbosity=2).run(suite)
