from django.urls import path
from .views import *

urlpatterns = [
    path('canvas/', canvas, name='common_canvas'),
]
