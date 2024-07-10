# accounts/urls.py
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
] + static(settings.STATIC_URL)
