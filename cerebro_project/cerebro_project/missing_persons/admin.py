# missing_persons/admin.py
from django.contrib import admin
from .models import Missing_person, Eyecolor, Race, Comment
from django.forms import TextInput, Textarea
from django.db import models

class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
admin.site.register(Missing_person, YourModelAdmin)
admin.site.register(Eyecolor)
admin.site.register(Race)
admin.site.register(Comment)