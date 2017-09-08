from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View

def index(request):
    if request.user.is_authenticated:
        return render(request, str(request.user.groups.all()[0]) + '/index.html')
    return redirect('login')

