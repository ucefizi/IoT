from django.http import JsonResponse
from django.shortcuts import HttpResponse, render

from receive.models import *

def index(request):
	return render(request, 'api/index.html')

def rooms(request):
	r = Room.objects.all()
	dic = {}
	dic['len'] = len(r)
	dic['data'] = {}
	for i in r:
		dic['data'][i.name] = {'surface': i.surface, 'volume': i.volume}
	return JsonResponse(dic)

def data(request, room):
	data = Capture.objects.filter(room=room)
	types = []
	for i in data:
		types.append(i.var)
	types = list(set(types))
	dic = {}
	dic['len'] = len(types)
	dic['data'] = {i:None for i in types}
	for i in data:
		for j in dic['data']:
			if i.var == j and dic['data'][j] == None :
				dic['data'][j] = i.value
	return JsonResponse(dic)