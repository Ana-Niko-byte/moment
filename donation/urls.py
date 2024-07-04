from django.urls import path
from .views import *

urlpatterns = [
    path('make-a-donation/', make_donation, name='donation'),
]