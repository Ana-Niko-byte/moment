from django.shortcuts import render, redirect
from django.conf import settings
from .forms import *

def donation_checkout(request):
    donationForm = DonationForm()

    context = {
        'donationForm': donationForm,
    }

    return render(
        request,
        'donation/donation.html',
        context
    )