from django.urls import path
from .views import charity

urlpatterns = [
    path('', charity, name='home'),
]