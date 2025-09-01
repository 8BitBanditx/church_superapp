from django.contrib import admin
from .models import PrayerRequest

class PrayerRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_submitted', 'is_public', 'answered')
    search_fields = ('name', 'request')
    list_filter = ('is_public', 'answered')

admin.site.register(PrayerRequest, PrayerRequestAdmin)
