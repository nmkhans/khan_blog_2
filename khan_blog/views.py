from django.shortcuts import render
from post.models import Post

def home(req):
  data = Post.objects.all()
  return render(req, 'index.html', {'data': data})