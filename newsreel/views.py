from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import BlogPost


class IndexView(generic.ListView):
    template_name = 'newsreel/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return BlogPost.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:5]



class DetailView(generic.DetailView):
    model = BlogPost
    template_Name = 'newsreel/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return BlogPost.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = BlogPost
    template_name = 'newsreel/results.html'



class CurrentView(generic.DetailView):
    model = BlogPost
    template_name = 'newsreel/current.html'


    def comment():
        pass

