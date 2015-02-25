from django.conf.urls import patterns, include, url
from django.contrib import admin
from sites import urls

urlpatterns = patterns('',
    url(r'^$', 'sites.views.index', name='home'),
    url(r'^summary/', 'sites.views.summary', name='summary'),
    url(r'^summary-average/', 'sites.views.average', name='average'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sites/',include(urls,namespace='sites')),
)
