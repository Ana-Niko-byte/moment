from django.urls import path
from .views import *

urlpatterns = [
    path('make-donation/', donation_checkout, name='checkout'),
]
