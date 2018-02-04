
import views

from django.conf.urls import url

urlpatterns = [

    # Function Base View
    url(r'^func-base$', views.BookFunc),


    # Class Base View
    url(r'^class-base$', views.BookView.as_view()),
    url(r'^template-base$', views.BookTemplateView.as_view()),
    url(r'^list-base$', views.BookListView.as_view()),
    url(r'^detail-base/(?P<pk>\d+)/$', views.BookDetailView.as_view()),

    # restful
    url(r'^restful/detail/$', views.SchoolDetail.as_view()),
    url(r'^restful/detail/(?P<pk>[0-9]+)/$', views.SchoolDetail.as_view()),
    url(r'^restful/$', views.BookRestfulList.as_view()),
    url(r'^restful/(?P<pk>[0-9]+)/$', views.BookRestfulList.as_view()),
]
