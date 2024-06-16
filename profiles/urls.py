from django.urls import path
from . import views

urlpatterns = [
  path('add-profile/', views.add_profile, name='add-profile')    
]
