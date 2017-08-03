from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'home/index.html')
    return redirect('login')

def mrcaerialSandown(request):
    if request.user.is_authenticated:
        return render(request, 'home/mrcaerialSandown.html')
    return redirect('login')

def mrcaerialMornington(request):
    if request.user.is_authenticated:
        return render(request, 'home/mrcaerialMornington.html')
    return redirect('login')

def mrcaerialCaulfield(request):
    if request.user.is_authenticated:
        return render(request, 'home/mrcaerialCaulfield.html')
    return redirect('login')