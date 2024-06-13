# CodeAgainstCancer/urls.py
from django.contrib import admin
from django.urls import path, include
from accounts.views import homepageView  # Adjust as per your views import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepageView, name='home'),  # Adjust as per your view function
    path('accounts/', include('accounts.urls')),  # Make sure this import is correct
    # Add more URL patterns as needed
]
