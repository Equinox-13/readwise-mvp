from django.db import models
from django.contrib.auth.models import User


class Source(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    
    SOURCE_CHOICES = [
        ('book', 'Book'),
        ('article', 'Article'),
        ('other', 'Other'),
    ]
    source_type = models.CharField(max_length=20, choices=SOURCE_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.title

class Highlight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Other fields like tags, notes, etc.

    def __str__(self):
        return f"{self.source.title} - {self.content[:50]}..."

class Sample(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
