from django.shortcuts import render, HttpResponse
from django.http import Http404, JsonResponse

from receive.models import *
from charts.forms import *

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
	form = ChartForm(initial={'room': room.name})
	return render(request, 'room_captures.html', {
		'captures': captures,
		'room': room,
		'form': form,
	})

def capture_details(request, id):
	try: capture = Capture.objects.get(id=id)
	except Capture.DoesNotExist: raise Http404('this capture does not exist')
	return render(request, 'capture_details.html', {
		'capture': capture,
	})

def status(request):
	rooms = Room.objects.all()
	data = [{} for i in range(len(rooms))]
	for i in range(len(rooms)):
		data[i]['room'] = rooms[i].name
		data[i]['data'] = []
		try : captures = Capture.objects.filter(room=rooms[i].name)
		except Capture.DoesNotExist: raise Http404('{} has no captures yet'.format(room.name))
		types = []
		for j in captures:
			types.append(j.var)
		types = list(set(types))
		data[i]['data'] = [{} for j in types]
		for j in range(len(types)):
			data[i]['data'][j]['name'] = types[j]
			data[i]['data'][j]['value'] = None
			data[i]['data'][j]['when'] = None
			data[i]['data'][j]['aver'] = None
			data[i]['data'][j]['max'] = None
			data[i]['data'][j]['min'] = None
		
		by_type = [[] for j in types]
		by_filed = [{
			'room': [],
			'when': [],
			'value': [],
			'var': [],
			'unit': [],
			'id': []
		} for j in types]

		for j in range(len(types)):
			try : by_type[j] = Capture.objects.filter(room=rooms[i].name, var=types[j])
			except Capture.DoesNotExist: raise Http404('{} has no captures yet'.format(room.name))

		for j in range(len(types)):
			for k in range(len(by_type[j])):
				by_filed[j]['room'].append(by_type[j][k].room)
				by_filed[j]['when'].append(by_type[j][k].when)
				by_filed[j]['value'].append(by_type[j][k].value)
				by_filed[j]['var'].append(by_type[j][k].var)
				by_filed[j]['unit'].append(by_type[j][k].unit)
				by_filed[j]['id'].append(by_type[j][k].id)

		for j in range(len(types)):
			data[i]['data'][j]['value'] = by_filed[j]['value'][-1]
			data[i]['data'][j]['when'] = by_filed[j]['when'][-1]
			data[i]['data'][j]['aver'] = sum(by_filed[j]['value'])/len(by_filed[j]['value'])
			data[i]['data'][j]['max'] = max(by_filed[j]['value'])
			data[i]['data'][j]['min'] = min(by_filed[j]['value'])

	return render(request, 'status.html', {
			'data': data,
		})