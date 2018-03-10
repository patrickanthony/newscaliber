from django.contrib import admin

from .models import BlogPost
"""
class ChoiceInline(admin.StackedInline):
    model = BlogPost
    extra = 3
"""

class BlogAdmin(admin.ModelAdmin):
    fieldset = [
    (None,                  {'fields': ['title']}),
    ('Date information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
#    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['content','title', 'author']
    list_display = ('title','pub_date', 'author')

admin.site.register(BlogPost, BlogAdmin)