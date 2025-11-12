from django.test import TestCase
from .models import Product, Category

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Кофе")
        self.product = Product.objects.create(name='Test Coffee', price=20.99, stock=20, category=Category.objects.get(name='Кофе'))
    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Coffee"),
        self.assertEqual(self.product.price,20.99)