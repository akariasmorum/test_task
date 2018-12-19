from django.conf.urls import url, include
#import django.contrib.auth.urls

from . import views

urlpatterns = [
	url(r'^get-process', views.get_processes, name='processes'),
]