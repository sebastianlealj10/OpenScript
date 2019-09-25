import sys
import time

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
from OpenforumPage import OpenforumForm
from QuizPage import QuizForm
from AttendancePage import AttendanceForm
from Dictionary import Courses
from utils import get_description
from datetime import datetime


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

    def get_course(self, course_url, section):
        try:
            Course(self.driver).get_course(course_url, section)
            print(course_url + " : " + section)
        except Exception as e:
            print(course_url + ": " + str(e))
            pass

    def assignments(self, section, number, text):
        try:
            for i in range(0, number):
                Course(self.driver).create_activity(section)
                ActivityModal(self.driver).create_assignment()
                AssignmentForm(self.driver).fill_form(i + 1, text)
                print("assignment: " + str(i + 1))
        except Exception as e:
            print(e)
            pass

    def labels(self, section, number):
        try:
            for i in range(0, number):
                Course(self.driver).create_activity(section)
                ActivityModal(self.driver).create_label()
                LabelForm(self.driver).create_label_image()
                print("label: " + str(i + 1))
        except Exception as e:
            print("label failed")
            print(e)
            pass

    def open_forum(self, section, number, text):
        try:
            for i in range(0, number):
                Course(self.driver).create_activity(section)
                ActivityModal(self.driver).create_open_forum()
                OpenforumForm(self.driver).fill_form(i + 1, text)
                print("open forum: " + str(i + 1))
        except Exception as e:
            print(e)
            pass

    def quiz(self, section, number, text):
        try:
            for i in range(0, number):
                Course(self.driver).create_activity(section)
                ActivityModal(self.driver).create_quiz()
                QuizForm(self.driver).fill_form(i + 1, text)
                print("quiz: " + str(i + 1))
        except Exception as e:
            print(e)
            pass

    def attendance(self, section, number, text):
        try:
            for i in range(0, number):
                Course(self.driver).create_activity(section)
                ActivityModal(self.driver).create_attendance()
                AttendanceForm(self.driver).fill_form(i + 1, text)
                print("quiz: " + str(i + 1))
        except Exception as e:
            print(e)
            pass


if __name__ == "__main__":
    start = datetime.now()
    print("start =", start)
    description = get_description()
    navigate = GenerateActivities()
    navigate.setup('https://snap2perf-sandbox.mrooms.net')
    for url, j in Courses.items():
        covers = int(''.join(Courses[url]["cover"]))
        if covers > 0:
            navigate.covers(url)
        for x, y in Courses[url]["Section"].items():
            navigate.get_course(url, x)
            assignments = int(''.join(Courses[url]["Section"][x]["Actions"]["assignment"]))
            labels = int(''.join(Courses[url]["Section"][x]["Actions"]["label"]))
            open_forum = int(''.join(Courses[url]["Section"][x]["Actions"]["open_forum"]))
            quiz = int(''.join(Courses[url]["Section"][x]["Actions"]["quiz"]))
            attendance = int(''.join(Courses[url]["Section"][x]["Actions"]["attendance"]))
            if assignments > 0:
                navigate.assignments(x, assignments, description)
            if labels > 0:
                navigate.labels(x, labels)
            if open_forum > 0:
                navigate.open_forum(x, open_forum, description)
            if quiz > 0:
                navigate.quiz(x, quiz, description)
            if attendance > 0:
                navigate.attendance(x, attendance, description)

    end = datetime.now()
    print("end =", end)
    navigate.teardown()
