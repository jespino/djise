from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.serializers import HyperlinkedModelSerializer

from djise.models import Entity, Activity, ActivityAttachment, Event, EventAttachment

class CreateAny(IsAuthenticatedOrReadOnly):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        return super(CreateAny, self).has_permission(request, view)


class ActivitySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        read_only_fields = ['votes']


class EntityViewSet(viewsets.ModelViewSet):
    model = Entity


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    model = Activity

    permission_classes = [CreateAny]

    def create(self, request):
        return super(ActivityViewSet, self).create(request)

    @action(methods=["GET"], permission_classes=[AllowAny])
    def vote(self, request, pk=None):
        activity = self.get_object()
        activity.votes += 1
        activity.save()
        return Response({'status': 'voted'})


class ActivityAttachmentViewSet(viewsets.ModelViewSet):
    model = ActivityAttachment


class EventViewSet(viewsets.ModelViewSet):
    model = Event


class EventAttachmentViewSet(viewsets.ModelViewSet):
    model = EventAttachment
