# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Assets



class AssetsSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Assets
        fields  = "__all__"