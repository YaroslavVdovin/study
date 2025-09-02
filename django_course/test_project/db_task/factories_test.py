import factory
from factory.django import DjangoModelFactory
from .models import Product

class DBFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    price = factory.Faker('random_digit')
    stock = factory.Faker('random_digit')
    category = 10