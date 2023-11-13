from django.urls import path
from . import views

urlpatterns = [
    path('display_highlights/', views.display_highlights, name='display_highlights'),
    path('add_highlight/', views.add_highlight, name='add_highlight'),
    # Define other URL patterns for different views
]