from django.shortcuts import render

from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_details.html',{'product' : product})


