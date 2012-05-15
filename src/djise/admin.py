from django.contrib import admin
from djise.models import *

class EntityAdmin(admin.ModelAdmin):
    pass
admin.site.register(Entity, EntityAdmin)

class EventAttachmentInline(admin.TabularInline):
    model = EventAttachment

class EventAdmin(admin.ModelAdmin):
    inlines = [ EventAttachmentInline ]
admin.site.register(Event, EventAdmin)

class ActivityAttachmentInline(admin.TabularInline):
    model = ActivityAttachment

class ActivityAdmin(admin.ModelAdmin):
    inlines = [ ActivityAttachmentInline ]
admin.site.register(Activity, ActivityAdmin)
