from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


@admin.register(Donation)
class DonationAdmin(SummernoteModelAdmin):
    '''
    A class registering the Donation model using Django Summernote.

    Methods:
    Read-Only fields: all Donation model fields.
    Displays fields 'full_name', 'donation_amount', 'country',
    'postcode', 'donation_date' in a list in admin.
    Allows search-by 'full_name', 'charity' and 'donation_user', 'country, and 'postcode'.
    Allows quick filtering by 'charity', 'donation_user', 'donation_date', and 'country'.
    Orders by earliest date.
    '''
    readonly_fields = [
        'donation_number',
        'full_name',
        'charity',
        'donation_amount',
        'country',
        'postcode',
        'donation_date',
    ]
    
    list_display = (
        'full_name',
        'donation_amount',
        'country',
        'postcode',
        'donation_date'
    )
    search_fields = ['full_name', 'charity', 'donation_user', 'country', 'postcode']
    list_filter = ('charity', 'donation_user', 'donation_date', 'country')
    ordering = ('-donation_date',)
