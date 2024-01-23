from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm

app_name = "login"

def homepage(request):
	return render(request, 'registration/home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login:profile')  # Redirect to profile page after login
 # Redirect to profile page after registration
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('login:profile')  # Redirect to profile page after login
  # Redirect to profile page after login
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login:login')# Redirect to login page after logout
@login_required
def profile(request):
    return render(request, 'registration/profile.html')