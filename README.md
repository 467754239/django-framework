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



## django login

```python
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')	# 装饰类，作用于它的所有方法。
class Book(View):

	@method_decorator(login_required)				# 装饰指定的HTTP请求方法，作用于该方法。
	def get(self, request):
		pass

	def post(self, request):
		pass
	
```

```python
from django.contrib.auth.mixins import LoginRequiredMixin


class Book(LoginRequiredMixin, View):

	def get(self, request):
		pass

	def post(self, request):
		pass
```
