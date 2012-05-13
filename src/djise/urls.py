from django.conf.urls.defaults import patterns, include, url
from djise.views import EventView

from djise.models import *
from django.views.generic import ListView, DetailView

urlpatterns = patterns('',
    url(r'entities/$', ListView.as_view(model=Entity), name='entities'),
    url(r'entity/(?P<slug>[\w\d\-]+)/$', DetailView.as_view(model=Entity), name='entity'),
    url(r'events/$', ListView.as_view(model=Event), name='events'),
    url(r'event/(?P<slug>[\w\d\-]+)/$', EventView.as_view(), name='event'),
    url(r'activities/$', ListView.as_view(model=Activity), name='activities'),
    url(r'activity/(?P<slug>[\w\d\-]+)/$', DetailView.as_view(model=Activity), name='activity'),
)
