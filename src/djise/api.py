from rest_framework import viewsets
from djise.models import Entity, Activity, ActivityAttachment, Event, EventAttachment

class EntityViewSet(viewsets.ModelViewSet):
    model = Entity

class ActivityViewSet(viewsets.ModelViewSet):
    model = Activity

class ActivityAttachmentViewSet(viewsets.ModelViewSet):
    model = ActivityAttachment

class EventViewSet(viewsets.ModelViewSet):
    model = Event

class EventAttachmentViewSet(viewsets.ModelViewSet):
    model = EventAttachment
