from django.urls import path

from .views import ItemView, ContactView, ProductView, ProdDetailView, review_posting, review_accepted

urlpatterns = [
    path('items/', ItemView.as_view(), name='list_of_items'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('products_revs/', ProductView.as_view(), name='products'),
    path('products_revs/<int:pk>/', ProdDetailView.as_view(), name='prod_detail'),
    path('products_revs/<int:product_id>/add_review', review_posting, name="prod_add_rev"),
    path('rev_accepted/', review_accepted, name="rev_accepted")
]