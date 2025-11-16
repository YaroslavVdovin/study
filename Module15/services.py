import models

def add_stud(student):
    new_stud = models.Students.create(**student.__dict__)
    new_stud.save()

def add_course(course):
    new_course = models.Courses.create(**course.__dict__)
    new_course.save()

def delete_stud(student,courses):
    if courses != []:
        for course in courses:
            course.delete_instance()
    student.delete_instance()
def add_course_stud(student, course):
    course_addition = models.StudentCourses.create(student_id = student.id, course_id = course.id)