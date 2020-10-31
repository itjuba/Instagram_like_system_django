from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.template import RequestContext
from .forms import LoginForm ,RegisterForm
from django.contrib import  auth

# Create your views here.



def signup(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'accounts/signup.html', {'form': form})



def login(request):
    form = LoginForm(request.POST or None)
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        print(request.user.is_authenticated)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            print('error')
    return render(request, 'accounts/login.html', {'form': form})


def logout(request):
     if request.method == 'POST':
            auth.logout(request)
            return redirect('home')

