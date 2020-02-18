from django.db import models
from datetime import datetime

class GalleryPic(models.Model):
    caption = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='gallery/%Y/%m/%d/', default='default/default.png')
    is_banner = models.BooleanField(default=False)
    def __str__(self):
        return self.caption