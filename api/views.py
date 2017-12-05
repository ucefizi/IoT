from django.http import JsonResponse
from django.shortcuts import HttpResponse, render

from receive.models import *

def index(request):
	return render(request, 'api/index.html')

def rooms(request):
	r = Room.objects.all()
	dic = {}
	dic['len'] = len(r)
	dic['data'] = [{}]*len(r)
	for i in range(len(r)):
		dic['data'][i] = {'room_name': r[i].name, 'surface': r[i].surface, 'volume': r[i].volume}
		captures = Capture.objects.filter(room=r[i].name)[::-1]
		types = []
		for j in captures: types.append(j.var)
		types = list(set(types))
		for j in types: dic['data'][i][j] = None
		for j in captures:
			for k in types:
				if j.var == k and dic['data'][i][k] == None : dic['data'][i][k] = j.value

	return JsonResponse(dic)
