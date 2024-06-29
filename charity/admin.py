from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


@admin.register(Charity)
class CharityAdmin(SummernoteModelAdmin):

    list_display = ('name', 'category', 'entry_donation')
    search_fields = ['name', 'category']
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)
