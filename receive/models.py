from django.db import models
from django.utils import timezone

class Room(models.Model):
	name = models.CharField(max_length=25)
	surface = models.FloatField()
	volume = models.FloatField()

class Capture(models.Model):
	room = models.CharField(max_length=25)
	when = models.DateTimeField(default=timezone.now)
	value = models.FloatField()
	var = models.CharField(max_length=20)
	unit = models.CharField(max_length=10)

class Thing(models.Model):
	STATUS_CHOICES = (
		('on', 'on'),
		('off', 'off')
	)
	room = models.CharField(max_length=25)
	obj = models.CharField(max_length=25)
	status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='off')
	when = models.DateTimeField(default=timezone.now)