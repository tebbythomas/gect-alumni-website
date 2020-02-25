from django.contrib import admin
from .models import GalleryPic

class GalleryPicAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'is_banner')
    list_filter = ('is_banner', 'caption')
    list_editable = ('is_banner',)
    search_fields = ('caption', 'is_banner')
    
admin.site.register(GalleryPic, GalleryPicAdmin)