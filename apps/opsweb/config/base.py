# -*- coding: UTF-8 -*-

"""
Django settings for opsweb project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import djcelery
import datetime

djcelery.setup_loader()
BROKER_URL= 'amqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'amqp://guest@localhost//'
#CELERY_TIMEZONE = TIME_ZONE
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=)=t7s8$%@ipn@hl-ptyab=bl4=#$wkm$)gnit+-)@g7)%)(lk'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

#ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "djcelery",
    "rest_framework_docs",
    "drf_openapi",
    "rest_framework",

    'api',
    'scheduler',
    'profiles',
    'book',
    'assets',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'opsweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, '..', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'opsweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

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



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

#LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Logger Handler
LOGGING = {
   "version": 1,
   'disable_existing_loggers': False,
   "loggers": {
        "api": {
                 "level": "DEBUG",
                 "handlers": ["console_handle", "opsweb_file_handle"],
             },
        "django": {
             "level": "DEBUG",
             "handlers": ["django_handle"],
         },
    },
   "handlers": {
        "console_handle": {
             "class": "logging.StreamHandler",
             "formatter": 'simple'
         },
        "opsweb_file_handle": {
             "class": "logging.FileHandler",
             "filename": os.path.join(os.path.abspath(os.path.join(BASE_DIR, "..", "..")), "logs", "api.log"),
             "formatter": "api"
         },
        "django_handle": {
             "class": "logging.FileHandler",
             "filename": os.path.join(os.path.abspath(os.path.join(BASE_DIR, "..", "..")), "logs", "django.log"),
             "formatter": "simple"
         },
        'console': {
             'level': 'DEBUG',
             'class': 'logging.StreamHandler',
         }
    },
   'formatters': {
        'api': {
             'format': '[%(asctime)s] [%(process)d] [%(thread)d] [%(filename)16s:%(lineno)4d] [%(levelname)-6s] %(message)s'
         },
        'simple': {
             'format': '%(asctime)s %(levelname)s %(message)s'
         }
    },
}


# Session
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 60 * 150
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# CELERY
CELERYD_LOG_FILE = os.path.join(os.path.abspath(os.path.join(BASE_DIR, "..", "..")), "logs", "celery.log")
CELERYD_LOG_FORMAT = '[%(asctime)s] [%(processName)s] [%(levelname)s] %(message)s'
CELERYD_TASK_LOG_FORMAT = '[%(asctime)s] [%(processName)s] [%(levelname)s] [%(task_name)s] [%(task_id)s] [%(filename)s:%(lineno)s] %(message)s'
CELERYD_LOG_LEVEL = 'DEBUG'


#REST_FRAMEWORK = {
#    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning'
#}


# https://github.com/manosim/django-rest-framework-docs
REST_FRAMEWORK_DOCS = {
    'HIDE_DOCS': False  # Default: False
}


'''
JSONParser
    http://www.django-rest-framework.org/api-guide/parsers/
'''
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
            )
        }
