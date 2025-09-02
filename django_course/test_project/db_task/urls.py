from django.urls import path

from .views import product_list, product_details

urlpatterns = [
    path('products/', product_list),
    path("products/<int:product_id>/", product_details)
]