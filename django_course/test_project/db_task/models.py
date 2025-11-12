from django.db import models
from django.core.validators import MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('db_task.Category', on_delete=models.CASCADE)
    stock = models.IntegerField(validators=[MinValueValidator(0)], default=0)