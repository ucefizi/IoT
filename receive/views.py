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
			return HttpResponse('Room Saved!')
		else: return HttpResponse('That room already saved!', status=445)
	else: return HttpResponse('Access Denied!', status=401)

def capture(request, var, val, unit, room, key):
	if key == NON_SECRET_KEY:
		x = Room.objects.filter(name=room)
		if not len(x):
			new_room = Room()
			new_room.name = room
			new_room.surface = 15
			new_room.volume = 45
			new_room.save()
		new_capture = Capture()
		new_capture.var = var
		new_capture.value = val
		new_capture.unit = unit
		new_capture.room = room
		new_capture.save()
		return HttpResponse('Capture Saved!')
	else: return HttpResponse('Access Denied!', status=401)