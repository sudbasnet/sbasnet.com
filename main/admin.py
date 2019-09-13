from django.contrib import admin
from .models import Intro, Art, WorkExperience, Education, Skill, CareerSummary
from tinymce.widgets import TinyMCE
from django.db import models


# TinyMCE allows you to format the text without using HTML tags
class TextAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(Intro)
admin.site.register(CareerSummary)
admin.site.register(Art)
admin.site.register(Education, TextAdmin)
admin.site.register(Skill)
admin.site.register(WorkExperience, TextAdmin)
