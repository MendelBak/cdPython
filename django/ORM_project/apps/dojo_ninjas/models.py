# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField()

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas") #Foreign key connecting this to the dojo table, since many ninjas are in one dojo, but not vice vesa (Foreign Keys are always a One To Many Relationship).1459
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)