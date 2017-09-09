from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.models import User, Group
from django.template import RequestContext


def error404(request):
    if request.user.is_authenticated:
        return render(request, 'home/404.html')
    return redirect('login')

def index(request):
    if request.user.is_authenticated:
        return render(request, str(request.user.groups.all()[0]) + '/index.html')
    return redirect('login')

def logout_template(request):
    logout(request)
    return redirect('login')

class UserFormView(View):
    form_class = UserForm
    template_name = 'home/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.groups.filter(name='home').exists():
                login(request, user)
                return redirect('home:index')
            elif user.groups.filter(name='axe').exists():
                login(request, user)
                return redirect('axe:index')
            elif user.groups.filter(name='chief').exists():
                login(request, user)
                return redirect('chief:index')
            elif user.groups.filter(name='dell').exists():
                login(request, user)
                return redirect('dell:index')
            else:
                return render(request,'home/noCompany.html')
            
        else:
            return redirect('login')

        return render(request, self.template_name, {'form': form})