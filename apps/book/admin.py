# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Book
from .models import Publish
# Register your models here.



class BookAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'publish', 'create_time', 'update_time')

class PublishAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'city', 'create_time', 'update_time')


admin.site.register(Book, BookAdmin)
admin.site.register(Publish, PublishAdmin)
