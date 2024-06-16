from django.urls import path
from . import views

urlpatterns = [
  path('add-category/', views.add_category, name="add-category")  
]
