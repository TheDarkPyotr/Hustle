from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
import requests

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.university =  form.cleaned_data.get('university')
            user.profile.university_username = form.cleaned_data.get('university_username')
            user.profile.university_password = form.cleaned_data.get('university_password')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

