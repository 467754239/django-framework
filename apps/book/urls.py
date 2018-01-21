
import views

from django.conf.urls import url

urlpatterns = [

    # Function Base View
    url(r'^func-base$', views.BookFunc),


    # Class Base View
    url(r'^class-base$', views.BookView.as_view()),
    url(r'^template-base$', views.BookTemplateView.as_view()),
]
