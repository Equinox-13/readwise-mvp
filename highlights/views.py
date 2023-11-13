from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Highlight, Source
from django.http import HttpResponse
from .forms import HighlightForm

# Example view for displaying highlights
@login_required
def display_highlights(request):
    user_highlights = Highlight.objects.filter(user=request.user)
    return render(request, 'highlights/display_highlights.html', {'highlights': user_highlights})


def home(request):
    return HttpResponse("Hello, World!")


@login_required
def add_highlight(request):
    if request.method == 'POST':
        form = HighlightForm(request.POST)
        if form.is_valid():
            new_highlight = form.save(commit=False)
            new_highlight.user = request.user
            new_highlight.save()
            # Redirect to a success page or wherever appropriate
    else:
        form = HighlightForm()
    return render(request, 'highlights/add_highlight.html', {'form': form})