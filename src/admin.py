from django.contrib import admin

# Register your models here.
from src.models import Event

admin.site.register(Event)       	#register your event import the event from model files

