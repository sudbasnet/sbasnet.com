from django.contrib import admin
from .models import Intro, Art, WorkExperience, Education, Skill, CareerSummary
from django.db import models


admin.site.register(Intro)
admin.site.register(CareerSummary)
admin.site.register(Art)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(WorkExperience)
