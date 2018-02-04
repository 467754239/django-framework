# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Book, School

class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = '__all__'
