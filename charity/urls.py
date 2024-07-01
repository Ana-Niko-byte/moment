from django.urls import path
from .views import charity_home, charity_donation

urlpatterns = [
    path('', charity_home, name='home'),
    path('donate/<slug:slug>', charity_donation, name='donate'),
]