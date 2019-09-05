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
from ActivitiesModal import ActivityModal


class GenerateData(unittest.TestCase):
    Start_course = 20

    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
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

    def test_createActivities(self):
        login_page = Login(self.driver)
        login_page.login_form()
        Course(self.driver).create_activity()
        ActivityModal(self.driver).choose_activity()

    """
    def tearDown(self):
        # close the browser window
        self.driver.quit()
    """


if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(GenerateData.test_createActivities())
    suite = unittest.TestSuite()
    suite.addTest(GenerateData('test_createActivities'))
    unittest.TextTestRunner(verbosity=2).run(suite)
