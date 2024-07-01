from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

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
    if request.method == 'POST':
        contactForm = ContactForm(data=request.POST)
        if contactForm.is_valid():
            name = contactForm.cleaned_data['name']
            email = contactForm.cleaned_data['email']
            subject = contactForm.cleaned_data['subject']
            message = contactForm.cleaned_data['message']

            send_mail(
                subject=f"{subject}",
                message=f"{message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=["ananikolayenia@gmail.com", f"{email}"],
                # send_mail doesn't seem to have a reply_to? Check later in documentation
                # reply_to=[f"{email}"],
                fail_silently=False,
            )

            print('sending your message')
            send_mail()
            print('your message has been sent!')

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