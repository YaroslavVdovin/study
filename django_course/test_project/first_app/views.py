from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'news/home.html')

def creed(request):
    return render(request, 'news/bootstrap_practice.html')

def navigation_task(request):
    return render(request, 'news/bootstrap_practice_middle.html')

def blog_middle(request):
    return render(request, 'news/middle_blog.html')

def hard_blog(request):
    return render(request, 'news/hard_blog.html')