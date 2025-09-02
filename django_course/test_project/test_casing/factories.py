from factory.django import DjangoModelFactory
from .models import Courses, Students, SubCourses
import factory

class CourseFactory(DjangoModelFactory):
    class Meta:
        model = Courses
    name = factory.Faker('word')
    description = factory.Faker('sentences', nb=3)
    length = factory.Faker('random_int', min=10, max=150)


class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Students
    name = factory.Faker('first_name')
    age = factory.Faker('random_int', min=18, max=65)

    @factory.post_generation
    def courses(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        if extracted:
            self.courses.add(*extracted)

class SubCourseFactory(DjangoModelFactory):
    class Meta:
        model = SubCourses
    name = factory.Faker('sentence', nb=1)
    description = factory.Faker('text', nb=3)
    parent_course = factory.SubFactory(Courses)