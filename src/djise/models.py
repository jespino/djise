from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify


def slugify_uniquely(value, model, slugfield="slug"):
    """Returns a slug on a name which is unique within a model's table
       self.slug = SlugifyUniquely(self.name, self.__class__)
    """
    suffix = 0
    potential = base = slugify(value)
    if len(potential) == 0:
        potential = 'null'
    while True:
        if suffix:
                potential = "-".join([base, str(suffix)])
        if not model.objects.filter(**{slugfield: potential}).count():
                return potential
        # we hit a conflicting slug, so bump the suffix & try again
        suffix += 1


STATUS_CHOICES = (
        ('in-progress', _('In progress')),
        ('closed', _('Closed')),
        ('voting', _('Voting')),
        ('call-for-papers', _('In Call 4 Papers')),
)

LEVEL_CHOICES = (
        ('very-easy', _('Very easy')),
        ('easy', _('Easy')),
        ('normal', _('Normal')),
        ('hard', _('Hard')),
        ('very-hard', _('Very hard')),
)

class Entity(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class Event(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.SlugField(max_length=25, choices=STATUS_CHOICES)
    entity = models.ForeignKey('Entity', related_name='events')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class Activity(models.Model):
    slug = models.SlugField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    event = models.ForeignKey('Event', verbose_name=_('Event'), related_name='activities')
    votes = models.IntegerField(default=0)
    datetime = models.DateTimeField(null=True, blank=True)
    speaker = models.CharField(max_length=255)
    duration = models.IntegerField(null=True, blank=True)
    knowledges_needed = models.TextField(null=True, blank=True)
    level = models.SlugField(choices=LEVEL_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_uniquely(self.name, self.__class__)
        return super(Activity, self).save(*args, **kwargs)

class ActivityAttachment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    activity = models.ForeignKey('Activity', related_name='attachments')
    attachment = models.FileField(upload_to='activity_attachments')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class EventAttachment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    event = models.ForeignKey('Event', related_name='attachments')
    attachment = models.FileField(upload_to='activity_attachments')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
