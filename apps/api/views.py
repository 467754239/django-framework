# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Album
from .serializers import AlbumSerializer

from rest_framework.response import Response
from rest_framework.views import APIView



class MonkeyApiView(APIView):
    model = Album
    serializer_class = AlbumSerializer

    def get(self, request, *args, **kwargs):
        objs = self.model.objects.all()
        serializer = self.serializer_class(objs, many=True)
        return Response(serializer.data)

