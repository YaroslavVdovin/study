from factory.django import DjangoModelFactory
from .models import Item, Product
import factory

class ItemFactory(DjangoModelFactory):
    class Meta:
        model = Item
    name = factory.Faker('word')
    description = factory.Faker('sentences', nb=5)

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product
    name = factory.Faker('sentence')
    SKU_code = factory.Faker('ean', length=8)
    description = factory.Faker('paragraph', nb_sentences=5)
    tags = factory.Faker('words', nb=5)