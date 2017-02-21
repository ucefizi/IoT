from django.shortcuts import render, HttpResponse
import django

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
			x.append(capt.when)
			y.append(capt.value)
		
		if chart.plot == 'scatter':
			ax.plot(x, y, 'ro')
		elif chart.plot == 'line' :
			ax.plot(x, y, 'r-')
		elif chart.plot == 'bar':
			ax.bar(x, y, width=10)
		else: return HttpResponse('Please specify a valid plot!')

		ax.xaxis_date()

		canvas=FigureCanvas(fig)
		response=django.http.HttpResponse(content_type='image/png')
		canvas.print_png(response)
		return response

	else:
		form = ChartForm()
		return render(request, 'charts/index.html', {
			'form': form,
		})