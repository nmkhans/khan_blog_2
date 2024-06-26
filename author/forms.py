from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'placeholder': 'Enter user name'}))
  first_name = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'placeholder': 'Enter your first name'}))
  last_name = forms.CharField(widget=forms.TextInput(attrs = {'required': True, 'placeholder': 'Enter your last name'}))
  email = forms.EmailField(widget=forms.EmailInput(attrs = {'required': True, 'placeholder': 'Enter your email'}))
  password1 = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder': 'Enter a password'}), label = 'Password')
  password2 = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder': 'Re enter password'}), label = 'Confirm Password')

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']