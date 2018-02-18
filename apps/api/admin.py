# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from .models import Album
from .models import Track

from django.contrib import admin



class AlbumAdmin(admin.ModelAdmin):
    search_fields = ('album_name',)
    list_display = ('album_name', 'artist')

class TrackAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'order')


# admin.site.register(Album)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Track, TrackAdmin)