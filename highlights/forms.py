from django import forms
from .models import Highlight, Sample

class HighlightForm(forms.ModelForm):
    class Meta:
        model = Highlight
        fields = ['source', 'content']  # Add other fields as needed


class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ['title', 'author']

    