from django.shortcuts import render, redirect
from .forms import RegistrationForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
  
def user_logout(req):
  logout(req)
  return redirect('home')

@login_required
def user_profile(req):
  return render(req, 'author/user_profile.html', {'user': req.user})

@login_required
def user_profile_update(req):
  if req.method == 'POST':
    form = ProfileUpdateForm(req.POST, instance = req.user)

    if form.is_valid():
      form.save()
      messages.success(req, 'Profile updated.')
      return redirect('profile-page')
  else:
    form = ProfileUpdateForm(instance = req.user)

  return render(req, 'author/user_profile_update.html', {'form': form})

@login_required
def user_password_change(req):
  if req.method == 'POST':
    form = PasswordChangeForm(req.user, req.POST)

    if form.is_valid():
      form.save()
      update_session_auth_hash(req, form.user)
      messages.success(req, "Password updated.")
      return redirect('profile-page')
  else:
    form = PasswordChangeForm(req.user)

  return render(req, 'author/user_password_change.html', {'form': form})