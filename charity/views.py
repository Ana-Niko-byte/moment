from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import EmailMessage

from .models import *
from .forms import *

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


def charity_detail(request, slug):
    charity = get_object_or_404(Charity, slug=slug)

    context = {
        'charity': charity,
    }
    return render(
        request,
        "charity/charity_detail.html",
        context
    )

def contact(request):
    contactForm = ContactForm()
    if request.method == 'POST':
        if contactForm.is_valid():
            contactForm = ContactForm()
            messages.add_message(
                request, messages.SUCCESS,
                '''Your message has been forwarded onto our team! We
                endeavour to respond within 2 business days :)'''
            )
            return redirect('home')
        else:
            contactForm = ContactForm()
    context = {
        'contactForm': contactForm,
    }
    
    return render(
        request,
        "charity/contact.html",
        context
    )