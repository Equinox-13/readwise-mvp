from django import forms
from .models import Highlight

class HighlightForm(forms.ModelForm):
    class Meta:
        model = Highlight
        fields = ['source', 'content']  # Add other fields as needed