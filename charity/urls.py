from django.urls import path
from .views import *

urlpatterns = [
    path('', charity_home, name='home'),
    path('donate/<slug:slug>', charity_donation, name='donate'),
    path('charity/<slug:slug>', charity_detail, name='charity_detail'),
]