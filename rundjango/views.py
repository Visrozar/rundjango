from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'home/index.html')
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
            login(request, user)
            return redirect('home:index')

        return render(request, self.template_name, {'form': form})