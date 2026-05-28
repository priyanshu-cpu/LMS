from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .models import Books
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'Lms/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'Lms/register.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
        
    return render(request,'Lms/login.html')

@login_required
def dashboard(request):
    return redirect(request, 'Lms/dashboard.html')

def logout():
    pass