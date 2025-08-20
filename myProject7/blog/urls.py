from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_details, name='blog_details'),
]