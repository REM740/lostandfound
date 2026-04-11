from django.contrib import admin
from .models import LostItem, FoundItem


class LostItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'lost_in', 'lost_by', 'lost_by_email', 'date_lost')
    search_fields = ('name', 'description', 'lost_in', 'lost_by', 'lost_by_email')


class FoundItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'found_by', 'found_by_email', 'claimed_by', 'claimed_by_email', 'date_claimed')
    search_fields = ('name', 'description', 'found_by', 'found_by_email', 'claimed_by', 'claimed_by_email')


admin.site.register(LostItem, LostItemAdmin)
admin.site.register(FoundItem, FoundItemAdmin)
