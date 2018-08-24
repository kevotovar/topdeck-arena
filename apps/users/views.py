from django.contrib.auth import logout
from django.shortcuts import render, redirect


def login(request):
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')
