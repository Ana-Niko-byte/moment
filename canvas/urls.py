from django.urls import path
from .views import *

urlpatterns = [
    path('common/', canvas, name='common_canvas'),
]
