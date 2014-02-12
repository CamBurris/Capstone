from django.conf.urls import patterns, url
from dates import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)