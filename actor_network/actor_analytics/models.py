from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Actor(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    image = models.URLField(max_length=500)
    biography  = models.TextField()
    movie_list = models.TextField()
    relations = models.TextField()
    response_data = models.TextField()

    def __unicode__(self):
        return self.name
