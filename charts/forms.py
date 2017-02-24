from django import forms
from .models import Chart

class ChartForm(forms.ModelForm):
    class Meta:
        model = Chart
        fields = ('room', 'var', 'plot', 'fromdate', 'todate')