# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False

    # readonly_fields = ['user', 'phone']
    verbose_name = 'UserProfile'
    verbose_name_plural = 'user extend profile'

class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline, ]



admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
