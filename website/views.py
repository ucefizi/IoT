from django.shortcuts import render, HttpResponse
from django.http import Http404

from receive.models import *

def home(request):
	return render(request, 'home.html')

def rooms(request):
	rooms = Room.objects.all()
	return render(request, 'index.html', {
		'rooms': rooms,
	})

def room_captures(request, id):
	try: room = Room.objects.get(id=id)
	except Room.DoesNotExist: raise Http404('This room does not exist')
	try: captures = Capture.objects.filter(room=room.name)
	except Capture.DoesNotExist: raise Http404('This room has no captures yet')
	return render(request, 'room_captures.html', {
		'captures': captures,
		'room': room,
	})

def capture_details(request, id):
	try: capture = Capture.objects.get(id=id)
	except Capture.DoesNotExist: raise Http404('this capture does not exist')
	return render(request, 'capture_details.html', {
		'capture': capture,
	})