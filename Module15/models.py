from peewee import *

conn = SqliteDatabase('database_prod.sqlite')

cursor = conn.cursor()

class BaseModel(Model):
    class Meta:
        database = conn


class Courses(BaseModel):
    id = AutoField(column_name='id')
    name = CharField(column_name='name')
    time_start = TextField(column_name='time_start')
    time_end = TextField(column_name='time_end')

class Students(BaseModel):
    id = AutoField(column_name='id')
    name = CharField(column_name='name')
    surname = CharField(column_name='surname')
    age = IntegerField(column_name='age')
    city = CharField(column_name='city')


class StudentCourses(BaseModel):
    student_id = ForeignKeyField(Students, backref='studkiss')
    course_id = ForeignKeyField(Courses, backref='coursersy')

conn.close()