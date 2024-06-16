from django.shortcuts import render, redirect
from .forms import CategoryForm

# Create your views here.
def add_category(req):
  if req.method == 'POST':
    form = CategoryForm(req.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = CategoryForm()

  return render(req, 'categories/add_category.html', {'form': form})