from django.conf.urls.defaults import patterns, include, url
from djise.views import EventView, VoteView, DetailSuperView, ListSuperView

from djise.models import *
from django.views.generic import ListView, DetailView

from rest_framework import routers
from djise.api import EntityViewSet, ActivityViewSet, ActivityAttachmentViewSet, EventViewSet, EventAttachmentViewSet

router = routers.DefaultRouter()
router.register(r'entity', EntityViewSet)
router.register(r'activity', ActivityViewSet)
router.register(r'activity-attachment', ActivityAttachmentViewSet)
router.register(r'event', EventViewSet)
router.register(r'event-attachment', EventAttachmentViewSet)

urlpatterns = patterns('',
    url(r'^$', ListSuperView.as_view(model=Entity, menu=['entities']), name='entities'),
    url(r'^entity/(?P<slug>[\w\d\-]+)/$', DetailSuperView.as_view(model=Entity, menu=['entities']), name='entity'),
    url(r'^events/$', ListSuperView.as_view(model=Event, menu=['events']), name='events'),
    url(r'^event/(?P<slug>[\w\d\-]+)/$', EventView.as_view(), name='event'),
    url(r'^activity/(?P<slug>[\w\d\-]+)/$', DetailSuperView.as_view(model=Activity, menu=['events']), name='activity'),
    url(r'^activity/(?P<slug>[\w\d\-]+)/vote/$', VoteView.as_view(), name='activity-vote'),

    url(r'^api/v1/', include(router.urls, namespace="api-v1")),
)
