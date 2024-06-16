from django.shortcuts import render, redirect
from .forms import AuthorForm

# Create your views here.
def add_author(req):
  if req.method == 'POST':
    form = AuthorForm(req.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = AuthorForm()

  return render(req, 'author/add_author.html', {'form': form})