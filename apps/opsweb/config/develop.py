# -*- coding: UTF-8 -*-

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': "opsweb",
         'USER': 'root',
         'PASSWORD': '123456',
         'HOST': '127.0.0.1',
         'PORT': 3306,
      },
}

LANGUAGE_CODE = 'zh-hans'
