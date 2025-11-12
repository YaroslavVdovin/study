from itertools import product

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView, FormView
from django.views.generic import DetailView

from django.urls import reverse_lazy

from .forms import Feedback, ProductRevForm
from .models import Item, Product, Review


class ItemView(ListView):
    model = Item
    template_name = 'item_list.html'
    paginate_by = 5
    context_object_name = 'items'

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_form"] = Feedback()
        return context

class ProductView(ListView):
    model = Product
    template_name = 'prod_list.html'
    paginate_by = 10
    context_object_name = 'products'


class ProdDetailView(DetailView):
    model = Product
    template_name = 'rev_input.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["review_form"] = ProductRevForm()
        return context


class RevInputView(FormView):
    form_class = ProductRevForm
    template_name = 'rev_input.html'
    success_url = reverse_lazy('rev_accepted')
    def form_valid(self, form):

        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)

        review = form.save(commit=False)
        review.product = product
        review.save()

        return super().form_valid(form)

class SuccessView(TemplateView):
    template_name = 'review_accepted.html'


# Create your views here.
