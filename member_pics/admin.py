from django.contrib import admin
from .models import MemberPic

class MemberPicAdmin(admin.ModelAdmin):
    list_display = ('id', 'member', 'caption')
    list_filter = ('member','caption')
    list_editable = ('caption','member')
    search_fields = ('caption', 'member')
    
admin.site.register(MemberPic, MemberPicAdmin)