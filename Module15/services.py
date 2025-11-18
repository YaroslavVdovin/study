import models
from datetime import datetime

def add_student(name, surname, age, city):
    if models.Students.select().where(models.Students.name == name,
                                         models.Students.surname == surname,
                                         models.Students.age == age,
                                         models.Students.city == city).exists():
        return print(f'Студент {name}, {surname}, {age}, {city} уже существует в базе данных')
    elif age<18 or age>60:
        return print('Недопустимый возраст студента')
    else:
        new_student = models.Students.create(name=name,
                                             surname=surname,
                                             age=age,
                                             city=city)
        return new_student


def add_course(name, time_start, time_end):
    if models.Courses.select().where(models.Courses.name == name,
                                     models.Courses.time_start == time_start,
                                     models.Courses.time_end == time_end).exists():
        return print(
            f'Курс {name}, {time_start}, {time_end} уже существует в базе данных')
    elif datetime.strptime(time_start, '%Y-%m-%d').year <= 2017:
        return print(
            f'Начало курса {name}, {time_start}, {time_end} слишком рано')
    else:
        new_course = models.Courses.create(name=name,
                                           time_start=time_start,
                                           time_end=time_end)
        return new_course


def delete_student(student):
    courses_passed = models.StudentCourses.select().where(models.StudentCourses.student_id == student.id)
    if courses_passed:
        for course in courses_passed:
            course.delete_instance()
    student.delete_instance()


def add_course_student(student, course):
    course_addition = models.StudentCourses.create(student_id=student.id, course_id=course.id)
    return course_addition
