# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView


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
