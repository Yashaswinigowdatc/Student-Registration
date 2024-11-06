from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, StudentRegistrationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import  StudentRegistration


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('register')  # Redirect to the registration page or another page
    else:
        form = LoginForm()
    return render(request, 'student_registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('success')
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_registration/register.html', {'form': form})

def registration_success(request):
    return render(request, 'student_registration/success.html')
    
@login_required
def student_list(request):
    students = StudentRegistration.objects.all()
    return render(request, 'registration/student_list.html', {'students':students})

def user_logout(request):
    logout(request)
    return redirect('login')
