from django.db import models

class Item(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=300)

class Contact(models.Model):
    name = models.TextField(max_length=300)
    email = models.TextField(max_length=300)
    message = models.TextField(max_length=800)

class Product(models.Model):
    name = models.TextField(max_length = 200)
    SKU_code = models.CharField(max_length = 8)
    description = models.TextField(max_length=1000)
    tags = models.TextField(max_length = 500)

class Review(models.Model):
    product = models.ForeignKey('pagination_unknown.Product', related_name='reviews', on_delete=models.CASCADE)
    email = models.EmailField('Почта обзорщика')
    rev_text = models.TextField('Текст обзора', max_length=2000)