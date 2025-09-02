from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Courses(models.Model):
    name = models.TextField("Наименование курса", max_length=20, unique=True)
    description = models.CharField("Описание курса", default=None)
    length = models.IntegerField("Продолжительность в часах",
                                 validators=[MinValueValidator(10), MaxValueValidator(150)], default=None)

class Students(models.Model):
    name = models.CharField('ФИО студента', max_length=200)
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(65)])
    courses = models.ManyToManyField(Courses)

class SubCourses(models.Model):
    name = models.TextField('Наименование подраздела', max_length=100, unique=True)
    description = models.CharField("Описание раздела")
    parent_course = models.ForeignKey('test_casing.Courses', on_delete=models.CASCADE)
# Create your models here.
