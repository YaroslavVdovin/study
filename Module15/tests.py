import unittest

from peewee import *

import factories
import models
from Module16.services import add_stud, add_course, delete_stud, add_course_stud

import random

import os



class TestStud(unittest.TestCase):



    def setUp(self):
        self.conn = SqliteDatabase('database_test.sqlite')
        self.cursor = self.conn.cursor()
        models.Students._meta.database = self.conn
        models.Courses._meta.database = self.conn
        models.StudentCourses._meta.database = self.conn
        self.conn.create_tables([models.Students, models.Courses, models.StudentCourses])
        models.StudentCourses.delete().execute()
        models.Courses.delete().execute()
        models.Students.delete().execute()

    def test_stud_create(self):
        studs = factories.StudentFactory.create_batch(5)
        for stud in studs:
            add_stud(stud)
        self.assertEqual(len(studs), len(models.Students.select()))

    def test_course_create(self):
        courses = factories.CourseFactory.create_batch(5)
        for course in courses:
            add_course(course)

        self.assertEqual(len(courses), len(models.Courses.select()))

    def test_stud_delete1(self):
        studs = factories.StudentFactory.create_batch(5)
        for stud in studs:
            add_stud(stud)

        courses = factories.CourseFactory.create_batch(5)
        for course in courses:
            add_course(course)

        stud_to_remove = models.Students.get(models.Students.id == random.randint(1,5))
        courses_to_remove = models.StudentCourses.select().where(models.StudentCourses.student_id == stud_to_remove.id)
        delete_stud(stud_to_remove, courses_to_remove)
        self.assertFalse(models.Students.select().where(models.Students.id == stud_to_remove.id).exists() and models.StudentCourses.select().where(models.StudentCourses.student_id == stud_to_remove.id).exists())

    def test_stud_delete2(self):
        studs = factories.StudentFactory.create_batch(5)
        for stud in studs:
            add_stud(stud)

        courses = factories.CourseFactory.create_batch(5)
        for course in courses:
            add_course(course)

        stud_to_remove = models.Students.get(models.Students.id == random.randint(1, 5))
        course_to_remove = models.Courses.select().order_by(fn.Random()).first()
        add_course_stud(stud_to_remove, course_to_remove)
        courses_to_remove = models.StudentCourses.select().where(models.StudentCourses.student_id == stud_to_remove.id)
        delete_stud(stud_to_remove, courses_to_remove)
        self.assertFalse(models.Students.select().where(
            models.Students.id == stud_to_remove.id).exists() and models.StudentCourses.select().where(
            models.StudentCourses.student_id == stud_to_remove.id).exists())

    def test_stud_plus_course(self):
        studs = factories.StudentFactory.create_batch(5)
        for stud in studs:
            add_stud(stud)

        courses = factories.CourseFactory.create_batch(5)
        for course in courses:
            add_course(course)

        student_to_add = models.Students.select().order_by(fn.Random()).first()
        course_to_add = models.Courses.select().order_by(fn.Random()).first()
        add_course_stud(student_to_add, course_to_add)
        self.assertTrue(models.StudentCourses.select().where(models.StudentCourses.student_id == student_to_add.id and models.StudentCourses.course_id == course_to_add.id).exists())

    def tearDown(self):
        self.conn.close()

if __name__ == '__main__':
    unittest.main()