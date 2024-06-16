from django import forms
from . import models

class CategoryForm(forms.ModelForm):
  class Meta:
    model = models.Categories
    fields = '__all__'