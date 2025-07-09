from peewee import *

conn = SqliteDatabase('db_stud_orm.sqlite')

cursor = conn.cursor()

class BaseModel(Model):
    class Meta:
        database = conn

class StudentCourses(BaseModel):
    student_id = IntegerField(column_name='student_id')
    course_id = IntegerField(column_name='course_id')

class Courses(BaseModel):
    id = IntegerField(column_name='id')
    name = CharField(column_name='name')
    time_start = TextField(column_name='time_start')
    time_end = TextField(column_name='time_end')

class Students(BaseModel):
    id = IntegerField(column_name='id')
    name = CharField(column_name='name')
    surname = CharField(column_name='surname')
    age = IntegerField(column_name='age')
    city = CharField(column_name='city')

conn.create_tables([Students, StudentCourses, Courses])
courses_to_studs_list = [{'student_id':1,'course_id':1}, {'student_id':2,'course_id':1}, {'student_id':3,'course_id':1}, {'student_id':4,'course_id':2}]
studs_to_courses = StudentCourses.insert_many(courses_to_studs_list).execute()

course1 = Courses.create(id = 1, name = 'python', time_start = '21.07.21', time_end = '21.08.21')
course1.save()
course2 = Courses.create(id = 2, name = 'java', time_start = '13.07.21', time_end = '16.08.21')
course2.save()

student_list = [(1, 'Max', 'Brooks', 24, 'Spb'),
                (2, 'John', 'Stones', 15, 'Spb'),
                (3, 'Andy', 'Wings', 45, 'Manhester'),
                (4, 'Kate', 'Brooks', 34, 'Spb')]
student_dicts = [{'id':a, 'name':b, 'surname': c, 'age': d, 'city':e} for a, b, c, d, e in student_list]

Students.insert_many(student_dicts).execute()

#Студенты 30+
for stud in Students.select().where(Students.age > 30):
    print(stud.id, stud.name)

#Студенты питоняшки
for stud in (Students
             .select(Students.id, Students.name)
             .join(StudentCourses, on=(Students.id == StudentCourses.student_id))
             .join(Courses, on=(StudentCourses.course_id == Courses.id))
             .where(Courses.name == "python")
            ):
    print(stud.name)

#Студенты питоняшки из СПб
for stud in (Students
             .select(Students.id, Students.name)
             .join(StudentCourses, on=(Students.id == StudentCourses.student_id))
             .join(Courses, on=(StudentCourses.course_id == Courses.id))
             .where((Courses.name == "python") & (Students.city == "Spb"))
            ):
    print(stud.name)

conn.close()