from django.urls import path
from . import views

urlpatterns = [
  # path('add-post/', views.add_post, name='add-post') ,
  path('add-post/', views.AddPostView.as_view(), name='add-post') ,
  path('edit-post/<int:id>/', views.EditPostView.as_view(), name="edit-post"), 
  path('delete-post/<int:id>/', views.DeletePostView.as_view(), name="delete-post") 
]
