# accounts/urls.py
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import signup, profile_view


urlpatterns = [
    path('registration/', signup, name='signup'),
    path('profile/', profile_view, name='profile'),
] + static(settings.STATIC_URL)
