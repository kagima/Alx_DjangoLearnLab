from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required

# Registration view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form':form})

# Logout view
def logout(request):
    logout(request)
    return redirect('login') 

# Profile management
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})  

def blog(request):
    pass             

def post(request):
    pass 