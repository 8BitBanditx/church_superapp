from django.shortcuts import render, redirect
from .forms import PrayerRequestForm

def submit_prayer_request(request):
    if request.method == 'POST':
        form = PrayerRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'prayers/thank_you.html')  # Simple thank you page
    else:
        form = PrayerRequestForm()
    return render(request, 'prayers/prayer_form.html', {'form': form})
from django.shortcuts import render
from .models import PrayerRequest

def public_prayer_list(request):
    public_requests = PrayerRequest.objects.filter(is_public=True).order_by('-date_submitted')
    return render(request, 'prayers/public_prayer_list.html', {'public_requests': public_requests})
