import json
import os
from django.conf import settings
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django import forms   
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import CANCER_TYPE_CHOICES

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration successful!"))
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile_view(request):
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)
    cancer_type_display = dict(CANCER_TYPE_CHOICES).get(user_profile.cancer_type, user_profile.cancer_type)

    json_path = os.path.join(settings.BASE_DIR, 'static/cancer_information.json')
    with open(json_path, 'r') as json_file:
        cancer_data = json.load(json_file)
    cancer_info = cancer_data.get(user_profile.cancer_type, {
        'dietary_restrictions': 'No specific restrictions.',
        'recommended_foods': 'General healthy diet recommendations.',
        'special_instructions': 'Follow general health advice.'
    })

    context = {
        'user': user,
        'user_profile': user_profile,
        'cancer_type_display': cancer_type_display,
        'cancer_info': cancer_info
    }
    return render(request, 'profile/profile_page.html', context)