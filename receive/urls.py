from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^capture/type=(?P<var>[a-z]+)&value=(?P<val>[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?)&unit=(?P<unit>[a-z]+)&room=(?P<room>[a-z,A-Z]+\d+)&key=(?P<key>[a-z,A-Z,0-9]+)$', views.capture, name='capture'),
	url(r'^room/name=(?P<name>[a-z,A-Z]+\d+)&surface=(?P<surf>(\d+(\.\d*)))&volume=(?P<vol>(\d+(\.\d*)))&key=(?P<key>[a-z,A-Z,0-9]+)$', views.room, name='room'),
]