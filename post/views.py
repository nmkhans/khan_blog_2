from django.shortcuts import render, redirect
from .forms import PostForm 

# Create your views here.
def add_post(req):
  if req.method == 'POST':
    form = PostForm(req.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = PostForm()

  return render(req, 'posts/add_post.html', {'form': form})