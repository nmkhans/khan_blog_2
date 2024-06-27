from django.shortcuts import render
from post.models import Post
from categories.models import Categories

def home(req, category_slug = None):
  posts = Post.objects.all()
  categories = Categories.objects.all()

  if category_slug is not None:
    category = Categories.objects.get(slug = category_slug)

    posts = Post.objects.filter(categories = category)

  return render(req, 'index.html', {'data': posts, 'categories': categories})

def search(req, search_term):
  # posts = Post.objects.get(title = search_term)
  # print(posts.id)
  return render(req, 'search.html', {'search_term': search_term})