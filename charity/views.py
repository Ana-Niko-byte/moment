from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils.text import slugify

from .models import *
from .forms import *


# Create your views here.
def charity_home(request):
    '''

    '''
    charities = Charity.objects.all()

    context = {
        'charities' : charities,
    }

    return render(
        request,
        "charity/index.html",
        context
    )


def charity_detail(request, slug):
    '''

    '''
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
    '''
    A view for sending queries via the ContactForm on the Contact page.
    '''
    if request.method == 'POST':
        contactForm = ContactForm(data=request.POST)
        if contactForm.is_valid():
            name = contactForm.cleaned_data['name']
            email = contactForm.cleaned_data['email']
            subject = contactForm.cleaned_data['subject']
            message = contactForm.cleaned_data['message']

            recipient_list = ["ananikolayenia@gmail.com", f"{email}"]
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=recipient_list,
                fail_silently=False,
            )
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


def create_charity_account(request):
    '''
    '''
    if request.method == 'POST':
        charityForm = CharityForm(data=request.POST)
        if charityForm.is_valid():
            charity = charityForm.save(commit=False)
            charity.slug = slugify(charity.name)
            charity.community_size = 0
            charity.approved = False
            charity.save()
            messages.add_message(
                request, messages.SUCCESS,
                '''Your information has been successfully sent to our admins.
                We should have all your information revAdded successfully!'''
            )
        else:
            charityForm = CharityForm()
            messages.add_message(
                request, messages.error,
                '''Please review the form and fill in all necessary
                information. For any queries, please contact our team on our
                dedicated Contact page.'''
            )

    context = {
        'charityForm': CharityForm,
    }
    return render(
        request,
        'charity/create_charity.html',
        context
    )
