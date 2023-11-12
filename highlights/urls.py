from django.urls import path
from . import views

urlpatterns = [
    path('highlights/', views.display_highlights, name='display_highlights'),
    # Define other URL patterns for different views
]