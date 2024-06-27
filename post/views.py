from django.shortcuts import render, redirect
from .forms import PostForm 
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_post(req):
  if req.method == 'POST':
    form = PostForm(req.POST)

    if form.is_valid():
      form.instance.author = req.user
      form.save()
      return redirect('home')
  else:
    form = PostForm()

  return render(req, 'posts/add_post.html', {'form': form})

@login_required
def edit_post(req, id):
  post = Post.objects.get(pk=id)

  if req.method == 'POST':
    form = PostForm(req.POST, instance = post)
    if form.is_valid():
      form.instance.author = req.user
      form.save()
      return redirect('home')
  else:
    form = PostForm(instance = post)

  return render(req, 'posts/add_post.html', {'form': form})

@login_required
def delete_post(req, id):
  Post.objects.get(pk = id).delete()

  return redirect('home')