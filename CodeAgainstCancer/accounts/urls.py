# accounts/urls.py
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import signup


urlpatterns = [
    path('registration/', signup, name='signup'),
] + static(settings.STATIC_URL)
