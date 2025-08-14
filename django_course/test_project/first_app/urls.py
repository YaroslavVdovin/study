from django.urls import path

from .views import index, home, creed, navigation_task, blog_middle, hard_blog

urlpatterns = [
    path('index/', index),
    path('home/', home, name='home'),
    path('creed/', creed, name='creed'),
    path('navigating/', navigation_task, name='navigation_task'),
    path('blog_middle/', blog_middle, name='blog_middle'),
    path('hard/', hard_blog, name='hard_blog')
]