from django.shortcuts import render, HttpResponse
from .models import *
from website.settings import NON_SECRET_KEY

def room(request, name, surf, vol, key):
	if key == NON_SECRET_KEY:
		x = Room.objects.filter(name=name)
		if not len(x):
			new_room = Room()
			new_room.name = name
			new_room.surface = surf
			new_room.volume = vol
			new_room.save()
			return HttpResponse('room saved')
		else: return HttpResponse('room already in db', status=445)
	else: return HttpResponse('denied', status=401)

def capture(request, var, val, unit, room, key):
	if key == NON_SECRET_KEY:
		x = Room.objects.filter(name=room)
		if not len(x):
			new_room = Room()
			new_room.name = room
			new_room.surface = 15.0
			new_room.volume = 45.0
			new_room.save()
		new_capture = Capture()
		new_capture.var = var
		new_capture.value = val
		new_capture.unit = unit
		new_capture.room = room
		new_capture.save()
		return HttpResponse('saved')
	else: return HttpResponse('denied', status=401)

def captures(request, var, val, unit, room, key):
	if key == NON_SECRET_KEY:
		types = var.split(';')[:-1]
		values = val.split(';')[:-1]
		units = unit.split(';')[:-1]
		x = Room.objects.filter(name=room)
		if not len(x):
			new_room = Room()
			new_room.name = room
			new_room.surface = 15.0
			new_room.volume = 45.0
			new_room.save()
		for i in range(len(types)):
			new_capture = Capture()
			new_capture.var = types[i]
			new_capture.value = float(values[i])
			new_capture.unit = units[i]
			new_capture.room = room
			new_capture.save()
		return HttpResponse('saved')
	else: return HttpResponse('denied', status=401)