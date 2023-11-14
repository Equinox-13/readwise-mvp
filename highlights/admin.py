from django.contrib import admin

from .models import Source, Highlight, Sample

admin.site.register(Source)
admin.site.register(Highlight)
admin.site.register(Sample)
