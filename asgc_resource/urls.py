from django.conf.urls import include, url
from asgc_resource import views

urlpatterns = [
    url(r'^primary_info/$', views.primaryinfo_list),
    url(r'^primary_info/(?P<hostname>[a-z0-9\-]+)/$', views.primaryinfo_list_detail)
]
