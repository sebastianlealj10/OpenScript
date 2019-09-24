import sys

from selenium import webdriver

sys.path.extend(['/home/sebas/PycharmProjects/OpenScript', '/home/sebas/PycharmProjects/OpenScript/.idea',
                 '/home/sebas/PycharmProjects/OpenScript/.idea/inspectionProfiles',
                 '/home/sebas/PycharmProjects/OpenScript/PageObjects',
                 '/home/sebas/PycharmProjects/OpenScript/PageObjects/Pages'])

from LoginPage import Login
from CoursePage import Course
from ActivitiesModal import ActivityModal
from AssignmentPage import AssignmentForm
from LabelPage import LabelForm
from Dictionary import Courses


class GenerateActivities:

    def __init__(self):
        self.driver = webdriver.Firefox()

    def setup(self, url):
        # create a new Firefox session
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
        Course(self.driver).get_course(url, section)
        try:
            for i in range(0, number):
                Course(self.driver).create_activity(section)
                ActivityModal(self.driver).create_assignment()
                AssignmentForm(self.driver).fill_form(i + 1)
        except Exception as e:
            print(e)
            pass

    def labels(self, url, section, number):
        Course(self.driver).get_course(url, section)
        try:
            for _ in range(0, number):
                print(url)
                Course(self.driver).create_activity(section)
                ActivityModal(self.driver).create_label()
                LabelForm(self.driver).create_label_image()
        except Exception as e:
            print(url + ": " + str(e))
            pass


if __name__ == "__main__":

    navigate = GenerateActivities()
    navigate.setup('https://snap2perf-sandbox.mrooms.net')
    for i, j in Courses.items():
        covers = int(''.join(Courses[i]["cover"]))
        if covers > 0:
            navigate.covers(i)
        for x, y in Courses[i]["Section"].items():
            assignments = int(''.join(Courses[i]["Section"][x]["Actions"]["assignment"]))
            if assignments > 0:
                navigate.assignments(i, x, assignments)
            labels = int(''.join(Courses[i]["Section"][x]["Actions"]["label"]))
            if labels > 0:
                navigate.labels(i, x, labels)

    # navigate.teardown()
