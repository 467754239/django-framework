
## django + uwsgi
```
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/uwsgi/
http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html
```

## django settings split
```
https://stackoverflow.com/questions/10664244/django-how-to-manage-development-and-production-settings
```

## django doc
```
http://www.django-rest-framework.org/topics/documenting-your-api/
https://github.com/limdauto/drf_openapi/
```


## celery
```
http://docs.celeryproject.org/projects/django-celery/en/2.4/introduction.html#using-django-celery
http://www.cnblogs.com/alex3714/p/6351797.html
http://www.jianshu.com/p/1840035cb510
http://www.cnblogs.com/znicy/p/5626040.html
```

## utc
```
后端应该在数据库统一存储UTC时间并返回UTC时间给前端，
前端在发送时间和接收时间的时候要把时间分别从当前时区转换成UTC发送给后端，以及接收后端的UTC时间转换成当地时区。
```
