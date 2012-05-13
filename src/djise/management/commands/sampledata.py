# encoding: utf-8

from django.core.management.base import BaseCommand, CommandError
import random
from djise.models import *
from django.contrib.webdesign import lorem_ipsum
import datetime

class Command(BaseCommand):
    args = ''
    help = 'Example data'
    
    random.seed(12345678901) # to ensure that we always insert the same data
                        
    # handle

    def handle(self, *args, **options):
        ENTITIES = 2
        EVENTS_PER_ENTITY = 3
        ACTIVITY_PER_EVENT = 5

        for x in range(ENTITIES):
            entity = Entity.objects.create(
                    slug=self.random_slug(),
                    name="%s %s" % (self.random_word(), self.random_word())
            )
            for y in range(EVENTS_PER_ENTITY):
                event = Event.objects.create(
                        slug=self.random_slug(),
                        name="%s %s %s" % (self.random_word(), self.random_word(), self.random_word()),
                        status=random.choice([ status[0] for status in STATUS_CHOICES ]),
                        entity=entity
                )
                for z in range(ACTIVITY_PER_EVENT):
                    activity = Activity.objects.create(
                            slug=self.random_slug(),
                            name="%s %s %s" % (self.random_word(), self.random_word(), self.random_word()),
                            description=self.random_paragraph(),
                            votes=self.random_value(10),
                            event=event
                    )
    
    # Random functions:

    def random_url(self):
        """Random number from 1 to max_value."""
        word1 = self.random_word()
        word2 = self.random_word()
        dot_x = random.choice(["com","es","org","net","info"])
        return "http://www.%s.%s/%s/" % (word1,dot_x,word2)

    def random_year(self):
        """Random number from 1 to max_value."""
        return random.randint(2000, 2011)

    def random_slug(self):
        return "%s-%s-%s" % (self.random_word(), self.random_word(), self.random_word())

    def random_sentence(self):
        """Random text with variable number of words, one sentence."""
        return lorem_ipsum.sentence()

    def random_paragraph(self):
        """Random text with variable number of words, one paragraph."""
        return lorem_ipsum.paragraph()

    def random_range(self, n):
        """Random number from 1 to max_value."""
        return range(0,self.random_value(n))

    def random_word(self):
        return lorem_ipsum.words(1, common=False)
    
    def random_value(self,max_value):
        """Random number from 0 to max_value - 1."""
        return random.randint(0, max_value-1)
        
    def random_value1(self,max_value):
        """Random number from 1 to max_value."""
        return random.randint(1, max_value+1)
          
    def random_boolean(self, weight_true = 1, weight_false = 1):
        """Random true/false value, with probability weights."""
        return random.choice([True] * weight_true + [False] * weight_false)
    
    def random_boolean_almost_false(self):
        """Random number from 1 to max_value."""
        return random.choice([True,False,False,False,False])

    def random_email(self):
        """Random mail address."""
        return lorem_ipsum.words(1, common=False) + u'@' + lorem_ipsum.words(1, common=False) + \
               random.choice([u'.es', u'.com', u'.org', u'.net', u'.gov', u'.tk'])
