from django.contrib import admin

from .models import Tag, News


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_tag', 'public_date']

