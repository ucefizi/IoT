from django.db import models

class Chart(models.Model):
	PLOT_CHOICES = (
		('scatter', 'scatter'),
		('bar', 'bar'),
		('line', 'line'),
	)
	room = models.CharField(max_length=25)
	var = models.CharField(max_length=25)
	plot = models.CharField(max_length=10, choices=PLOT_CHOICES, default='scatter')