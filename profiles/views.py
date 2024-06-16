from django.shortcuts import render, redirect
from .forms import ProfileForm

# Create your views here.
def add_profile(req):
  if req.method == 'POST':
    form = ProfileForm(req.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = ProfileForm()

  return render(req, 'profiles/add_profile.html', {'form': form})