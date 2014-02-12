from django.conf.urls import patterns, url
from project import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<project_id>\d+)/$', views.detail, name='detail'),
	url(r'^create/$', views.create, name='create'),
)