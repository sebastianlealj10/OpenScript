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
from AssignmentPage import AssignmentForm


class GenerateActivities:
    Number_of_activities = 2

    def __init__(self):
        self.driver = webdriver.Firefox()

    def setup(self, url):
        # create a new Firefox session
        self.driver.implicitly_wait(30)
        self.driver.get(url)

    def teardown(self):
        # close the browser window
        self.driver.quit()

    def covers(self, url):
        login_page = Login(self.driver)
        login_page.login_form()
        self.driver.get(url)
        try:
            Course(self.driver).change_cover()
        except Exception as e:
            print(url + "failed".format(e))
            pass

    def assignments(self, url):
        number_of_activities = self.Number_of_activities
        self.driver.get(url)
        try:
            for y in range(0, number_of_activities):
                Course(self.driver).create_activity()
                ActivityModal(self.driver).choose_activity()
                AssignmentForm(self.driver).fill_form(y)
        except Exception as e:
            print(url + "failed".format(e))
            pass


if __name__ == "__main__":
    navigate = GenerateActivities()
    navigate.setup('https://snap2perf-sandbox.mrooms.net/course/view.php?id=20')
    navigate.covers('https://snap2perf-sandbox.mrooms.net/course/view.php?id=20')
    navigate.assignments('https://snap2perf-sandbox.mrooms.net/course/view.php?id=20')
