from django.db import models
from django.contrib.auth.models import User


class Source(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    # Add other fields like publication date, source type (book, article, etc.)

    def __str__(self):
        return self.title

class Highlight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    content = models.TextField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    # Other fields like tags, notes, etc.

    def __str__(self):
        return f"{self.source.title} - {self.content[:50]}..."
