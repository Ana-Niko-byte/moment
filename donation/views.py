from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

class donation_view(TemplateView):
    template_name = "donation.html"
