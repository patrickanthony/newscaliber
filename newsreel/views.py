from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import BlogPost


class IndexView(generic.ListView):
    template_name = 'newsreel/index.html'
    context_object_name = 'latest_blog_post'

    def get_queryset(self):
        """Return the last five published questions."""
        return BlogPost.objects.order_by('-pub_date')[:5]