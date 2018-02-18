# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from .models import Assets
from .models import Flavor

from django.contrib import admin



class AssetsAdmin(admin.ModelAdmin):
    search_fields = ('instance_id', 'instance_name')
    list_display = ('instance_id', 'instance_name')

class FlavorAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'cpu_core_num', 'mem_total')


admin.site.register(Assets, AssetsAdmin)
admin.site.register(Flavor, FlavorAdmin)