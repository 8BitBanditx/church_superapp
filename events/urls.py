from django.urls import path
from . import views

urlpatterns = [
    path('', views.events_calendar, name='events_calendar'),
    path('events.json', views.events_json, name='events_json'),  # This serves event data to the calendar!
]
