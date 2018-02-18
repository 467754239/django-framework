# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Assets
from .serializers import AssetsSerializer

from rest_framework.response import Response
from rest_framework.views import APIView



class AssetsApiView(APIView):
    model = Assets
    serializer_class = AssetsSerializer

    def get(self, request, *args, **kwargs):
        objs = self.model.objects.all()
        serializer = self.serializer_class(objs, many=True)
        return Response(serializer.data)

