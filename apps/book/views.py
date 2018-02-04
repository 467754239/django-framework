# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import logging

from .models import Book
from .models import School

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from .serializers import SchoolSerializer


logger = logging.getLogger('api')
# Create your views here.


def BookFunc(request):

    if request.method == 'GET':
        return HttpResponse("book func-base view, method: GET")

    elif request.method == 'POST':
        return HttpResponse("book func-base view, method: POST")


class BookView(View):

    def get(self, request, *args, **kwargs):
        logger.debug(self.args)
        logger.debug(self.kwargs)
        return HttpResponse("book class-base view, method: GET")

    def post(self, request):
        return HttpResponse("book class-base view, method: POST")


class BookTemplateView(TemplateView):
    template_name = "book/book.html"

    # v1
    def get_context_data(self, **kwargs):
        context = super(BookTemplateView, self).get_context_data(**kwargs)  # 先执行父类并保存父类的执行结果
        # logger.debug(kwargs)
        context['username'] = 'monkey'
        context['books'] = ['python', 'golang', 'shell']
        return context

    '''v2
    def get_context_data(self, **kwargs):
        kwargs['username'] = 'monkey'
        kwargs['books'] = ['python', 'golang', 'shell']
        return super(BookTemplateView, self).get_context_data(**kwargs)  # 先执行父类并保存父类的执行结果
    '''


# 列表页
class BookListView(ListView):
    model = Book
    template_name = 'book/book_paginate.html'
    context_object_name = 'object_list'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)  # 先执行父类并保存父类的执行结果
        context['job'] = 'pythoner'
        return context

    def get_queryset(self):
        return self.model.objects.order_by('-name')


# 详情页
class BookDetailView(DetailView):
    model = Book
    context_object_name = 'object_list'
    template_name = 'book/book_detail.html'

    def get_context_data(self, **kwargs):
        kwargs['CurrentTime'] = datetime.datetime.now()
        return super(BookDetailView, self).get_context_data(**kwargs)  # 先执行父类并保存父类的执行结果



# Restful
'''
http://www.django-rest-framework.org/tutorial/3-class-based-views/
'''
@method_decorator(csrf_exempt, name='dispatch')
class BookRestfulList(APIView):
    model = School
    serializer_class = SchoolSerializer

    #@method_decorator(csrf_exempt)
    #def dispatch(self, *args, **kwargs):
    #    return super(BookRestfulList, self).dispatch(*args, **kwargs)
    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk:
            obj = self.get_object(pk)
            serializer = self.serializer_class(obj)
        else:
            objs = self.model.objects.all()
            serializer = self.serializer_class(objs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        s= self.serializer_class(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        obj = self.get_object(pk)
        s= self.serializer_class(obj, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
mixins.ListModelMixin # 返回queryset数据
mixins.RetrieveModelMixin # 返回单条数据


http://www.django-rest-framework.org/tutorial/3-class-based-views/
'''
class SchoolDetail(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):

    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def get(self, request, *args, **kwargs):
	if kwargs.get('pk', None):
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
