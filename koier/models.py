from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Koier(models.Model):
    name = models.CharField(max_length=30);
    sengeplasser = models.IntegerField(20);
    vedstatus = models.IntegerField(20);
