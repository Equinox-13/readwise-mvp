from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Highlight, Source
from django.http import HttpResponse
from .forms import HighlightForm, SampleForm

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
        print("insdie=========post")
        if form.is_valid():
            print("========not inside")
            new_highlight = form.save(commit=False)
            new_highlight.user = request.user
            new_highlight.save()
            print("inside===============")
            return HttpResponseRedirect("/thanks/")
            # Redirect to a success page or wherever appropriate
    else:
        form = HighlightForm()
    return render(request, 'highlights/add_highlight.html', {'form': form})


@login_required
def add_sample(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
        print("insdie=========post")
        print("Is form valid====>", form.is_valid())
        print(form.errors)
        if form.is_valid():
            print("========not inside")
            new_highlight = form.save(commit=False)
            # new_highlight.user = request.user
            new_highlight.save()
            print("inside===============")
            return HttpResponse("thanks for submitting")
            # Redirect to a success page or wherever appropriate
    else:
        form = HighlightForm()
    return render(request, 'highlights/sample.html', {'form': form})