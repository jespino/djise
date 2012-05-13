from django.contrib import admin
from djise.models import Entity

class EntityAdmin(admin.ModelAdmin):
    pass
admin.site.register(Entity, EntityAdmin)
