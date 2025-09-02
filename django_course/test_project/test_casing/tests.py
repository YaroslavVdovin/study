from django.test import TestCase
from .factories import StudentFactory, CourseFactory
from .models import Students, Courses, SubCourses
import random


class TestCasesEducation(TestCase):

    def setUp(self):
        courses = CourseFactory.create_batch(5)
        studs = StudentFactory.create_batch(20)


    def test_blank_studs(self):
        """
        Case: Студенты созданы. Связей нет
        Expected: Создан батч студентов. Курсов у них нет и это ОК
        """
        students = Students.objects.all()
        for stud in students:
            self.assertFalse(stud.courses.exists())
            print(f" {stud.name} has {stud.courses.count()} course(s) assigned")

    def test_add_single_course(self):
        """
        Case: Добавляем каждому курс
        Expected: У каждого студента есть по курсу
        """
        students = Students.objects.all()
        courses = Courses.objects.all()
        for stud in students:
            stud.courses.add(random.choice(courses))
            self.assertTrue(stud.courses.exists())
            print(f"{stud.name} has {stud.courses.count()} course(s) assigned")

    def test_delete_all_courses(self):
        """
        Case: Удаляем у каждого все курсы
        Expected: У каждого студента удалены все курсы
        """
        students = Students.objects.all()
        courses = Courses.objects.all()
        for stud in students:
            for course in courses:
                stud.courses.add(course)
            stud.courses.clear()
            self.assertFalse(stud.courses.exists())
            print(f"{stud.name} has {stud.courses.count()} course(s) assigned")

    def test_delete_random_course(self):
        """
        Case: Удаляем у каждого по одному случайному курсу
        Expected: У каждого студента на один курс меньше чем было
        """
        students = Students.objects.all()
        courses = Courses.objects.all()
        for stud in students:
            for course in courses:
                stud.courses.add(course)
            courses_before = stud.courses.count()
            print(f"{stud.name} has {courses_before} course(s) assigned")
            stud.courses.remove(random.choice(courses))
            courses_after = stud.courses.count()
            print(f"Random course deleted. {stud.name} has {courses_after} course(s) left")
            self.assertTrue(courses_before-courses_after, 1)

    def test_delete_all_courses_mother_table(self):
        """
        Case: Удаляем все курсы из таблицы
        Expected: У каждого студента вообще нет курсов. Т.к. связанные записи удалены
        """
        students = Students.objects.all()
        courses = Courses.objects.all()
        for stud in students:
            stud.courses.add(random.choice(courses))
            self.assertTrue(stud.courses.count())
            print(f"{stud.name} has {stud.courses.count()} course(s) assigned")
        for course in courses:
            course.delete()
        for stud in students:
            self.assertFalse(stud.courses.count())
            print(f"{stud.name} has {stud.courses.count()} course(s) assigned")



class TestCasesFixtures(TestCase):
    """
    Case: Тест с фикстурами
    Expected: Фикстуры удачно подгружены. Связи созданы
    """
    fixtures = ['fixture.json', 'fixtures_Courses.json']
    def test_fixture_upload_with_fk(self):
        for course in SubCourses.objects.all():
            print(f"{course.name} is child course to {course.parent_course.name}")


# Create your tests here.
