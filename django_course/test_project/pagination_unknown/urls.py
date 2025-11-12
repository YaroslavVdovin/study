from django.urls import path

from .views import ItemView, ContactView, ProductView, ProdDetailView, RevInputView, SuccessView

urlpatterns = [
    path('items/', ItemView.as_view(), name='list_of_items'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('products_revs/', ProductView.as_view(), name='products'),
    path('products_revs/<int:pk>/', ProdDetailView.as_view(), name='prod_detail'),
    path('products_revs/<int:product_id>/add_review', RevInputView.as_view(), name="prod_add_rev"),
    path('rev_accepted/', SuccessView.as_view(), name="rev_accepted")
]