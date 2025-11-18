from models import *
import factory, factory_peewee

conn = SqliteDatabase('database_test.sqlite')

Students._meta.database = conn
Courses._meta.database = conn
StudentCourses._meta.database = conn

class CourseFactory(factory_peewee.PeeweeModelFactory):
    class Meta:
        model = Courses
    name = factory.Faker('word')
    time_start = factory.Faker('past_date', start_date="-5d")
    time_end = factory.Faker('future_date', end_date="+5d")



class StudentFactory(factory_peewee.PeeweeModelFactory):
    class Meta:
        model = Students
    name = factory.Faker('first_name')
    surname = factory.Faker('last_name')
    age = factory.Faker('random_int', min=18, max=65)
    city = factory.Faker('city')


    @factory.post_generation
    def courses(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        if extracted:
            self.courses.add(*extracted)

class SubCourseFactory(factory_peewee.PeeweeModelFactory):
    class Meta:
        model = StudentCourses
    name = factory.Faker('sentence', nb=1)
    description = factory.Faker('text', nb=3)
    parent_course = factory.SubFactory(Courses)

