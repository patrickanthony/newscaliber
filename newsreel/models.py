import datetime
from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    date_published = models.DateTimeField('date published')
    content = models.CharField(max_length=2000)
    last_modified = models.DateField.auto_now_add


    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
