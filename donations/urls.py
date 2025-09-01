from django.urls import path
from . import views

urlpatterns = [
    path('give/', views.online_giving, name='online_giving'),
]
