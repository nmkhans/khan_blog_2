from django.shortcuts import render
from post.models import Post

def home(req):
  data = Post.objects.all()
  return render(req, 'index.html', {'data': data})

def search(req, search_term):
  # posts = Post.objects.get(title = search_term)
  # print(posts.id)
  return render(req, 'search.html', {'search_term': search_term})