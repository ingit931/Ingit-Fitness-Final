from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm, CreateUserForm

from django.contrib.auth.decorators import login_required
from .models import Profile

def homepage(request):
    return render(request, 'accounts/homepage.html')


def register_user(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, username=user.username,
                                   email = user.email)
            messages.add_message(request, messages.SUCCESS, 'User registered successfully')
            return redirect('/login')
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong')
            return render(request, 'accounts/register.html', {'form_user': form})
    context = {
        'form_user': CreateUserForm,
        'activate_register': 'active'
    }
    return render(request, 'accounts/register.html', context)


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'],
                                password=data['password'])
            #print(user)
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return redirect('/admins')
                elif not user.is_staff:
                    login(request, user)
                    return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'Invalid Username or Password')
                return render(request, 'accounts/login.html', {'form_login':form})
    context = {
        'form_login': LoginForm,
        'activate_login': 'active'
    }
    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('/login')














