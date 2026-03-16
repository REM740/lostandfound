from django.contrib import admin
from .models import LostItem, FoundItem


class LostItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'lost_in', 'lost_by', 'date_lost')
    search_fields = ('name', 'description', 'lost_in')


class FoundItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'claimed_by', 'date_claimed')
    search_fields = ('name', 'description')


admin.site.register(LostItem, LostItemAdmin)
admin.site.register(FoundItem, FoundItemAdmin)
