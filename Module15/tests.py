import unittest
from peewee import *
import factories
import models
from Module15.services import add_student, add_course, delete_student, add_course_student
import random


class TestStud(unittest.TestCase):

    def setUp(self):
        self.conn = SqliteDatabase('database_test.sqlite')
        self.cursor = self.conn.cursor()
        self.conn.create_tables([models.Students, models.Courses, models.StudentCourses])
        factories.StudentFactory._meta.model = models.Students
        factories.CourseFactory._meta.model = models.Courses

    def test_student_create_correct(self):
        studs = factories.StudentFactory.create_batch(5)
        add_student(name='TestBoy',
                    surname='TestBoyevich',
                    age=25,
                    city='Tagil')
        self.assertEqual(len(studs) + 1, len(models.Students.select()))

    def test_student_create_incorrect(self):

        self.assertIsNone(add_student(name='TestBoy',
                                     surname='TestBoyevich',
                                     age=105,
                                     city='Tagil'))

    def test_course_create(self):
        courses = factories.CourseFactory.create_batch(5)
        add_course(name='TestCourse',
                   time_start='2025-09-12',
                   time_end='2025-10-10')
        self.assertEqual(len(courses) + 1, len(models.Courses.select()))

    def test_course_create_incorrect(self):
        self.assertIsNone(add_course(name='TestCourse',
                          time_start='2010-09-12',
                          time_end='2025-10-10'))

    def test_student_delete1(self):
        factories.StudentFactory.create_batch(5)

        student_to_remove = models.Students.get(models.Students.id == random.randint(1,5))
        delete_student(student_to_remove)
        self.assertFalse(models.Students.select().where(models.Students.id == student_to_remove.id).exists() and models.StudentCourses.select().where(models.StudentCourses.student_id == student_to_remove.id).exists())

    def test_stud_delete2(self):
        factories.StudentFactory.create_batch(5)
        factories.CourseFactory.create_batch(5)
        stud_to_remove = models.Students.get(models.Students.id == random.randint(1, 5))
        course_to_remove = models.Courses.select().order_by(fn.Random()).first()
        add_course_student(stud_to_remove, course_to_remove)

        delete_student(stud_to_remove)
        self.assertFalse(models.Students.select().where(
            models.Students.id == stud_to_remove.id).exists() and models.StudentCourses.select().where(
            models.StudentCourses.student_id == stud_to_remove.id).exists())

    def test_stud_plus_course(self):
        factories.StudentFactory.create_batch(5)
        factories.CourseFactory.create_batch(5)
        student_to_add = models.Students.select().order_by(fn.Random()).first()
        course_to_add = models.Courses.select().order_by(fn.Random()).first()
        add_course_student(student_to_add, course_to_add)
        self.assertTrue(models.StudentCourses.select().where(models.StudentCourses.student_id == student_to_add.id and models.StudentCourses.course_id == course_to_add.id).exists())

    def tearDown(self):
        self.conn.close()
        models.StudentCourses.delete().execute()
        models.Courses.delete().execute()
        models.Students.delete().execute()


if __name__ == '__main__':
    unittest.main()
