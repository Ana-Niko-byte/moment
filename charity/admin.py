from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


@admin.register(Charity)
class CharityAdmin(SummernoteModelAdmin):
    '''
    A class registering the Charity model using Django Summernote.

    Methods:
    Displays fields 'name', 'category', 'entry_donation' in a list in admin.
    Allows search-by 'name' and 'category'.
    Allows quick filtering by 'category'.
    Pre-populates the slug field with the slugified 'name' value.
    Customizes the 'description' field for better UIUX in the admin panel.
    '''
    list_display = ('name', 'category', 'entry_donation')
    search_fields = ['name', 'category']
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    '''
    A class registering the Profile model using Django Summernote.

    Methods:
    Displays fields 'user' and 'date_added' in a list in admin.
    Allows search-by 'user'.
    '''
    list_display = ('user', 'date_added')
    search_fields = ['user', 'birth_date', 'charities']