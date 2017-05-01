from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^capture/type=(?P<var>[a-z]+)&value=(?P<val>[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?)&unit=(?P<unit>[a-z]+)&room=(?P<room>[a-z,A-Z,0-9]+)&key=(?P<key>[a-z,A-Z,0-9]+)$', views.capture, name='capture'),
	url(r'^room/name=(?P<name>[a-z,A-Z,0-9]+)&surface=(?P<surf>(\d+(\.\d*)))&volume=(?P<vol>(\d+(\.\d*)))&key=(?P<key>[a-z,A-Z,0-9]+)$', views.room, name='room'),
	url(r'^captures/types=(?P<var>([a-z]+;)+)&values=(?P<val>([+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?;)+)&units=(?P<unit>([a-z]+;)+)&room=(?P<room>[a-z,A-Z,0-9]+)&key=(?P<key>[a-z,A-Z,0-9]+)$', views.captures, name='captures'),
	url(r'^thing/object=(?P<obj>[a-z, A-Z]+)&status=(?P<status>[a-z]+)&room=(?P<room>[a-z,A-Z,0-9]+)&key=(?P<key>[a-z,A-Z,0-9]+)', views.thing, name='thing'),
]