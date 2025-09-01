from django.urls import path
from . import views

urlpatterns = [
    path('', views.opportunities_list, name='opportunities_list'),
    path('signup/', views.volunteer_signup, name='volunteer_signup'),
    path('thank-you/', views.volunteer_thank_you, name='volunteer_thank_you'),
]
