# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Album



class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model   = Album
        fields  = ('album_name', 'artist', 'tracks')