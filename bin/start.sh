#!/bin/bash

cd /opt/django-framework/apps
python manage.py celery worker -c 4 --loglevel=info
