from django.shortcuts import render
from .models import Lesson


def index(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons_k': lessons,
        'title_k': 'LESSONS LIST'
    }
    return render(request, 'lessons/index.html', context)
