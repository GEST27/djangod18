from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form':form,}
    return render(request, 'users/login.html', context = context)




def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))

    else:
        form = UserRegistrationForm()
    context = {'form': form,}
    return render(request, 'users/register.html', context=context)


def profile(request):
    if request.method == "POST":
        form = UserProfileForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users/profile.html'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {'form': form,}
    return render(request, 'users/profile.html', context = context)