from django.shortcuts import render
from django.http import JsonResponse
from .models import Event  # Use your actual model name

def events_calendar(request):
    return render(request, 'events/calendar.html')

def events_json(request):
    # Example events; replace with your DB logic!
    events = [
        {
            "title": "Bible Study",
            "start": "2025-06-12T19:00:00",
            "end": "2025-06-12T20:30:00",
            "description": "Mid-week Bible study for all ages.",
            "location": "Main Sanctuary"
        },
        {
            "title": "Choir Rehearsal",
            "start": "2025-06-13T18:00:00",
            "end": "2025-06-13T19:30:00",
            "description": "Choir rehearsal, everyone welcome!",
            "location": "Choir Room"
        },
    ]
    return JsonResponse(events, safe=False)
