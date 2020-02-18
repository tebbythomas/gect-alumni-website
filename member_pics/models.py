from django.db import models
from datetime import datetime
from members.models import Member


class MemberPic(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='members_pics/%Y/%m/%d/')
    caption = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return f"{self.member.display_name}'s pic : {self.caption}"
