from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'email', 'is_authorized', 'branch', 'display_name', 'country', 'indian_state')
    list_filter = ('is_authorized', 'email', 'branch', 'user', 'country', 'indian_state')
    list_editable = ('is_authorized',)
    search_fields = ('user', 'email', 'is_authorized', 'branch', 'display_name', 'country', 'indian_state')
    
admin.site.register(Member, MemberAdmin)