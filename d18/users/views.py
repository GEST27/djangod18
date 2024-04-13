from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from products.models import Basket
from django.contrib.auth.decorators import login_required

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
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))

    else:
        form = UserRegistrationForm()
    context = {'form': form,}
    return render(request, 'users/register.html', context=context)

@login_required
def profile(request):
    if request.method == "POST":
        form = UserProfileForm(instance=request.user, data = request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    baskets = Basket.objects.filter(user = request.user)
    total_sum = 0
    total_quantity = 0
    for i in baskets:
        total_sum += i.sum()
        total_quantity += i.quantity

    context = {'Title':'Профиль',
               'form': form,
               'baskets': baskets,
               'total_sum':total_sum,
               'total_quantity':total_quantity}
    return render(request, 'users/profile.html', context = context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

