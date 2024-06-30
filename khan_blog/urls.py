from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('category/<slug:category_slug>/', views.home, name = 'filter-by-category'),
    path('search/<str:search_term>/', views.search, name = 'search'),
    path('author/', include('author.urls')),
    path('categories/', include('categories.urls')),
    path('post/', include('post.urls')),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)