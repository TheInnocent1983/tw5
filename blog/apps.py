from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

# urls.py - Add to your URL patterns
from django.urls import path
from . import views # adjust import based on your project structure
urlpatterns = [
# ... your existing URL patterns ...
path('health/', views.health_check, name='health-check'),
]
