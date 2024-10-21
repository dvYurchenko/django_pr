from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import  LoginForm


def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'users/login.html',{'form':form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Привет {username.title()}, Добро пожаловать!')
                return redirect("home")

        messages.error(request, 'invalid username/password')
        return render(request, 'users/login.html', {'form':form})

def sign_out(request):
    logout(request)
    messages.success(request, 'Вы вышли из аккаунта')
    return redirect('login')
