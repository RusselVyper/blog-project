from django.shortcuts import render, redirect
from django.http import HttpResponse    
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory 
from django.contrib.auth import authenticate, login, logout


from .models import *
from .forms import CreateUserForm


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('blog:home')

