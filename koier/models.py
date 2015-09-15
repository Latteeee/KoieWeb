from __future__ import unicode_literals

from django.db import models

class Koie(models.Model):
    navn = models.CharField(max_length=30)
    sengeplasser = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()

class Rapport(models.Model):
    koie = models.ForeignKey(Koie)
    dato = models.DateField()
    skaderapport = models.CharField(max_length=200)
    vedstatus = models.IntegerField()

class Dugnad(models.Model):
    koie = models.ForeignKey(Koie)
    dato = models.DateField()

class Booking(models.Model):
    koie = models.ForeignKey(Koie)
    email = models.EmailField()
    dato = models.DurationField()

class Message(models.Model):
    koie = models.ForeignKey(Koie)
    message = models.TextField(max_length=300)


