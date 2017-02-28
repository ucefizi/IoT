from django.db import models
from django.utils import timezone
import datetime

class Chart(models.Model):
	PLOT_CHOICES = (
		('scatter', 'scatter'),
		('line', 'line'),
		('scatterline', 'scatterline'),
	)
	room = models.CharField(max_length=25)
	var = models.CharField(max_length=25)
	plot = models.CharField(max_length=15, choices=PLOT_CHOICES, default='scatter')
	fromdate = models.DateTimeField(default=datetime.datetime(2017, 1, 1))
	todate = models.DateTimeField(default=timezone.now)