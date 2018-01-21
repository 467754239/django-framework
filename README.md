# django framework

- [x] admin
- [x] celery(rabbitmq)
- [x] docs 
- [x] split settings.py 
- [x] django-rest-freamework 
- [x] nginx + uwsgi + virtualenv + django


## deloy
```bash
$ cd /opt/django-framework/apps
$ virtualenv .venv
$ source .venv/bin/activate
$ pip install -r ../requirements.txt
$ python manage.py runserver 0.0.0.0:80
```

## django view method
- [x] function-base-view
- [x] class-base-view
    - [x] View 
    - [x] TemplateView
    - [x] ListView


