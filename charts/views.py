from django.shortcuts import render, HttpResponse
import django

import matplotlib.pyplot
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from .models import *
from .forms import *
from receive.models import Capture

def index(request):
	
	if request.method == 'POST':
		chart_form = ChartForm(data=request.POST)
		chart = chart_form.save(commit=False)
		captures = Capture.objects.filter(room=chart.room, var=chart.var)
		fig=Figure()
		ax=fig.add_subplot(111)
		x=[]
		y=[]
		for capt in captures:
			if capt.when >= chart.fromdate and capt.when <= chart.todate:
				x.append(capt.when)
				y.append(capt.value)

		if len(x) >= 1:
			if chart.plot == 'scatter':
				ax.plot(x, y, 'ro')
			elif chart.plot == 'line' :
				ax.plot(x, y, 'r-')
			elif chart.plot == 'scatterline':
				ax.plot(x, y, 'ro-')
			else: return HttpResponse('Please specify a valid plot!')

			ax.set_xlabel('time')
			ax.set_ylabel(chart.var)
			ax.set_title(chart.plot + 'plot for the ' + chart.var + ' of the room ' + chart.room)
			ax.xaxis_date()

			fig.autofmt_xdate()

			canvas=FigureCanvas(fig)
			response=django.http.HttpResponse(content_type='image/png')
			canvas.print_png(response)
			return response
		else: return HttpResponse('Nothing found!', status=404)

	else:
		form = ChartForm()
		return render(request, 'charts/index.html', {
			'form': form,
		})