from django.shortcuts import render
from .forms import *


def make_donation(request):
    donationForm = DonationForm()
    context = {
        'donationForm': donationForm,
    }
    return render(
        request, 
        'donation/donation.html',
        context
    )