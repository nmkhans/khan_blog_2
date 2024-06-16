from django.shortcuts import render, redirect
from .forms import PostForm 
from .models import Post

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

def edit_post(req, id):
  post = Post.objects.get(pk=id)

  if req.method == 'POST':
    form = PostForm(req.POST, instance = post)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = PostForm(instance = post)

  return render(req, 'posts/add_post.html', {'form': form})

def delete_post(req, id):
  Post.objects.get(pk = id).delete()

  return redirect('home')