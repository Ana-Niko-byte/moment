from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


@admin.register(Canvas)
class CanvasAdmin(SummernoteModelAdmin):
    '''
    A class registering the Canvas model using Django Summernote.

    Methods:
    Read-Only fields: 'charity', 'contributors', and 'start_date'.
    Displays fields 'canvas_name', 'charity', and 'due_date' in a list in admin.
    Allows search-by 'canvas_name' and 'charity'.
    Allows quick filtering by 'charity'.
    '''

    readonly_fields = [
        'charity',
        'contributors',
        'start_date',
    ]
    
    list_display = (
        'canvas_name',
        'charity',
        'due_date',
    )
    search_fields = ['canvas_name', 'charity']
    list_filter = ('charity',)
