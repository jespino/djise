from django.conf.urls.defaults import patterns, include, url
from djise.views import EventView, VoteView, DetailSuperView, ListSuperView

from djise.models import *
from django.views.generic import ListView, DetailView

urlpatterns = patterns('',
    url(r'^$', ListSuperView.as_view(model=Entity, menu=['entities']), name='entities'),
    url(r'entity/(?P<slug>[\w\d\-]+)/$', DetailSuperView.as_view(model=Entity, menu=['entities']), name='entity'),
    url(r'events/$', ListSuperView.as_view(model=Event, menu=['events']), name='events'),
    url(r'event/(?P<slug>[\w\d\-]+)/$', EventView.as_view(), name='event'),
    url(r'activity/(?P<slug>[\w\d\-]+)/$', DetailSuperView.as_view(model=Activity, menu=['events']), name='activity'),
    url(r'activity/(?P<slug>[\w\d\-]+)/vote/$', VoteView.as_view(), name='activity-vote'),
)
