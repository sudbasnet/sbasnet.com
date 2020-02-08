from django.shortcuts import render
from .models import Intro, Art, WorkExperience, Education, Skill, CareerSummary
from django.utils import timezone
from django.http import HttpResponse
from .helper import parse_yarn
import json
import os


intros = Intro.objects.order_by('rank')
artworks = Art.objects.order_by('rank')
work_experiences = WorkExperience.objects.order_by('-start')
summary = CareerSummary.objects.order_by('date_added')[0].body
education = Education.objects.order_by('-start')
skills = Skill.objects.order_by('type_rank')

with open('main/conversation.json', 'r') as conversation_file:
    data = conversation_file.read()
conversation = parse_yarn(json.loads(data))


def home(request):
    return render(request, 'main/home.html', {'intros': intros, 'artwork': artworks, 'conversation': conversation})


def resume(request):
    return render(request, 'main/resume.html', {'summary': summary, 'work': work_experiences, 'edu': education, 'skill': skills})


def rocket(request):
    return render(request, 'main/rocket.html', {})
