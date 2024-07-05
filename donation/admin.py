from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


class DonationAdmin(admin.ModelAdmin):
    '''
    A class registering the Donation model using Django Summernote.

    Methods:
    Displays fields 'charity', 'donation_amount', 'donation_user',
    'donation_date'.
    in a list in admin.
    Allows search-by 'charity' and 'donation_user'.
    Allows quick filtering by 'charity', 'donation_user' and 'donation_date'.
    '''
    readonly_fields = ('donation_number', 'donation_date')
    list_display = (
        'charity',
        'donation_amount',
        'donation_user',
        'donation_date'
    )
    search_fields = ['charity', 'donation_user']
    list_filter = ('charity', 'donation_user', 'donation_date')
    ordering = ('-donation_date',)


admin.site.register(Donation)
