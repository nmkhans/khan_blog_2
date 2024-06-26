from django.urls import path
from . import views

urlpatterns = [
  path('user-registration/', views.user_registration, name = 'registration-page'),
  path('user-login/', views.UserLoginView.as_view(), name = 'login-page'),
  path('user-logout/', views.user_logout, name = 'logout-page'),
  path('user-profile/', views.user_profile, name = 'profile-page'),
  path('user-profile-update/', views.user_profile_update, name = 'profile-update-page'),
  path('user-password-change/', views.user_password_change, name = 'password-change-page'),
  path('all-posts-by-user/', views.all_posts_by_user, name = 'all-posts-by-user'),
]
