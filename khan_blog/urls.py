from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('category/<slug:category_slug>/', views.home, name = 'filter-by-category'),
    path('search/<str:search_term>/', views.search, name = 'search'),
    path('author/', include('author.urls')),
    path('categories/', include('categories.urls')),
    path('post/', include('post.urls')),
]
