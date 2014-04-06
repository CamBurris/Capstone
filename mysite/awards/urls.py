from django.conf.urls import patterns, url
from awards import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)