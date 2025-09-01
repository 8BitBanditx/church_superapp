from django.shortcuts import render, redirect
from .models import Donation
from .forms import DonationForm

def donation_list(request):
    donations = Donation.objects.all().order_by('-date')
    return render(request, 'donations/donation_list.html', {'donations': donations})

def donation_add(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donation_list')
    else:
        form = DonationForm()
    return render(request, 'donations/donation_add.html', {'form': form})

def online_giving(request):
    return redirect("https://www.bbolm.com/about-5")
