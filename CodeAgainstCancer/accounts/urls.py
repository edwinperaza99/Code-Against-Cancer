# accounts/urls.py
from django.urls import path
from .views import login_view, SignUpView, user_logout
from . import views

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path("logout", views.user_logout , name='logout'),
    # Add more URLs as per your application requirements
]
