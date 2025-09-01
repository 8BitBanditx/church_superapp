from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prayer/', include('prayers.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('events/', include('events.urls')),
    path('volunteers/', include('volunteers.urls')),
    path('donations/', include('donations.urls')),
    path('scripturebot/', include('scripturebot.urls')),




]
