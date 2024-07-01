from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Charity, Donation, Profile

# Create your views here.
def charity_home(request):
    charities = Charity.objects.all()

    context = {
        'charities' : charities,
    }
    
    return render(
        request,
        "charity/index.html",
        context
    )


def charity_donation(request, slug):
    charity = get_object_or_404(Charity, slug=slug)
    return render(
        request,
        "charity/donation.html"
    )
