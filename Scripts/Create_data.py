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

    def __init__(self):
        self.driver = webdriver.Firefox()

    def setup(self, url):
        # create a new Firefox session
        self.driver.implicitly_wait(10)
        self.driver.get(url)
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

    def assignments(self, url, section, number):

        self.driver.get(url+'#section-' + str(section))
        try:
            for i in range(0, number):
                Course(self.driver).create_activity(section)
                ActivityModal(self.driver).create_assignment()
                AssignmentForm(self.driver).fill_form(i+1)
        except Exception as e:
            print(e)
            pass

    def labels(self, url, section, number):

        self.driver.get(url+'#section-' + str(section))
        try:
            for _ in range(0, number):
                Course(self.driver).create_activity()
                ActivityModal(self.driver).create_label()
                # AssignmentForm(self.driver).fill_form(number)
        except Exception as e:
            print(url + ": " + str(e))
            pass


if __name__ == "__main__":

    navigate = GenerateActivities()
    navigate.setup('https://snap2perf-sandbox.mrooms.net')
    for i, j in Courses.items():
        k = Courses[i]["cover"]
        k = int(''.join(k))
        if k > 0:
            navigate.covers(i)
        for x, y in Courses[i]["Section"].items():
            p = Courses[i]["Section"][x]["Actions"]["assignment"]
            p = int(''.join(p))
            if p > 0:
                navigate.assignments(i, x, p)
            q = Courses[i]["Section"][x]["Actions"]["label"]
            q = int(''.join(q))
            if q > 0:
                navigate.labels(i, x, p)

    navigate.teardown()
