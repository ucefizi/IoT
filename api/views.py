from django.http import JsonResponse
from django.shortcuts import HttpResponse

from receive.models import *

def index(request):
	return HttpResponse('This API provides JSON data for front-end devoloppers to use in their apps')

def rooms(request):
	r = Room.objects.all()
	dic = {}
	for i in r:
		dic[i.name] = {'surface': i.surface, 'volume': i.volume}
	return JsonResponse(dic)

def data(request, room):
	data = Capture.objects.filter(room=room)
	types = []
	for i in data:
		types.append(i.var)
	types = list(set(types))
	dic = {i:None for i in types}
	for i in data:
		for j in dic:
			if i.var == j and dic[j] == None :
				dic[j] = i.value
	return JsonResponse(dic)