from django.contrib import admin
from .models import *

class RoomAdmin(admin.ModelAdmin):
	list_display = ('name',)

class CaptureAdmin(admin.ModelAdmin):
	list_display = ('room', 'when')

admin.site.register(Room, RoomAdmin)
admin.site.register(Capture, CaptureAdmin)