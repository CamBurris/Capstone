from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from contact.forms import ContactForm1, ContactForm2, ContactForm3
from contact.views import ContactWizard
from studentProjects.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^$', 'mysite.views.index'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^polls/', include('polls.urls', namespace="polls")),
	url(r'^project/', include('project.urls', namespace="project")),
	url(r'^dates/', include('dates.urls', namespace="dates")),
	url(r'^links/', include('links.urls', namespace="links")),
	url(r'^awards/', include('awards.urls', namespace="awards")),
	url(r'^contact/', ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3])),
	url(r'^create/', index.as_view()),
	url(r'^contributors/', include('contributors.urls', namespace="contributors")),
	url(r'^about/', 'mysite.views.about'),
	url(r'^forms/', 'mysite.views.forms'),
	#url(r'^book/', index.as_view()),
)
