from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'sites.views.index', name='index'),
    url(r'^(?P<site_id>\d+)/$', 'sites.views.detail', name='detail'),
)
