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
from Dictionary import Courses


class GenerateActivities:
    Number_of_activities = 2

    def __init__(self):
        self.driver = webdriver.Firefox()

    def setup(self, url):
        # create a new Firefox session
        self.driver.implicitly_wait(30)
        self.driver.get(url)
        self.driver.maximize_window()
        login_page = Login(self.driver)
        login_page.login_form()

    def teardown(self):
        # close the browser window
        self.driver.quit()

    def covers(self, url):

        self.driver.get(url)
        try:
            Course(self.driver).change_cover()
        except Exception as e:
            print(url + ": " + str(e))
            pass

    def assignments(self, url, number):

        self.driver.get(url)
        try:
            for y in range(0, number):
                Course(self.driver).create_activity()
                ActivityModal(self.driver).choose_activity()
                AssignmentForm(self.driver).fill_form(number)
        except Exception as e:
            print(url + ": " + str(e))
            pass


if __name__ == "__main__":

    navigate = GenerateActivities()
    navigate.setup('https://snap2perf-sandbox.mrooms.net')
    for i, j in Courses["URL"].items():
        k = Courses["URL"][i]["Actions"]["cover"]
        l = int(''.join(k))
        m = Courses["URL"][i]["Actions"]["assignment"]
        o = int(''.join(m))
        if l > 0:
            navigate.covers(i)
        if o > 0:
            navigate.assignments(i, o)
    navigate.teardown()
