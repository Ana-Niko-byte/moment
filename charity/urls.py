from django.urls import path, include
from .views import *

urlpatterns = [
    path('', charity_home, name='home'),
    path('charity/<slug:slug>', charity_detail, name='charity_detail'),
    path('contact/', contact, name='contact'),
    path('create-charity/', create_charity_account, name='create_charity'),
]
