from itertools import product

from django.shortcuts import render, redirect
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


def review_posting(request, product_id):
    if not request.method == 'POST':
        return redirect('prod_detail', pk=product_id)

    form = ProductRevForm(request.POST)
    if form.is_valid():

        rev_text = form.cleaned_data['rev_text']
        email = form.cleaned_data['email']

        review = Review(
            product_id=product_id,
            rev_text=rev_text,
            email=email
        )

        review.save()
        return redirect('rev_accepted')
    return redirect('prod_detail', pk=product_id)


def review_accepted(request):
    return render(request, 'review_accepted.html')

# Create your views here.
