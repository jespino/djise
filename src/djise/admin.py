from django.contrib import admin
from djise.models import *

class EntityAdmin(admin.ModelAdmin):
    pass
admin.site.register(Entity, EntityAdmin)

class EventAttachmentInline(admin.StackedInline):
    pass

class EventAdmin(admin.ModelAdmin):
    inlines = [ EventAttachmentInline ]
admin.site.register(Event, EventAdmin)

class ActivityAttachmentInline(admin.StackedInline):
    pass

class ActivityAdmin(admin.ModelAdmin):
    inlines = [ ActivityAttachmentInline ]
admin.site.register(Activity, ActivityAdmin)
