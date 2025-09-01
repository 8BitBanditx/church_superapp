from django import forms
from .models import VolunteerSignUp

class VolunteerSignupForm(forms.ModelForm):
    class Meta:
        model = VolunteerSignUp
        fields = ['name', 'email', 'opportunity']  # add more if you need
