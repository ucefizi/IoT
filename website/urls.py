from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^get_all_rooms$', rooms, name='rooms'),
	url(r'^room_captures/id=(?P<id>\d+)$', room_captures, name='room_captures'),
	url(r'^capture/id=(?P<id>\d+)$', capture_details, name='capture_details'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^receive/', include('receive.urls', namespace='receive', app_name='receive')),
    url(r'^charts/', include('charts.urls', namespace='charts', app_name='charts')),
    url(r'^api/', include('api.urls', namespace='api', app_name='api')),
]