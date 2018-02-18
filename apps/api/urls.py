
import views

from django.conf.urls import url, include

urlpatterns = [

    url(r'^v1/demo/$', views.MonkeyApiView.as_view()),
]
