from django.views.generic import View
from django.http import HttpResponse
from djise.models import Entity
from django.core import serializers

class RestView(View):
    pass

class EntitiesRestView(RestView):
    def get(self, request):
        data = []
        for entity in Entity.objects.all():
            data.append(entity.slug)
        return HttpResponse(serializers.serialize("json", data))

    #def put(self, *args, **kwargs):

    #def post(self, entity_id):

    def delete(self, request):
        Entity.objects.all().delete()
        return HttpResponse('{ "ok":"true" }')

class EntityRestView(RestView):
    def get(self, request, slug):
        entity = get_object_or_404(Entity, slug=slug)
        data = serializers.serialize("json", entity)
        return HttpResponse(data)
        
    #def post(self, entity_id):

    def delete(self, request, slug):
        entity = get_object_or_404(Entity, slug=slug)
        entity.delete()
        return HttpResponse('{ "ok":"true" }')
