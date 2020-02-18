from django.db import models
from datetime import datetime

class NewsArticle(models.Model):
    headline = models.CharField(max_length=200)
    brief_description = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='news-articles/%Y/%m/%d/', default='default/default.png')
    full_article = models.TextField()
    def __str__(self):
        return self.headline