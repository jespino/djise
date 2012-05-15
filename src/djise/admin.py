from django.contrib import admin
from djise.models import *

class EntityAdmin(admin.ModelAdmin):
    pass
admin.site.register(Entity, EntityAdmin)

class EventAdmin(admin.ModelAdmin):
    pass
admin.site.register(Event, EventAdmin)

class ActivityAdmin(admin.ModelAdmin):
    pass
admin.site.register(Activity, ActivityAdmin)

class EventAttachmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(EventAttachment, EventAttachmentAdmin)

class ActivityAttachmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(ActivityAttachment, ActivityAttachmentAdmin)
