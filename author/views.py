from django.shortcuts import render, redirect
from .forms import RegistrationForm 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def user_registration(req):
  if not req.user.is_authenticated:
    if req.method == 'POST':
      form = RegistrationForm(req.POST)

      if form.is_valid():
        form.save()
        messages.success(req, 'Registration completed. Login to continue.')
        return redirect('login-page')
    else:
      form = RegistrationForm()

    return render(req, 'author/user_registration.html', {'form': form})
  else:
    return redirect('profile-page')

def user_login(req):
  if not req.user.is_authenticated:
    if req.method == 'POST':
      form = AuthenticationForm(req, req.POST)

      if form.is_valid():
        cd = form.cleaned_data
        username = cd['username']
        password = cd['password']

        user = authenticate(username = username, password = password)

        if user is not None:
          login(req, user)
          messages.success(req, 'Login successfull.')
          return redirect('profile-page')
        else:
          messages.error(req, 'User not found! Please create a account first.')
          return redirect('registration-page')
    else:
      form = AuthenticationForm()

    return render(req, 'author/user_login.html', {'form': form})
  else:
    return redirect('profile-page')

def user_profile(req):
  if req.user.is_authenticated:
    return render(req, 'author/user_profile.html', {'user': req.user})
  else:
    return redirect('login-page')

def user_logout(req):
  logout(req)
  return redirect('home')