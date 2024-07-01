from django.db import models
from categories.models import Categories
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length = 100)
  content = models.TextField()
  categories = models.ManyToManyField(Categories) 
  # one post has many categories and one category has many post (many to many relation)
  author = models.ForeignKey(User, on_delete = models.CASCADE)
  # one author has many post but a post has one author (one to many relation)
  image = models.ImageField(upload_to='', blank = True, null = True)

  def __str__(self):
    return f'Title: {self.title}'
  
class Comment(models.Model):
  name = models.CharField(max_length = 255)
  email = models.EmailField()
  body = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')

  def __str__(self):
    return f'Comment by {self.name}'