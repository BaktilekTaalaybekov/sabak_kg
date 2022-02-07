from django.shortcuts import render, get_object_or_404, redirect
from .models import Lesson, Category
from .forms import LessonForm


def index(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons_k': lessons,
        'title_k': 'LESSONS LIST',
    }
    return render(request, 'lessons/index.html', context)


def get_category(request, category_id):
    lessons = Lesson.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'lessons/category.html',
                  {'lessons_k_gk': lessons, 'category_k_gk': category})


def view_lesson(request, lesson_id):
    # lesson_item = Lesson.objects.get(pk=lesson_id)
    lesson_item = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'lessons/view_lesson.html', {"lesson_item": lesson_item})


def add_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            lesson = form.save()
            return redirect(lesson)

            form = LessonForm()

    else:
        form = LessonForm()

    return render(request, 'lessons/add_lesson.html', {'form': form})
