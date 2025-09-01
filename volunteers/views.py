from django.shortcuts import render
from .models import VolunteerOpportunity

def opportunities_list(request):
    opportunities = VolunteerOpportunity.objects.all()
    return render(request, 'volunteers/opportunities_list.html', {'opportunities': opportunities})

def volunteer_signup(request):
    # Placeholder, so Django stops complaining
    return render(request, 'volunteers/signup.html')

from django.shortcuts import render

def volunteer_thank_you(request):
    return render(request, 'volunteers/thank_you.html')
