from django.contrib import admin
from .models import NewsArticle

class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'headline')
    list_filter = ('headline',)
    list_editable = ('headline',)
    search_fields = ('headline', 'brief_description', 'full_article')
    
admin.site.register(NewsArticle, NewsArticleAdmin)