#!/bin/bash

cd /opt/opsweb/apps
python manage.py celery worker -c 4 --loglevel=info
