import datetime
from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)

    def __str__(self):
        return  self.title


    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        was_published_recently.admin_order_field = "pub_date"
        was_published_recently.boolean = True
        was_published_recently.short_description = "published recently?"


class Comment(models.Model):
    author = models.CharField(max_length=70)
    pub_date = models.DateTimeField('date published')
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.author + '\n' + self.comment

class User(models.Model):
    pass