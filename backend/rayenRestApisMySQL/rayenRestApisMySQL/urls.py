from django.urls import re_path, include

urlpatterns = [
    re_path(r'^', include('tutorials.urls')),  # Use re_path for regular expression
]
