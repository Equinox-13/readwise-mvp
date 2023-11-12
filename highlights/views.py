from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Highlight, Source

# Example view for displaying highlights
@login_required
def display_highlights(request):
    user_highlights = Highlight.objects.filter(user=request.user)
    return render(request, 'highlights/display_highlights.html', {'highlights': user_highlights})