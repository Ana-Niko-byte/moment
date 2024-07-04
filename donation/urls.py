from django.urls import path
from .views import *

urlpatterns = [
    path('donate/<slug:slug>', charity_donation, name='donate'),
]