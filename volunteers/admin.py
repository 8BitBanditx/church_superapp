from django.contrib import admin
from .models import VolunteerOpportunity, VolunteerSignUp

@admin.register(VolunteerOpportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)

@admin.register(VolunteerSignUp)
class VolunteerSignUpAdmin(admin.ModelAdmin):
    list_display = ('name', 'opportunity', 'date_signed_up')
    search_fields = ('name', 'opportunity__title')
