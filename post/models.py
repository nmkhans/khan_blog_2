from django.db import models
from categories.models import Categories
from author.models import Author

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length = 100)
  content = models.TextField()
  categories = models.ManyToManyField(Categories) 
  # one post has many categories and one category has many post (many to many relation)
  author = models.ForeignKey(Author, on_delete = models.CASCADE)
  # one author has many post but a post has one author (one to many relation)

  def __str__(self):
    return f'Title: {self.title}'