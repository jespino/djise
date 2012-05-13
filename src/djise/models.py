from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

STATUS_CHOICES = (
        ('in-progress', _('In progress')),
        ('closed', _('Closed')),
        ('voting', _('Voting')),
        ('call-for-papers', _('In Call 4 Papers')),
)

class Entity(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Event(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=50)
    status = models.SlugField(max_length=25, choices=STATUS_CHOICES)
    entity = models.ForeignKey('Entity', related_name='events')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Activity(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField()
    event = models.ForeignKey('Event', verbose_name='Event', related_name='activities')
    votes = models.IntegerField(default=0)
    datetime = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class ActivityAttachment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    activity = models.ForeignKey('Activity', related_name='attachments')
    attachment = models.FileField(upload_to='activity_attachments')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class EventAttachment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    event = models.ForeignKey('Event', related_name='attachments')
    attachment = models.FileField(upload_to='activity_attachments')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
