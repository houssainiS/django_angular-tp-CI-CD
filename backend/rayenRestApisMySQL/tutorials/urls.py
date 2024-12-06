from django.urls import path, re_path  # Import 'path' and 're_path' instead of 'url'
from tutorials import views

urlpatterns = [
    path('api/tutorials', views.tutorial_list),  # Use 'path' for simpler URL patterns
    re_path(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),  # Use 're_path' for regex
    path('api/tutorials/published', views.tutorial_list_published),  # Use 'path' for simpler URL patterns
]
