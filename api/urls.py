from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^rooms/$', views.rooms, name='rooms'),
	url(r'^data/room=(?P<room>[a-z,A-Z]+\d+)', views.data, name='data'),
]