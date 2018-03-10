import datetime
from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)

    def __str__(self):
        return  self.title


    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Comment(models.Model):
    author = models.CharField(max_length=70)
    pub_date = models.DateTimeField('date published')
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.author + '\n' + self.comment