from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'birthday', 'family')
    search_fields = ('first_name', 'last_name', 'email', 'family')
    list_filter = ('family', 'birthday')

admin.site.register(Member, MemberAdmin)
