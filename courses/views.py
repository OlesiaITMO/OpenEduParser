from django.shortcuts import render
from .models import *
from .grabber import Grabber
from django.http import HttpResponseRedirect


def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'index.html', context)


def update(request):
    information = Grabber()
    information.get_texts()

    information.save_groups()
    information.save_organizers()
    information.save_courses()

    return HttpResponseRedirect('/')
