from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_prayer_request, name='submit_prayer_request'),
    path('list/', views.public_prayer_list, name='public_prayer_list'),
]
