from .models import PrayerRequest

def public_prayer_list(request):
    public_requests = PrayerRequest.objects.filter(is_public=True).order_by('-date_submitted')
    return render(request, 'prayers/public_prayer_list.html', {'public_requests': public_requests})
