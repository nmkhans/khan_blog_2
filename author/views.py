from django.shortcuts import render

# Create your views here.
def add_author(req):
  return render(req, 'author/add_author.html')