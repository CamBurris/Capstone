from django.conf.urls import patterns, url
from contributors import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)